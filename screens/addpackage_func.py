from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from screens.addpackageUI import Ui_MainWindow
import mysql.connector

class AddPackageWindow(QMainWindow, Ui_MainWindow):
    #screen buttons
    cancel_button = QtCore.pyqtSignal()
    save_button = QtCore.pyqtSignal()
    package_added = QtCore.pyqtSignal()

    employeemanage_button = QtCore.pyqtSignal()
    clientmanage_button = QtCore.pyqtSignal()
    payments_button = QtCore.pyqtSignal()
    reports_button = QtCore.pyqtSignal()
    userlogs_button = QtCore.pyqtSignal()
    maintenance_button = QtCore.pyqtSignal()
    help_button = QtCore.pyqtSignal()
    logout_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(AddPackageWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn  # Store the database connection

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

    def handle_save(self):
        try:
            package_name = self.packagename.text()
            package_price = self.packageprice.text()
            package_details = self.textEdit.toPlainText()
            minimum_sessions = self.minimumsessions.text()  # Get the value from minimumsessions field

            if not package_name or not package_price or not package_details or not minimum_sessions:
                QtWidgets.QMessageBox.warning(self, "Warning", "Please fill in all fields.")
                return

            cursor = self.conn.cursor()

            # Insert data into 'packages' table
            insert_query = "INSERT INTO packages (Package_Name, Package_Price, Package_Details, Minimum_Sessions) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (package_name, package_price, package_details, minimum_sessions))
            self.conn.commit()

            cursor.close()
            QtWidgets.QMessageBox.information(self, "Success", "Data saved successfully.")
            self.package_added.emit()
            self.close()
            self.save_button.emit()

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error saving data: {err}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Unexpected error: {e}")

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
