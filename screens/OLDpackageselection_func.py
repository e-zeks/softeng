from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from screens.OLDpackageselectionUI import Ui_MainWindow
import mysql.connector

class PackageSelectionWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    select_button1 = QtCore.pyqtSignal(str)
    select_button2 = QtCore.pyqtSignal(str)
    select_button3 = QtCore.pyqtSignal(str)

    def __init__(self, conn):
        super(PackageSelectionWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn  # Store the database connection
        self.current_package_index = 0  # Track current package index

        self.back.clicked.connect(self.button_clicked)
        self.selectpackage1.clicked.connect(self.select_button1_clicked)
        self.selectpackage2.clicked.connect(self.select_button2_clicked)
        self.selectpackage3.clicked.connect(self.select_button3_clicked)

        self.package1_name = None
        self.package2_name = None
        self.package3_name = None

    def display_package_data(self):
        try:
            cursor = self.conn.cursor()

            # Fetch all packages from the database
            cursor.execute("SELECT Package_Name, Package_Price, Package_Details FROM packages")
            packages = cursor.fetchall()

            if packages:
                if self.current_package_index < len(packages):
                    # Display the first set of labels
                    package_name, package_price, package_details = packages[self.current_package_index]
                    price_with_peso = f"₱ {package_price} per session."
                    self.package1.setText(package_name)
                    self.price1.setText(price_with_peso)
                    self.label_3.setText(package_details)
                    self.package1_name = package_name

                    # Display the second set of labels if available
                    next_index = self.current_package_index + 1
                    if next_index < len(packages):
                        package_name, package_price, package_details = packages[next_index]
                        price_with_peso = f"₱ {package_price} per session."  # Calculate for package2
                        self.package2.setText(package_name)
                        self.price2.setText(price_with_peso)
                        self.label_6.setText(package_details)
                        self.package2_name = package_name
                    else:
                        self.package2.setText("")
                        self.price2.setText("")
                        self.label_6.setText("")
                        self.package2_name = None

                    # Display the third set of labels if available
                    third_index = self.current_package_index + 2
                    if third_index < len(packages):
                        package_name, package_price, package_details = packages[third_index]
                        price_with_peso = f"₱ {package_price} per session."  # Calculate for package3
                        self.package3.setText(package_name)
                        self.price3.setText(price_with_peso)
                        self.label_9.setText(package_details)
                        self.package3_name = package_name
                    else:
                        self.package3.setText("")
                        self.price3.setText("")
                        self.label_9.setText("")
                        self.package3_name = None

                    self.current_package_index = next_index

                else:
                    QtWidgets.QMessageBox.warning(self, "Warning", "No more packages to display.")
            else:
                QtWidgets.QMessageBox.warning(self, "Warning", "No package data found.")

            cursor.close()

        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error fetching package data: {err}")

    def refresh_data(self):
        self.current_package_index = 0  # Reset the index
        self.display_package_data()

    def button_clicked(self):
        self.back_button.emit()

    def select_button1_clicked(self):
        if self.package1_name:
            print(f"Selected Package 1 Name: {self.package1_name}")
            self.select_button1.emit(self.package1_name)

    def select_button2_clicked(self):
        if self.package2_name:
            print(f"Selected Package 2 Name: {self.package2_name}")
            self.select_button2.emit(self.package2_name)

    def select_button3_clicked(self):
        if self.package3_name:
            print(f"Selected Package 3 Name: {self.package3_name}")
            self.select_button3.emit(self.package3_name)
