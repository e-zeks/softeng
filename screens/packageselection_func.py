from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QSpacerItem, QMessageBox
from PyQt5 import QtGui, QtWidgets, QtCore
from screens.packageselectionUI import Ui_MainWindow
import mysql.connector

class PackageSelectionWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    book_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(PackageSelectionWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn
        self.packagedetails = ""

        self.back.clicked.connect(self.button_clicked)

        # Fetch packages from the database
        self.packages = self.fetch_packages_from_database()

    def button_clicked(self):
        self.back_button.emit()

    def fetch_packages_from_database(self):
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT Package_Name, Package_Price, Package_Details, `Minimum_Sessions` FROM packages")
            packages = cursor.fetchall()
            return packages
        except mysql.connector.Error as e:
            print(f"Error retrieving packages: {e}")
            QMessageBox.critical(self, "Database Error", f"Error retrieving packages: {e}")
            return []

    def add_initial_packages_widgets(self):
        # Clear existing widgets first
        self.clear_package_widgets()

        for package in self.packages:
            package_name = package["Package_Name"]
            package_price = package["Package_Price"]
            package_details = package["Package_Details"]
            min_sessions = package["Minimum_Sessions"]
            self.add_package_widget(package_name, package_price, package_details, min_sessions)

    def clear_package_widgets(self):
        # Remove all existing widgets in the layout
        while self.horizontalLayout_6.count():
            item = self.horizontalLayout_6.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def add_package_widget(self, package_name, package_price, package_details, min_sessions):
        new_widget = QtWidgets.QWidget()
        new_widget.setStyleSheet("QWidget\n"
                                 "{\n"
                                 "background-color: #5e3b96;\n"
                                 "border-radius:20px;\n"
                                 "}")
        new_layout = QtWidgets.QVBoxLayout(new_widget)

        # Package Name
        package_name_label = QtWidgets.QLabel(package_name)
        package_name_label.setFont(QtGui.QFont("Arial Black", 20, weight=QtGui.QFont.Bold))  # Larger font size
        package_name_label.setStyleSheet("QLabel { color: #c8a2c8; }")
        new_layout.addWidget(package_name_label)

        # Package Price
        package_price_label = QtWidgets.QLabel(f"Price: {package_price}")
        package_price_label.setFont(QtGui.QFont("Arial Black", 14))
        package_price_label.setStyleSheet("QLabel { color: #e6e6fa; }")
        new_layout.addWidget(package_price_label)

        # Package Details
        package_details_label = QtWidgets.QLabel(package_details)
        package_details_label.setFont(QtGui.QFont("Arial Black", 12))
        package_details_label.setStyleSheet("QLabel { color: #e6e6fa; }")
        new_layout.addWidget(package_details_label)

        # Minimum Sessions
        min_sessions_label = QtWidgets.QLabel(f"Minimum Sessions: {min_sessions}")
        min_sessions_label.setFont(QtGui.QFont("Arial Black", 12))
        min_sessions_label.setStyleSheet("QLabel { color: #e6e6fa; }")
        new_layout.addWidget(min_sessions_label)

        # Add spacer between details and book button
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Fixed)
        new_layout.addItem(spacerItem2)

        # Book button
        book = QtWidgets.QPushButton("Book Now")
        book.setFont(QtGui.QFont("Arial Black", 12))
        book.setStyleSheet("QPushButton { color: #5e3b96; background-color: white; border-radius: 20px; }")
        book.setMinimumSize(100, 40)
        book.setFocusPolicy(QtCore.Qt.StrongFocus)  # Ensure the button can receive focus
        new_layout.addWidget(book)

        book.clicked.connect(lambda: self.handle_book(package_name, package_price, min_sessions))

        self.horizontalLayout_6.addWidget(new_widget)

    def handle_book(self, package_name, package_price, min_sessions):
        self.packagedetails = {
            'package_name': package_name,
            'package_price': package_price,
            'min_sessions': int(min_sessions)
        }
        self.book_button.emit()