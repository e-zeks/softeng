from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QMessageBox, QFileDialog
from screens.transactionsuccessfulUI import Ui_MainWindow
import mysql.connector
from mysql.connector import Error
from PyQt5.QtGui import QGuiApplication, QPixmap, QDesktopServices


class TransactionSuccessfulWindow(QMainWindow, Ui_MainWindow):
    confirm_button = QtCore.pyqtSignal()
    save_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(TransactionSuccessfulWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn

        # Connect confirm button signal
        self.Confirm.clicked.connect(self.handle_confirm)
        self.help.clicked.connect(self.handle_help)
        self.schedule_line_edits = [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5,
                                    self.lineEdit_6, self.lineEdit_7]
        self.disable_and_remove_borders()

        self.save.clicked.connect(self.take_screenshot)

    def handle_help(self):
        pdf_path = "C:\\Users\\JC\\Desktop\\softeng-main\\Anytime Fitness User Manual.pdf"
        QDesktopServices.openUrl(QUrl.fromLocalFile(pdf_path))

    def take_screenshot(self):
        try:
            # Get the screen where the window is displayed
            screen = QGuiApplication.primaryScreen()

            # Grab the window
            screenshot = screen.grabWindow(self.winId())

            # Define the file path and name
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Screenshot", "", "PNG Files (*.png)")

            if file_path:
                # Save the screenshot
                screenshot.save(file_path, 'png')
                QMessageBox.information(self, "Success", "Screenshot saved successfully.")
            else:
                QMessageBox.warning(self, "Warning", "Screenshot save canceled.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error taking screenshot: {e}")

    def handle_confirm(self):
        try:
            clientdetails = self.clientdetails
            selectedcoach = self.selectedcoach
            selectedpackage = self.selectedpackage
            sessioncount = self.sessioncount
            total_amount = self.total_amount
            selectedsched = self.selectedsched

            self.save_to_database(clientdetails, selectedcoach, selectedpackage, sessioncount, total_amount,
                                  selectedsched)
            self.log_client_logout()
            print("logging out user")
            self.confirm_button.emit()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def disable_and_remove_borders(self):
        # Create a style sheet to remove borders
        style_sheet = """
            QLineEdit {
                border: none;
                padding: 2px; /* Optional: Add padding to improve appearance */
            }
        """

        # Apply the style sheet and disable all line edits
        for line_edit in self.findChildren(QLineEdit):
            line_edit.setStyleSheet(style_sheet)
            line_edit.setReadOnly(True)  # Set read-only mode

    def populate_fields(self, clientdetails, selectedcoach, selectedpackage, sessioncount, selectedsched):
        # Store details in instance variables
        self.clientdetails = clientdetails
        self.selectedcoach = selectedcoach
        self.selectedpackage = selectedpackage
        self.sessioncount = sessioncount
        self.selectedsched = selectedsched

        # Calculate the additional cost for the sessions correctly
        additional_sessions = sessioncount - selectedpackage['min_sessions']
        additional_cost = additional_sessions * 500

        # Calculate total amount
        self.total_amount = selectedpackage['package_price'] + additional_cost

        # Populate line edits with data
        print(clientdetails, selectedcoach, selectedpackage, sessioncount, selectedsched)

        self.coachline.setText(selectedcoach['full_name'])

        self.programplanline.setText(clientdetails['Program_Plan'])
        self.packageline.setText(selectedpackage['package_name'])
        self.numberofsessionsline.setText(str(sessioncount))
        self.totalamtline.setText(str(self.total_amount))

        # Populate selected schedules
        self.populate_selected_schedules(selectedsched)

    def populate_selected_schedules(self, selectedsched):
        # Clear all schedule line edits
        for line_edit in self.schedule_line_edits:
            line_edit.clear()

        # Assuming selectedsched is a dictionary containing session details
        for i, (day, details) in enumerate(selectedsched.items()):
            if i < len(self.schedule_line_edits):
                start_time = details.get('start', '')
                end_time = details.get('end', '')
                self.schedule_line_edits[i].setText(f"{day}: {start_time} - {end_time}")

    def save_to_database(self, clientdetails, selectedcoach, selectedpackage, sessioncount, total_amount,
                         selectedsched):
        # Extract necessary details
        coach_name = selectedcoach['full_name']
        client_name = clientdetails['Username']
        program_plan = clientdetails['Program_Plan']
        package_name = selectedpackage['package_name']

        try:
            cursor = self.conn.cursor()

            # Insert into Booking table
            booking_query = """
            INSERT INTO Booking (Coach_Name, Client_Name, Program_Plan, Package_Name, Session_Count, Total_Price)
            VALUES (%s, %s, %s, %s, %s, %s);
            """
            cursor.execute(booking_query,
                           (coach_name, client_name, program_plan, package_name, sessioncount, total_amount))
            self.conn.commit()

            # Get the last inserted BookingID
            booking_id = cursor.lastrowid

            # Insert into Sessions table
            for day, details in selectedsched.items():
                start_time = details.get('start', '')
                end_time = details.get('end', '')
                session_query = """
                INSERT INTO Sessions (BookingID, Day, StartTime, EndTime, Session_Counter)
                VALUES (%s, %s, %s, %s, %s);
                """
                cursor.execute(session_query, (booking_id, day, start_time, end_time, sessioncount))
            self.conn.commit()

            cursor.close()

            # Show confirmation message box
            QMessageBox.information(self, "Transaction Successful", "Transaction has been successfully saved.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            QMessageBox.critical(self, "Database Error", f"An error occurred while saving to the database: {err}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")

    def log_client_logout(self):
        try:
            cursor = self.conn.cursor()
            # Update the logout time for the current client

            clientdetails = list(self.clientdetails)
            sql = """
                UPDATE user_logs
                SET Logout_Time = NOW()
                WHERE ClientID = (SELECT ClientID FROM clients WHERE Username = %s)
                AND Logout_Time IS NULL
            """
            cursor.execute(sql, (clientdetails[1],))  # Assuming clientdetails[1] contains Username
            self.conn.commit()
            cursor.close()
            print("Logout time updated for client")  # Debug print

        except Error as e:
            print(f"Error logging client logout: {e}")
            QMessageBox.critical(self, "Error", f"Error logging client logout: {e}")
