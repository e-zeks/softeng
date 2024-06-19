from mysql.connector import Error
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.loginUI import Ui_MainWindow

class LoginWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    forgot_button = QtCore.pyqtSignal()
    loginadmin_button = QtCore.pyqtSignal()
    logincoach_button = QtCore.pyqtSignal()
    loginauditor_button = QtCore.pyqtSignal()
    loginclient_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(LoginWindow, self).__init__()
        self.conn = conn
        self.setupUi(self)

        self.back.clicked.connect(self.button_clicked)
        self.forgotpassword.clicked.connect(self.handle_OTP)
        self.login.clicked.connect(self.handle_login)

    def button_clicked(self):
        self.usernameinput.clear()
        self.passwordinput.clear()
        self.back_button.emit()

    # Forgot pass button
    def handle_OTP(self):
        self.usernameinput.clear()
        self.passwordinput.clear()
        self.forgot_button.emit()

    # Function to fetch login data
    def fetch_login_data(self):
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

    # Function to handle login
    def handle_login(self):
        username = self.usernameinput.text()
        password = self.passwordinput.text()
        login_data = self.fetch_login_data()

        for db_username, db_password, db_loa in login_data:
            if username == db_username and password == db_password:
                print("Log in successful")
                if db_loa == 'Admin':
                    print("Admin Screen")
                    self.usernameinput.clear()
                    self.passwordinput.clear()
                    self.loginadmin_button.emit()
                elif db_loa == 'Coach':
                    self.usernameinput.clear()
                    self.passwordinput.clear()
                    self.logincoach_button.emit()
                    print("Coach Screen")
                elif db_loa == 'Auditor':
                    self.usernameinput.clear()
                    self.passwordinput.clear()
                    self.loginauditor_button.emit()
                    print("Auditor Screen")
                elif db_loa == 'Client':
                    self.usernameinput.clear()
                    self.passwordinput.clear()
                    self.loginclient_button.emit()
                    print("Client Screen")
                return True
        print("Login failed")
        return False