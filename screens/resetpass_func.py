from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from screens.resetpassUI import Ui_MainWindow
import re
import mysql.connector  # Import mysql.connector for database interaction

class ResetPassWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    reset_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(ResetPassWindow, self).__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.button_clicked)
        self.resetnow.clicked.connect(self.handle_resetnow)
        self.conn = conn  # Store the database connection
        self.email = None

    def button_clicked(self):
        self.back_button.emit()

    def set_email(self, email):
        self.email = email

    def handle_resetnow(self):
        newpassword = self.password.text()
        newpassword2 = self.retypepassword.text()

        if self.validate_password(newpassword):
            if newpassword == newpassword2:
                if self.update_password_in_db(newpassword):  # Update password in the database
                    QMessageBox.information(self, "Success", "Password reset successfully!")
                    self.reset_button.emit()
                else:
                    QMessageBox.critical(self, "Database Error", "Failed to update the password in the database.")
            else:
                QMessageBox.warning(self, "Mismatch", "Passwords do not match. Please try again.")
        else:
            QMessageBox.warning(self, "Invalid Password", "Password must: \n- Have at least 8 characters\n- Contain at least one uppercase letter\n- Contain at least one lowercase letter\n- Contain at least one digit\n- Not contain any special characters")

    def validate_password(self, password):
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

    def update_password_in_db(self, newpassword):
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE employees SET password = %s WHERE email = %s", (newpassword, self.email))
            self.conn.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return False
