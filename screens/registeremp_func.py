import re
import hashlib
from mysql.connector import Error
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from screens.registerempUI import Ui_MainWindow

class RegisterWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    # register_2 = QtCore.pyqtSignal()

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
        lname = self.lname.text().strip()
        fname = self.fname.text().strip()
        email = self.emailadd.text().strip()
        contactnum = self.contactno.text().strip()
        username = self.username.text().strip()
        password = self.password.text().strip()
        confirm_password = self.confirmpassword.text().strip()

        if not self.validate_password():
            QMessageBox.warning(self, "Input Error", "Password must: \n- Have at least 8 characters\n- Contain at least one uppercase letter\n- Contain at least one lowercase letter\n- Contain at least one digit\n- Not contain any special characters")
            print("Password does not meet requirements.")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Input Error", "Passwords do not match.")
            print("Passwords do not match.")
            return

        if self.is_username_taken():
            QMessageBox.warning(self, "Input Error", "Username is already taken.")
            print("Username is already taken.")
            return

        # Hash the password using SHA-256
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        try:
            cursor = self.conn.cursor()
            query = "INSERT INTO employees (Last_Name, First_Name, Email, Contact_Number, Username, Password) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (lname, fname, email, contactnum, username, hashed_password))
            self.conn.commit()
            QMessageBox.information(self, "Success", "Registration successful.")
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
            QMessageBox.critical(self, "Database Error", f"Error during registration: {e}")
            print(f"Error during registration: {e}")

    def is_username_taken(self):
        username = self.username.text().strip()
        try:
            cursor = self.conn.cursor()
            query = "SELECT COUNT(*) FROM employees WHERE Username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            return result[0] > 0
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
            print(f"Error: {e}")
            return True

    def validate_password(self):
        password = self.password.text().strip()
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
