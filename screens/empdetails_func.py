from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from screens.empdetailsUI import Ui_MainWindow
import mysql.connector

class EmployeeDetailsWindow(QMainWindow, Ui_MainWindow):
    cancel_button = QtCore.pyqtSignal()
    save_button = QtCore.pyqtSignal()

    def __init__(self, emp_details, conn):
        super(EmployeeDetailsWindow, self).__init__()
        self.setupUi(self)
        self.emp_details = emp_details
        self.conn = conn

        # Populate UI with initial employee details
        self.set_empdetails(emp_details)

        # Connect buttons to functions
        self.back.clicked.connect(self.button_clicked)
        self.save.clicked.connect(self.handle_save)

    def button_clicked(self):
        self.cancel_button.emit()

    def handle_save(self):
        emp_id = self.emp_details.get('EmployeeID')  # Ensure emp_id is fetched correctly
        last_name = self.lname.text()
        first_name = self.fname.text()
        username = self.username.text()
        loa = self.loa.currentText()
        contact_number = self.contactno.text()
        email = self.emailadd.text()

        try:
            cursor = self.conn.cursor()
            sql = """UPDATE employees 
                     SET Last_Name = %s, First_Name = %s, Username = %s, LOA = %s, Contact_Number = %s, Email = %s
                     WHERE EmployeeID = %s"""
            data = (last_name, first_name, username, loa, contact_number, email, emp_id)
            cursor.execute(sql, data)
            self.conn.commit()
            cursor.close()
            QtWidgets.QMessageBox.information(self, 'Success', 'Employee details updated successfully.')
            self.save_button.emit()

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(self, 'Error', f"Error updating employee details: {err}")
            print(f"Error: {err}")  # Debug print statement

    def set_empdetails(self, emp_details):
        self.lname.setText(emp_details.get('Last_Name', ''))
        self.fname.setText(emp_details.get('First_Name', ''))
        self.username.setText(emp_details.get('Username', ''))
        self.loa.setCurrentText(emp_details.get('LOA', ''))
        self.contactno.setText(emp_details.get('Contact_Number', ''))
        self.emailadd.setText(emp_details.get('Email', ''))
