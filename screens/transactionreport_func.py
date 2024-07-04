from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog, QMessageBox
from screens.transactionreportUI import Ui_MainWindow
from mysql.connector import Error
import csv
from datetime import datetime


class TransactionReportWindow(QMainWindow, Ui_MainWindow):
    # Signals for button actions
    save_button = QtCore.pyqtSignal()
    back_button = QtCore.pyqtSignal()
    logout_button = QtCore.pyqtSignal()
    help_button = QtCore.pyqtSignal()
    clientreport_button = QtCore.pyqtSignal()
    coachesreport_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(TransactionReportWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn  # Store the database connection

        # Connect UI signals to methods
        self.savetodesktop.clicked.connect(self.generate_report)
        self.back.clicked.connect(self.backbutton_clicked)
        self.clients.clicked.connect(self.handle_clientreport)
        self.logout.clicked.connect(self.handle_logout)
        self.coaches.clicked.connect(self.handle_coachesreport)
        self.help.clicked.connect(self.handle_help)

        # Initialize table
        self.set_tableElements()
        self.disable_editing()
        self.calculate_total_amount()

    def load_data(self):
        cursor = self.conn.cursor()

        # Fetch data from payments table joined with booking table
        cursor.execute("""
            SELECT p.Receipt_Number, p.Booking_ID, p.Transaction_Handler, p.PaymentDate, p.Amount_Total,
                   p.Change, p.Amount_Received, b.Client_Name, b.Package_Name
            FROM payments p
            INNER JOIN booking b ON p.Booking_ID = b.BookingID
        """)
        results = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]

        cursor.close()
        return results, column_names

    def set_tableElements(self):
        results, column_names = self.load_data()
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(results))

        # Set the column headers
        self.tableWidget.setHorizontalHeaderLabels(column_names)

        # Set font and background color for the table
        font = QtGui.QFont("Arial Black", 14)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: white;")

        for row_number, row_data in enumerate(results):
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

    def disable_editing(self):
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)

    def calculate_total_amount(self):
        total_amount = 0.00

        # Find the index of the 'Amount_Total' column
        column_index = -1
        for i in range(self.tableWidget.columnCount()):
            if self.tableWidget.horizontalHeaderItem(i).text() == "Amount_Total":
                column_index = i
                break

        if column_index == -1:
            QMessageBox.critical(self, "Error", "Amount_Total column not found.")
            return

        # Calculate the total amount from the 'Amount_Total' column
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, column_index)
            if item is not None and item.text().strip() != "":
                total_amount += float(item.text().strip())

        # Set the total amount with two decimal places
        self.totalamount_2.setText(f"{total_amount:.2f}")

    def generate_report(self):
        # Get report name and current month
        report_name = self.reportname.toPlainText().strip()
        current_month = self.currentmonth.toPlainText().strip()  # Fetch text from QTextEdit

        if not report_name:
            QMessageBox.warning(self, "Warning", "Please enter a report name.")
            return

        # Get additional metadata
        company_name = "Anytime Fitness - The Garden Walk"  # Replace with actual company name
        address = "105 Felix Ave, Santo Domingo, Cainta, 1900 Rizal"  # Replace with actual address
        contact_details = "0926 679 1189"  # Replace with actual contact details
        report_title = self.reportname.toPlainText().strip()  # Use the reportname QTextEdit for the report title
        created_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Fetch report creator (assuming you have user details in your database)
        report_creator = self.fetch_report_creator()  # Replace with actual method to fetch user's first name and last name

        # Generate filename with current date, selected month, and report name
        current_date = datetime.now().strftime('%Y-%m-%d')
        filename = f"{current_date}_{current_month}_{report_name}.csv"

        # Open file dialog to save the report
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Report", "", "CSV Files (*.csv)")

        if file_path:
            try:
                with open(file_path, mode='w', newline='') as file:
                    writer = csv.writer(file)

                    # Write metadata or header with date and report name
                    writer.writerow(["Name of Company:", company_name])
                    writer.writerow(["Address:", address])
                    writer.writerow(["Contact Details:", contact_details])
                    writer.writerow(["Title of Report:", report_title])
                    writer.writerow(["Date and Time Created:", created_datetime])
                    writer.writerow(["Report Creator:", report_creator])
                    writer.writerow(["Month:", current_month])
                    writer.writerow([])  # Empty line for separation

                    # Write table headers
                    headers = [self.tableWidget.horizontalHeaderItem(i).text() for i in
                               range(self.tableWidget.columnCount())]
                    writer.writerow(headers)

                    # Write table data
                    for row in range(self.tableWidget.rowCount()):
                        row_data = []
                        for column in range(self.tableWidget.columnCount()):
                            item = self.tableWidget.item(row, column)
                            if item is not None:
                                row_data.append(item.text())
                            else:
                                row_data.append("")
                        writer.writerow(row_data)

                    # Add totals as new rows
                    writer.writerow([])  # Empty line for separation
                    writer.writerow(['Total Amount', self.totalamount_2.text()])

                QMessageBox.information(self, "Success", f"Report saved successfully as {filename}")
                self.save_button.emit()

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error saving report: {str(e)}")

    def fetch_report_creator(self):
        # Assuming you have a method to fetch the logged-in user's first name and last name from the database
        # Replace with actual query and logic to fetch user's name
        user_id = 3  # Replace with actual user ID or identifier of the logged-in user
        cursor = self.conn.cursor()
        cursor.execute("SELECT first_name, last_name FROM employees WHERE EmployeeID = %s", (user_id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            first_name, last_name = result
            return f"{first_name} {last_name}"
        else:
            return "Unknown User"  # Handle if no user found or default value

    def refresh_data(self):
        self.tableWidget.clearContents()
        self.set_tableElements()
        self.disable_editing()

    def backbutton_clicked(self):
        print("Back")
        self.back_button.emit()

    def handle_clientreport(self):
        self.clientreport_button.emit()

    def log_user_logout(self):
        if self.current_user_id is None:
            print("No current user logged in")  # Debug print
            return

        try:
            cursor = self.conn.cursor()
            # Retrieve the latest LogID
            cursor.execute("SELECT MAX(LogID) FROM user_logs")
            last_log_id = cursor.fetchone()[0]

            if last_log_id is not None:
                query = """
                    UPDATE user_logs
                    SET Logout_Time = NOW()
                    WHERE LogID = %s AND Logout_Time IS NULL
                """
                cursor.execute(query, (last_log_id,))
                self.conn.commit()
                print(f"Logout time updated for LogID: {last_log_id}")  # Debug print
            else:
                print("No LogID found to update logout time")  # Debug print

        except Error as e:
            print(f"Error logging user logout: {e}")
        finally:
            cursor.close()
            self.current_user_id = None  # Clear the current user ID after logging out
            self.current_user_type = None  # Clear the current user type after logging out


    def handle_logout(self):
        print("Logging out user")
        self.log_user_logout()
        self.logout_button.emit()

    def handle_coachesreport(self):
        self.coachesreport_button.emit()

    def handle_help(self):
        pdf_path = "C:\\Users\\JC\\Desktop\\softeng-main\\Anytime Fitness User Manual.pdf"
        QDesktopServices.openUrl(QUrl.fromLocalFile(pdf_path))
