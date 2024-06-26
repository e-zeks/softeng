from datetime import datetime, timedelta
import hashlib
from mysql.connector import Error
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from screens.loginUI import Ui_MainWindow

class LoginWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    forgot_button = QtCore.pyqtSignal()
    loginadmin_button = QtCore.pyqtSignal()
    logincoach_button = QtCore.pyqtSignal()
    loginauditor_button = QtCore.pyqtSignal()
    loginclient_button = QtCore.pyqtSignal(dict)

    def __init__(self, conn):
        super(LoginWindow, self).__init__()
        self.conn = conn
        self.setupUi(self)

        self.failed_attempts = {}  # Dictionary to store failed attempts
        self.back.clicked.connect(self.button_clicked)
        self.forgotpassword.clicked.connect(self.handle_OTP)
        self.login.clicked.connect(self.handle_login)

        self.login_disabled = False
        self.login_timer = QtCore.QTimer(self)
        self.login_timer.timeout.connect(self.unlock_login_button)

    def button_clicked(self):
        self.usernameinput.clear()
        self.passwordinput.clear()
        self.back_button.emit()

    # Forgot pass button
    def handle_OTP(self):
        self.usernameinput.clear()
        self.passwordinput.clear()
        self.forgot_button.emit()

    # Function to fetch login data from employees table
    def fetch_employee_login_data(self):
        if self.conn is None:
            return []
        try:
            cursor = self.conn.cursor()
            query = "SELECT Username, Password, LOA FROM employees"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error: {e}")
            return []

    # Function to fetch login data from clients table
    def fetch_client_login_data(self):
        if self.conn is None:
            return []
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM clients"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error: {e}")
            return []

    # Function to handle login
    def handle_login(self):
        if self.login_disabled:
            self.show_login_locked_message()
            print("Login temporarily locked. Please try again later.")
            return False

        username = self.usernameinput.text()
        password = self.passwordinput.text()

        # Hash the entered password using SHA-256
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # Fetch login data from employees table
        employee_login_data = self.fetch_employee_login_data()
        for db_username, db_password, db_loa in employee_login_data:
            if username == db_username and hashed_password == db_password:
                self.usernameinput.clear()
                self.passwordinput.clear()
                if db_loa == 'Admin':
                    self.loginadmin_button.emit()
                    print("Log in successful as Admin")
                elif db_loa == 'Coach':
                    self.logincoach_button.emit()
                    print("Log in successful as Coach")
                elif db_loa == 'Auditor':
                    self.loginauditor_button.emit()
                    print("Log in successful as Auditor")
                return True

        # Fetch login data from clients table
        client_login_data = self.fetch_client_login_data()
        for client_data in client_login_data:
            db_username = client_data[7]
            db_password = client_data[8]
            if username == db_username and hashed_password == db_password:
                self.usernameinput.clear()
                self.passwordinput.clear()
                self.loginclient_button.emit({
                    'Last_Name': client_data[1],
                    'First_Name': client_data[2],
                    'Address': client_data[3],
                    'Birthdate': client_data[4],
                    'Contact_Number': client_data[5],
                    'Email': client_data[6],
                    'Username': client_data[7],
                    'Password': client_data[8],
                    'Program_Plan': client_data[9],
                    'Conditions': client_data[10]
                })
                print("Log in successful as Client")
                return True

        # Login failed, increment failed attempt count and set lockout if necessary
        if username in self.failed_attempts:
            self.failed_attempts[username] += 1
        else:
            self.failed_attempts[username] = 1

        # If 5 or more failed attempts, lock the login button for 1 minute
        if self.failed_attempts[username] >= 5:
            self.login_disabled = True
            self.login_timer.start(60000)  # 60000 milliseconds = 1 minute
            self.show_login_locked_message()
            print("Login failed. Too many attempts. Login temporarily locked.")

        print("Login failed")
        return False

    def unlock_login_button(self):
        self.login_disabled = False
        self.login_timer.stop()
        self.hide_login_locked_message()
        print("Login unlocked")

    def show_login_locked_message(self):
        self.login.setEnabled(False)
        msg = QMessageBox()
        msg.setWindowTitle("Login Locked")
        msg.setText("Too many failed attempts. Please try again in 1 minute.")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def hide_login_locked_message(self):
        self.login.setEnabled(True)

    def closeEvent(self, event):
        self.login_timer.stop()
        super().closeEvent(event)