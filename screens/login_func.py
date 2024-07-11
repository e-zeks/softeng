from mysql.connector import Error
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from screens.loginUI import Ui_MainWindow
import hashlib

class LoginWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    forgot_button = QtCore.pyqtSignal()
    loginadmin_button = QtCore.pyqtSignal()
    logincoach_button = QtCore.pyqtSignal(dict)
    loginauditor_button = QtCore.pyqtSignal()
    loginclient_button = QtCore.pyqtSignal(dict)

    def __init__(self, conn):
        super(LoginWindow, self).__init__()
        self.conn = conn
        self.current_user = None
        self.setupUi(self)

        self.passwordinput.setEchoMode(QLineEdit.Password)  # Set the password input to be hidden

        self.failed_attempts = {}  # Dictionary to store failed attempts
        self.login_disabled = False
        self.login_timer = QtCore.QTimer(self)
        self.login_timer.timeout.connect(self.unlock_login_button)

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

    # Function to fetch login data from employees table
    def fetch_employee_login_data(self):
        if self.conn is None:
            return []
        try:
            cursor = self.conn.cursor()
            query = "SELECT EmployeeID, Username, Password, LOA, First_Name, Last_Name FROM employees"
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
            query = "SELECT ClientID, Last_Name, First_Name, Address, Birthdate, Contact_Number, Email, Username, Password, Program_Plan, Conditions FROM clients"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error: {e}")
            return []

    def log_user_activity(self, user_id, user_type, first_name, last_name, action):
        try:
            cursor = self.conn.cursor()
            emp_id = user_id if user_type == 'Employee' else None
            client_id = user_id if user_type == 'Client' else None

            if action == "login":
                query = """
                INSERT INTO user_logs (EmployeeID, ClientID, UserType, First_Name, Last_Name, Login_Time)
                VALUES (%s, %s, %s, %s, %s, NOW())
                """
                cursor.execute(query, (emp_id, client_id, user_type, first_name, last_name))
            elif action == "logout":
                query = """
                UPDATE user_logs
                SET Logout_Time = NOW()
                WHERE (EmployeeID = %s OR ClientID = %s) AND UserType = %s AND Logout_Time IS NULL
                """
                cursor.execute(query, (emp_id, client_id, user_type))
            self.conn.commit()
        except Error as e:
            print(f"Error logging user activity: {e}")
            print(
                f"user_id: {user_id}, user_type: {user_type}, first_name: {first_name}, last_name: {last_name}, action: {action}")

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
        for db_employee_id, db_username, db_password, db_loa, db_first_name, db_last_name in employee_login_data:
            if username == db_username and hashed_password == db_password:
                print("Log in successful")
                self.log_user_activity(db_employee_id, 'Employee', db_first_name, db_last_name, 'login')
                self.current_user = {
                    'UserID': db_employee_id,
                    'UserType': 'Employee',
                    'First_Name': db_first_name,
                    'Last_Name': db_last_name
                }
                self.usernameinput.clear()
                self.passwordinput.clear()
                if db_loa == 'Admin':
                    self.loginadmin_button.emit()
                    print("Admin Screen")
                elif db_loa == 'Coach':
                    self.logincoach_button.emit(self.current_user)
                    print("Coach Screen")
                elif db_loa == 'Auditor':
                    self.loginauditor_button.emit()
                    print("Auditor Screen")
                return True

        # Fetch login data from clients table
        client_login_data = self.fetch_client_login_data()
        for client_data in client_login_data:
            db_client_id = client_data[0]
            db_last_name = client_data[1]
            db_first_name = client_data[2]
            db_address = client_data[3]
            db_birthdate = client_data[4]
            db_contact_number = client_data[5]
            db_email = client_data[6]
            db_username = client_data[7]
            db_password = client_data[8]
            db_program_plan = client_data[9]
            db_conditions = client_data[10]

            if username == db_username and hashed_password == db_password:
                print("Log in successful")
                self.log_user_activity(db_client_id, 'Client', db_first_name, db_last_name, 'login')
                self.current_user = {
                    'UserID': db_client_id,
                    'UserType': 'Client',
                    'First_Name': db_first_name,
                    'Last_Name': db_last_name
                }
                self.usernameinput.clear()
                self.passwordinput.clear()
                self.loginclient_button.emit({
                    'Last_Name': db_last_name,
                    'First_Name': db_first_name,
                    'Address': db_address,
                    'Birthdate': db_birthdate,
                    'Contact_Number': db_contact_number,
                    'Email': db_email,
                    'Username': db_username,
                    'Password': db_password,
                    'Program_Plan': db_program_plan,
                    'Conditions': db_conditions
                })
                print("Client Screen")
                return True

        # Login failed, increment failed attempt count and set lockout if necessary
        if username in self.failed_attempts:
            self.failed_attempts[username] += 1
        else:
            self.failed_attempts[username] = 1

        # If 5 or more failed attempts, lock the login button for 1 minute
        if self.failed_attempts[username] >= 3:
            self.login_disabled = True
            self.login_timer.start(60000)  # 60000 milliseconds = 1 minute
            self.show_login_locked_message()
            print("Login failed. Too many attempts. Login temporarily locked.")
        else:
            self.show_incorrect_password_message()

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

    def show_incorrect_password_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("Login Failed")
        msg.setText("Incorrect username or password. Please try again.")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def handle_logout(self):
        if self.current_user:
            self.log_user_activity(self.current_user['UserID'], self.current_user['UserType'], self.current_user['First_Name'], self.current_user['Last_Name'], 'logout')
            self.current_user = None
            print("Logout successful")