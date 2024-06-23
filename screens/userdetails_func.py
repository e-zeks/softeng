from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from screens.userdetailsUI import Ui_MainWindow

class ClientDetailsWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()

    def __init__(self):
        super(ClientDetailsWindow, self).__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.button_clicked)

        self.setDisabled(self.lname)
        self.setDisabled(self.fname)
        self.dateEdit.setReadOnly(True)
        self.dateEdit.setEnabled(False)
        self.dateEdit.setStyleSheet("background-color: #f0f0f0; color: #808080; border: 1px solid #c0c0c0;")
        self.setDisabled(self.username)
        self.setDisabled(self.password)

    def button_clicked(self):
        self.back_button.emit()

    def set_clientdetails(self, client_details):
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