import re
import hashlib
import mysql.connector  # MySQL connector
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from screens.bookingUI import Ui_MainWindow

class ClientRegWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    register_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(ClientRegWindow, self).__init__()
        self.conn = conn
        self.setupUi(self)

        # Connect the buttons to their respective handlers
        self.back.clicked.connect(self.button_clicked)
        self.register_2.clicked.connect(self.handle_register)

    def button_clicked(self):
        # Emit the back_button signal when the back button is clicked
        self.back_button.emit()

    def is_username_taken(self):
        username = self.username.text().strip()
        try:
            cursor = self.conn.cursor()
            query = "SELECT COUNT(*) FROM clients WHERE Username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            return result[0] > 0
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
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

    def is_email_registered(self, email):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM clients WHERE Email = %s", (email,))
            result = cursor.fetchone()
            return result[0] > 0
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return True

    def handle_register(self):
        # Get the input values from the form fields and strip any leading/trailing whitespace
        last_name = self.lname.text().strip()
        first_name = self.fname.text().strip()
        address = self.address.text().strip()
        birthday = self.dateEdit.date().toString('yyyy-MM-dd')
        contact_number = self.contact_number.text().strip()
        email = self.emailaddress.text().strip()
        username = self.username.text().strip()
        password = self.password.text().strip()
        program_plan = self.programplan.currentText().strip()  # Assuming programPlan is a QComboBox
        conditions = self.medical_conditions.text().strip()  # Assuming conditions is a QTextEdit

        # Validate the email format using a regular expression
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            QMessageBox.warning(self, "Input Error", "Invalid email format.")
            return

        # Check if the username is already taken
        if self.is_username_taken():
            QMessageBox.warning(self, "Input Error", "Username is already taken.")
            return

        # Validate the password
        if not self.validate_password():
            QMessageBox.warning(self, "Input Error", "Password must: \n- Have at least 8 characters\n- Contain at least one uppercase letter\n- Contain at least one lowercase letter\n- Contain at least one digit\n- Not contain any special characters")
            return

        # Check if the email is already registered
        if self.is_email_registered(email):
            QMessageBox.warning(self, "Input Error", "Email is already registered.")
            return

        # Hash the password using SHA-256
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        try:
            cursor = self.conn.cursor()
            # Execute the SQL INSERT statement to add the client to the database
            cursor.execute(
                """
                INSERT INTO clients (Last_Name, First_Name, Address, Birthdate, Contact_Number, Email, Username, Password, Program_Plan, Conditions)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (last_name, first_name, address, birthday, contact_number, email, username, hashed_password, program_plan,
                 conditions)
            )
            self.conn.commit()  # Commit the transaction
            QMessageBox.information(self, "Success", "Client registered successfully.")
            self.register_button.emit()  # Emit the register_button signal
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
            self.conn.rollback()  # Rollback the transaction on error
