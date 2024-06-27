from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from screens.addcoachUI import Ui_MainWindow
from mysql.connector import Error

class AddCoachWindow(QMainWindow, Ui_MainWindow):
    #screen buttons
    cancel_button = QtCore.pyqtSignal()
    save_button = QtCore.pyqtSignal()

    #nav bar buttons
    employeemanage_button = QtCore.pyqtSignal()
    clientmanage_button = QtCore.pyqtSignal()
    payments_button = QtCore.pyqtSignal()
    reports_button = QtCore.pyqtSignal()
    userlogs_button = QtCore.pyqtSignal()
    maintenance_button = QtCore.pyqtSignal()
    help_button = QtCore.pyqtSignal()
    logout_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(AddCoachWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn

        # Retrieve data from the database and populate the combobox
        self.populate_combobox()

        #screen buttons
        self.cancel.clicked.connect(self.handle_cancel)
        self.save.clicked.connect(self.handle_save)

        #nav bar button
        self.employees.clicked.connect(self.handle_employees)
        self.clients.clicked.connect(self.handle_clients)
        self.payments.clicked.connect(self.handle_payments)
        self.report.clicked.connect(self.handle_reports)
        self.userlogs.clicked.connect(self.handle_userlogs)
        self.maintenance.clicked.connect(self.handle_maintenance)
        self.help.clicked.connect(self.handle_help)
        self.logout.clicked.connect(self.button_clicked)

    def handle_cancel(self):
        self.cancel_button.emit()

    def disable_field(self, field):
        field.setReadOnly(True)
        field.setEnabled(False)
        field.setStyleSheet("background-color: #f0f0f0; color: #808080; border: 1px solid #c0c0c0;")

    def refresh_fields(self):
        self.comboBox.clear()
        self.experience.clear()
        self.specialties.clear()
        self.fullname.clear()
        self.populate_combobox()

    def populate_combobox(self):
        try:
            cursor = self.conn.cursor()

            self.comboBox.addItem("")

            # Query to get the names of coaches already added
            cursor.execute("SELECT Last_Name, First_Name FROM coaches")
            added_coaches = cursor.fetchall()
            added_coach_names = {f"{last_name}, {first_name}" for last_name, first_name in added_coaches}

            # Query to get the names of all coaches from employees table
            cursor.execute("SELECT Last_Name, First_Name FROM employees WHERE LOA = 'Coach'")
            results = cursor.fetchall()

            # Add names to comboBox only if they are not already added
            for row in results:
                last_name, first_name = row
                full_name = f"{last_name}, {first_name}"
                if full_name not in added_coach_names:
                    self.comboBox.addItem(full_name)

            cursor.close()
        except Error as e:
            QMessageBox.critical(self, 'Error', f"Error retrieving coach data: {e}")

    def handle_save(self):
        try:
            print("saving...")
            print(f"Current text in combobox: {self.comboBox.currentText()}")
            print(f"Experiences: {self.experience.toPlainText()}")
            print(f"Specialties: {self.specialties.toPlainText()}")
            print(f"Coach Name: {self.fullname.text()}")

            last_name = self.comboBox.currentText().split(", ")[0]
            first_name = self.comboBox.currentText().split(", ")[1]
            experience = self.experience.toPlainText()  # Use toPlainText() instead of text
            specialties = self.specialties.toPlainText()  # Use toPlainText() instead of text
            coach_name = self.fullname.text()
            print("saving 2")

            cursor = self.conn.cursor()
            sql = """INSERT INTO coaches (Last_Name, First_Name, Experiences, Specialties, Coach_Name)
                     VALUES (%s, %s, %s, %s, %s)
                     ON DUPLICATE KEY UPDATE Experiences=%s, Specialties=%s, Coach_Name=%s"""
            data = (last_name, first_name, experience, specialties, coach_name, experience, specialties, coach_name)

            cursor.execute(sql, data)
            self.conn.commit()

            # Check if any rows were affected
            print(f"Rows affected: {cursor.rowcount}")

            cursor.close()
            QMessageBox.information(self, 'Success', 'Coach details updated successfully.')
            self.comboBox.clear()
            self.experience.clear()
            self.specialties.clear()
            self.fullname.clear()
            self.save_button.emit()

            # Remove the added coach from the combobox
            self.comboBox.removeItem(self.comboBox.currentIndex())

        except Error as e:
            QMessageBox.critical(self, 'Error', f"Error updating coach details: {e}")
            print(f"SQL Error: {e}")

        except Exception as ex:
            QMessageBox.critical(self, 'Error', f"Unexpected error: {ex}")
            print(f"Unexpected error: {ex}")

    #nav bar buttons
    def handle_employees(self):
        self.employeemanage_button.emit()

    def handle_clients(self):
        self.clientmanage_button.emit()

    def handle_payments(self):
        self.payments_button.emit()

    def handle_reports(self):
        self.reports_button.emit()

    def handle_userlogs(self):
        self.userlogs_button.emit()

    def handle_maintenance(self):
        self.maintenance_button.emit()

    def handle_help(self):
        self.help_button.emit()

    def button_clicked(self):
        print("Logging Out")
        self.logout_button.emit()