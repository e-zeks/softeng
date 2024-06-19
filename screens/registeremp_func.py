import re
from mysql.connector import Error
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.registerempUI import Ui_MainWindow

class RegisterWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    #register_2 = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(RegisterWindow, self).__init__()
        self.conn = conn
        self.setupUi(self)

        # Button connections
        self.back.clicked.connect(self.button_clicked)
        self.register_2.clicked.connect(self.handle_register)

    def button_clicked(self):
        self.back_button.emit()

    def handle_register(self):
        lname = self.lname.text()
        fname = self.fname.text()
        email = self.emailadd.text()
        contactnum = self.contactno.text()
        username = self.username.text()
        password = self.password.text()
        confirm_password = self.confirmpassword.text()

        if not self.validate_password():
            print("Password does not meet requirements.")
            return

        if password != confirm_password:
            print("Passwords do not match.")
            return

        if self.is_username_taken():
            print("Username is already taken.")
            return

        try:
            cursor = self.conn.cursor()
            query = "INSERT INTO employees (Last_Name, First_Name, Email, Contact_Number, Username, Password) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (lname, fname, email, contactnum, username, password))
            self.conn.commit()
            print("Registration successful.")
            self.lname.clear()
            self.fname.clear()
            self.emailadd.clear()
            self.contactno.clear()
            self.username.clear()
            self.password.clear()
            self.confirmpassword.clear()
        except Error as e:
            self.conn.rollback()
            print(f"Error during registration: {e}")

    def is_username_taken(self):
        username = self.username.text()
        try:
            cursor = self.conn.cursor()
            query = "SELECT COUNT(*) FROM employees WHERE Username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            return result[0] > 0
        except Error as e:
            print(f"Error: {e}")
            return True

    def validate_password(self):
        password = self.password.text()
        if len(password) < 8:
            return False
        if not re.search("[A-Z]", password):
            return False
        if not re.search("[a-z]", password):
            return False
        if not re.search("[0-9]", password):
            return False
        if re.search("[^A-Za-z0-9]", password):
            return False
        return True