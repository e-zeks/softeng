from mysql.connector import Error
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.loginUI import Ui_MainWindow

class LoginWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    forgot_button = QtCore.pyqtSignal()
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.button_clicked)
        self.forgotpassword.clicked.connect(self.handle_OTP)

    def button_clicked(self):
        self.back_button.emit()

    def handle_OTP(self):
        self.forgot_button.emit()

# Function to fetch login data
def fetch_login_data(conn):
    if conn is None:
        return []
    try:
        with conn.cursor() as cursor:
            query = "SELECT Username, Password, LOA FROM employees"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
    except Error as e:
        print(f"Error: {e}")
        return []
#
# # Function to handle login
def handle_login(conn, username, password, main_window):
    login_data = fetch_login_data(conn)
    for db_username, db_password, db_loa in login_data:
        if username == db_username and password == db_password:
            print("Log in successful")
            if db_loa == 'Admin':
                print("Admin Screen")
            elif db_loa == 'Coach':
                print("coach screen")
            elif db_loa == 'Auditor':
                print("auditor screen")
            elif db_loa == 'Client':
                print("client screen")
            return True
    print("Login failed")
    return False
