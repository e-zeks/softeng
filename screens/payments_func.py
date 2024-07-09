from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic.properties import QtCore
from PyQt5.QtCore import pyqtSignal
from screens.paymentsUI import Ui_MainWindow
from mysql.connector import Error


class PaymentWindow(QMainWindow, Ui_MainWindow):
    # Screen buttons
    back_button = pyqtSignal()
    save_button = pyqtSignal()

    # Nav bar buttons (assuming these are defined elsewhere similarly)
    employeemanage_button = pyqtSignal()
    clientmanage_button = pyqtSignal()
    reports_button = pyqtSignal()
    userlogs_button = pyqtSignal()
    maintenance_button = pyqtSignal()
    help_button = pyqtSignal()
    logout_button = pyqtSignal()

    def __init__(self, conn):
        super(PaymentWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn
        self.current_user_id = 1  # Store the current user's ID
        self.current_user_type = 'Admin'  # Store the current user's type as a string

        # Screen buttons connections
        self.back.clicked.connect(self.backbutton_clicked)
        self.save.clicked.connect(self.save_clicked)
        self.username.textChanged.connect(self.auto_generate_fields_and_receipt)  # Connect textChanged signal

        # Nav bar button connections (assuming these are implemented elsewhere)
        self.employees.clicked.connect(self.handle_employees)
        self.clients.clicked.connect(self.handle_clients)
        self.report.clicked.connect(self.handle_reports)
        self.userlogs.clicked.connect(self.handle_userlogs)
        self.maintenance.clicked.connect(self.handle_maintenance)
        self.help.clicked.connect(self.handle_help)
        self.logout.clicked.connect(self.handle_logout)

        # Generate Change Button connection
        self.calculate.clicked.connect(self.calculate_change)

    def auto_generate_fields_and_receipt(self):
        try:
            username = self.username.text().strip()
            if not username:
                return  # If username is empty, do nothing

            cursor = self.conn.cursor(dictionary=True)
            print("Cursor created for auto_generate_fields_and_receipt")

            # Query to get unpaid bookings for the given username
            query = """
            SELECT BookingID, Total_Price, NOW() as PaymentDate
            FROM Booking
            WHERE Client_Name = %s AND Status = 'unpaid'
            """
            cursor.execute(query, (username,))
            booking = cursor.fetchone()

            if booking:
                # Populate fields if a booking is found
                self.amttotal.setText(str(booking['Total_Price']))
                self.bookingid.setText(str(booking['BookingID']))
                self.paydate.setText(booking['PaymentDate'].strftime('%Y-%m-%d %H:%M:%S'))

                # Generate the receipt number
                receipt_cursor = self.conn.cursor()
                query = "SELECT MAX(Receipt_Number) AS max_receipt FROM Payments"
                receipt_cursor.execute(query)
                last_receipt = receipt_cursor.fetchone()[0]

                if last_receipt is None:
                    receipt_number = 1000
                else:
                    receipt_number = last_receipt + 1

                # Save the receipt number to the database
                insert_query = "INSERT INTO Payments (Receipt_Number) VALUES (%s)"
                receipt_cursor.execute(insert_query, (receipt_number,))
                self.conn.commit()  # Commit the transaction

                receipt_cursor.close()

                # Update the receipt number in the QLineEdit
                self.receiptno.setText(str(receipt_number))  # Update the receipt number in QLineEdit

                print(f"Receipt number generated: {receipt_number}")  # Debug print

            else:
                # Clear fields if no booking is found
                self.amttotal.clear()
                self.bookingid.clear()
                self.paydate.clear()
                self.receiptno.clear()

            cursor.close()

        except Error as e:
            print(f"Error auto generating fields and receipt: {e}")
            QMessageBox.critical(self, "Error", f"Error auto generating fields and receipt: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            QMessageBox.critical(self, "Error", f"Unexpected error: {e}")

    def calculate_change(self):
        try:
            amt_total = float(self.amttotal.text()) if self.amttotal.text() else 0.0
            amt_paid = float(self.amtpaid.text()) if self.amtpaid.text() else 0.0
            if amt_paid < 0:
                QMessageBox.critical(self, "Error", "Amount paid cannot be negative.")
                return
            change = amt_paid - amt_total
            self.code.setText(f"{change:.2f}")
        except ValueError as ve:
            self.code.clear()  # Clear the change field if there's a conversion error

    def save_clicked(self):
        try:
            # Get the receipt number from the UI
            receipt_number = int(self.receiptno.text()) if self.receiptno.text() else None
            if receipt_number is None:
                QMessageBox.critical(self, "Error", "Receipt number could not be generated.")
                return

            # Prepare SQL query to update payments table
            query_payments = """
            UPDATE payments
            SET Transaction_Handler = %(transaction_handler)s,
                Booking_ID = %(booking_id)s,
                PaymentDate = %(payment_date)s,
                Amount_Total = %(amount_total)s,
                Amount_Received = %(amount_received)s,
                `Change` = %(change)s
            WHERE Receipt_Number = %(receipt_number)s
            """

            # Prepare SQL query to update booking table status to 'paid'
            query_booking_update = """
            UPDATE Booking
            SET Status = 'paid'
            WHERE BookingID = %(booking_id)s
            """

            # Ensure values are retrieved from QLineEdit correctly and converted to correct data types
            transaction_handler = self.transactionhandler.text() if self.transactionhandler.text() else None
            booking_id = int(self.bookingid.text()) if self.bookingid.text() else None
            payment_date = self.paydate.text() if self.paydate.text() else None
            amount_total = float(self.amttotal.text()) if self.amttotal.text() else None
            amount_received = float(self.amtpaid.text()) if self.amtpaid.text() else None
            change = float(self.code.text()) if self.code.text() else None

            if amount_received is not None and amount_received < 0:
                QMessageBox.critical(self, "Error", "Amount paid cannot be negative.")
                return

            values_payments = {
                'receipt_number': receipt_number,
                'transaction_handler': transaction_handler,
                'booking_id': booking_id,
                'payment_date': payment_date,
                'amount_total': amount_total,
                'amount_received': amount_received,
                'change': change
            }

            values_booking_update = {
                'booking_id': booking_id
            }

            # Execute the query and commit the transaction for payments table
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(query_payments, values_payments)
            self.conn.commit()

            # Execute the query and commit the transaction for booking table update
            cursor.execute(query_booking_update, values_booking_update)
            self.conn.commit()

            cursor.close()
            QMessageBox.information(self, "Success", "Payment details updated successfully.")

        except ValueError as ve:
            # Handle value conversion errors (e.g., int() or float())
            QMessageBox.critical(self, "Error", f"Value conversion error: {ve}")

        except Error as e:
            print(f"Error updating payment details: {e}")
            QMessageBox.critical(self, "Error", f"Error updating payment details: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")
            QMessageBox.critical(self, "Error", f"Unexpected error: {e}")

    def backbutton_clicked(self):
        self.back_button.emit()

    # Other button handlers and signals (e.g., handle_employees, handle_clients, etc.) should be defined here

    # Nav bar buttons
    def handle_employees(self):
        self.employeemanage_button.emit()

    def handle_clients(self):
        self.clientmanage_button.emit()

    def handle_reports(self):
        self.reports_button.emit()

    def handle_userlogs(self):
        self.userlogs_button.emit()

    def handle_maintenance(self):
        self.maintenance_button.emit()

    def handle_help(self):
        self.help_button.emit()

    def handle_logout(self):
        print("Logging Out")
        self.log_user_logout()
        self.logout_button.emit()

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