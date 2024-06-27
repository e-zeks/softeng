import mysql
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from screens.enterOTPUI import Ui_MainWindow


class BookingOTPWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    resend_button = QtCore.pyqtSignal()
    verifyOTP_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(BookingOTPWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn
        self.sent_otp = ""
        self.data_tuple = ""

        self.back.clicked.connect(self.button_clicked)
        #self.resendOTP.clicked.connect()
        self.verifyOTP.clicked.connect(self.handle_verifyOTP)

        self.otp_fields = [self.otp1, self.otp2, self.otp3, self.otp4, self.otp5, self.otp6]
        for otp_field in self.otp_fields:
            otp_field.setMaxLength(1)
            otp_field.textChanged.connect(self.handle_text_change)

    def set_otp(self, otp):
        self.sent_otp = otp

    def handle_resend(self):
        self.resend_button.emit()

    def set_data_tuple(self, data_tuple):
        self.data_tuple = data_tuple

    def button_clicked(self):
        self.back_button.emit()

    def handle_text_change(self, text):
        sender = self.sender()
        if len(text) == 1:
            next_index = self.otp_fields.index(sender) + 1
            if next_index < len(self.otp_fields):
                self.otp_fields[next_index].setFocus()

    def clear_otp_fields(self):
        for otp_field in self.otp_fields:
            otp_field.clear()

    def handle_verifyOTP(self):
        entered_otp = ''.join([field.text() for field in self.otp_fields])
        print(self.sent_otp)
        print(self.data_tuple)
        if entered_otp == self.sent_otp:
            self.clear_otp_fields()
            try:
                cursor = self.conn.cursor()
                # Execute the SQL INSERT statement to add the client to the database
                cursor.execute(
                    """
                    INSERT INTO clients (Last_Name, First_Name, Address, Birthdate, Contact_Number, Email, Username, Password, Program_Plan, Conditions)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    self.data_tuple
                )
                self.conn.commit()  # Commit the transaction
                QMessageBox.information(self, "Success", "Client registered successfully.")
                self.verifyOTP_button.emit()

            except mysql.connector.Error as e:
                QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
                self.conn.rollback()  # Rollback the transaction on error
        else:
            QMessageBox.warning(self, "Failed", "Invalid OTP! Please try again.")
