from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from screens.editpackageUI import Ui_MainWindow
import mysql.connector

class EditPackageWindow(QMainWindow, Ui_MainWindow):
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
        super(EditPackageWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn  # Store the database connection

        self.cancel.clicked.connect(self.handle_cancel)
        self.save.clicked.connect(self.handle_save)

        # Populate comboBox with Package_ID values
        self.populate_comboBox()

        # Connect signals to slots
        self.comboBox.currentIndexChanged.connect(self.load_package_details)

        # Make packagename non-editable
        self.packagename.setReadOnly(True)

        #nav bar button
        self.employees.clicked.connect(self.handle_employees)
        self.clients.clicked.connect(self.handle_clients)
        self.payments.clicked.connect(self.handle_payments)
        self.report.clicked.connect(self.handle_reports)
        self.userlogs.clicked.connect(self.handle_userlogs)
        self.maintenance.clicked.connect(self.handle_maintenance)
        self.help.clicked.connect(self.handle_help)
        self.logout.clicked.connect(self.button_clicked)

    def populate_comboBox(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT Package_ID FROM packages")
            package_ids = cursor.fetchall()
            cursor.close()

            self.comboBox.clear()
            self.comboBox.addItem("")  # Add a blank choice as the first item
            for package_id in package_ids:
                self.comboBox.addItem(str(package_id[0]))

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error loading package IDs: {err}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Unexpected error: {e}")

    def load_package_details(self):
        try:
            package_id = self.comboBox.currentText()
            if package_id:
                cursor = self.conn.cursor()
                cursor.execute("SELECT Package_Name, Package_Price, Package_Details, Minimum_Sessions FROM packages WHERE Package_ID = %s", (package_id,))
                package = cursor.fetchone()
                cursor.close()

                if package:
                    self.packagename.setText(package[0])
                    self.packageprice.setText(str(package[1]))
                    self.packagedetails.setPlainText(package[2])
                    self.minimumsessions.setText(str(package[3]))  # Update minimumsessions field
                else:
                    self.packagename.clear()
                    self.packageprice.clear()
                    self.packagedetails.clear()
                    self.minimumsessions.clear()
            else:
                self.packagename.clear()
                self.packageprice.clear()
                self.packagedetails.clear()
                self.minimumsessions.clear()

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error loading package details: {err}")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Unexpected error: {e}")

    def refresh_data(self):
        self.populate_comboBox()
        self.load_package_details()

    def handle_cancel(self):
        self.cancel_button.emit()

    def handle_save(self):
        try:
            package_id = self.comboBox.currentText()
            package_price = self.packageprice.text()
            package_details = self.packagedetails.toPlainText()
            minimum_sessions = self.minimumsessions.text()  # Get the value from minimumsessions field

            if not package_id or not package_price or not package_details or not minimum_sessions:
                QtWidgets.QMessageBox.warning(self, "Warning", "Please fill in all fields.")
                return

            cursor = self.conn.cursor()

            # Update data in 'packages' table
            update_query = "UPDATE packages SET Package_Price = %s, Package_Details = %s, Minimum_Sessions = %s WHERE Package_ID = %s"
            cursor.execute(update_query, (package_price, package_details, minimum_sessions, package_id))
            self.conn.commit()

            cursor.close()
            QtWidgets.QMessageBox.information(self, "Success", "Data updated successfully.")
            self.save_button.emit()
            self.refresh_data()  # Refresh data after saving

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error updating data: {err}")
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
