from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from screens.userdetailsUI import Ui_MainWindow
from mysql.connector import Error

class ClientDetailsWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    save_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(ClientDetailsWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn

        self.back.clicked.connect(self.button_clicked)
        self.save.clicked.connect(self.handle_save)

        self.disable_field(self.lname)
        self.disable_field(self.fname)
        self.dateEdit.setReadOnly(True)
        self.dateEdit.setEnabled(False)
        self.dateEdit.setStyleSheet("background-color: #f0f0f0; color: #808080; border: 1px solid #c0c0c0;")
        self.disable_field(self.username)
        self.disable_field(self.password)

    def button_clicked(self):
        self.back_button.emit()

    def set_clientdetails(self, client_details):
        self.client_details = client_details
        self.lname.setText(client_details.get('Last_Name', ''))
        self.fname.setText(client_details.get('First_Name', ''))
        self.address.setText(client_details.get('Address', ''))

        # Handling Birthdate
        birthdate = client_details.get('Birthdate')
        if birthdate:
            self.dateEdit.setDate(QDate(birthdate.year, birthdate.month, birthdate.day))

        self.contact_number.setText(client_details.get('Contact_Number', ''))
        self.emailaddress.setText(client_details.get('Email', ''))
        self.username.setText(client_details.get('Username', ''))
        self.password.setText(client_details.get('Password', ''))
        self.programplan.setCurrentText(client_details.get('Program_Plan', ''))
        self.medical_conditions.setText(client_details.get('Conditions', ''))

    def disable_field(self, field):
        field.setReadOnly(True)
        field.setEnabled(False)
        field.setStyleSheet("background-color: #f0f0f0; color: #808080; border: 1px solid #c0c0c0;")

    def handle_save(self):
        client_details = {
            'Last_Name': self.lname.text(),
            'First_Name': self.fname.text(),
            'Address': self.address.text(),
            'Birthdate': self.dateEdit.date().toString('yyyy-MM-dd'),
            'Contact_Number': self.contact_number.text(),
            'Email': self.emailaddress.text(),
            'Username': self.username.text(),
            'Password': self.password.text(),
            'Program_Plan': self.programplan.currentText(),
            'Conditions': self.medical_conditions.text()
        }

        try:
            cursor = self.conn.cursor()
            sql = """UPDATE clients 
                     SET Last_Name = %s, First_Name = %s, Address = %s, Birthdate = %s, 
                         Contact_Number = %s, Email = %s, Password = %s, Program_Plan = %s, 
                         Conditions = %s
                     WHERE Username = %s"""
            data = (client_details['Last_Name'], client_details['First_Name'], client_details['Address'],
                    client_details['Birthdate'], client_details['Contact_Number'], client_details['Email'],
                    client_details['Password'], client_details['Program_Plan'], client_details['Conditions'],
                    client_details['Username'])

            cursor.execute(sql, data)
            self.conn.commit()
            cursor.close()
            QMessageBox.information(self, 'Success', 'Client details updated successfully.')
            self.save_button.emit()

        except Error as e:
            QMessageBox.critical(self, 'Error', f"Error updating client details: {e}")