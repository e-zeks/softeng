from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QSpacerItem, QMessageBox
from PyQt5 import QtGui, QtWidgets, QtCore
from screens.coachselectionUI import Ui_MainWindow
import mysql.connector

class CoachSelectionWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    book_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(CoachSelectionWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn
        self.coachdetails = ""

        self.back.clicked.connect(self.button_clicked)
        self.help.clicked.connect(self.handle_help)
        # Fetch coaches from the database
        self.coaches = self.fetch_coaches_from_database()

    def button_clicked(self):
        self.back_button.emit()

    def handle_help(self):
        pdf_path = "C:\\Users\\JC\\Desktop\\softeng-main\\Anytime Fitness User Manual.pdf"
        QDesktopServices.openUrl(QUrl.fromLocalFile(pdf_path))

    def fetch_coaches_from_database(self):
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT Coach_Name, Last_Name, First_Name, Experiences, Specialties FROM coaches")
            coaches = cursor.fetchall()
            return coaches
        except mysql.connector.Error as e:
            print(f"Error retrieving coaches: {e}")
            QMessageBox.critical(self, "Database Error", f"Error retrieving coaches: {e}")
            return []

    def add_initial_coach_widgets(self):
        # Clear existing widgets first
        self.clear_coach_widgets()

        for coach in self.coaches:
            coach_name = coach["Coach_Name"]
            full_name = f"{coach['First_Name']} {coach['Last_Name']}"
            experiences = coach["Experiences"]
            specialties = coach["Specialties"]
            self.add_coach_widget(coach_name, full_name, experiences, specialties)

    def clear_coach_widgets(self):
        # Remove all existing widgets in the layout
        while self.horizontalLayout_6.count():
            item = self.horizontalLayout_6.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def add_coach_widget(self, coach_name, full_name, experiences, specialties):
        new_widget = QtWidgets.QWidget()
        new_widget.setStyleSheet("QWidget\n"
                                 "{\n"
                                 "background-color: #5e3b96;\n"
                                 "border-radius:20px;\n"
                                 "}")
        new_layout = QtWidgets.QVBoxLayout(new_widget)

        coachname = QtWidgets.QLabel(coach_name)
        coachname.setFont(QtGui.QFont("Arial Black", 20, weight=QtGui.QFont.Bold))  # Larger font size
        coachname.setStyleSheet("QLabel { color: white; }")
        new_layout.addWidget(coachname)

        fullname = QtWidgets.QLabel(full_name)
        fullname.setFont(QtGui.QFont("Arial Black", 12))
        fullname.setStyleSheet("QLabel { color: white; }")
        new_layout.addWidget(fullname)

        # Add spacer between Name and Experiences
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        new_layout.addItem(spacerItem)

        label3 = QtWidgets.QLabel("Experiences")
        label3.setFont(QtGui.QFont("Arial Black", 14))
        label3.setStyleSheet("QLabel { color: white; }")
        new_layout.addWidget(label3)

        experiences_label = QtWidgets.QLabel(experiences)
        experiences_label.setFont(QtGui.QFont("Arial Black", 12))
        experiences_label.setStyleSheet("QLabel { color: white; }")
        new_layout.addWidget(experiences_label)

        label5 = QtWidgets.QLabel("Specialties")
        label5.setFont(QtGui.QFont("Arial Black", 14))
        label5.setStyleSheet("QLabel { color: white; }")
        new_layout.addWidget(label5)

        specialties_label = QtWidgets.QLabel(specialties)
        specialties_label.setFont(QtGui.QFont("Arial Black", 12))
        specialties_label.setStyleSheet("QLabel { color: white; }")
        new_layout.addWidget(specialties_label)

        # Add spacer between Specialties and Book button
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Fixed)
        new_layout.addItem(spacerItem2)

        book = QtWidgets.QPushButton("Book Now")
        book.setFont(QtGui.QFont("Arial Black", 12))
        book.setStyleSheet("QPushButton { color: #5e3b96; background-color: white; border-radius: 20px; }")
        book.setMinimumSize(100, 40)
        book.setFocusPolicy(QtCore.Qt.StrongFocus)  # Ensure the button can receive focus
        new_layout.addWidget(book)

        book.clicked.connect(lambda: self.handle_book(full_name, coach_name))

        self.horizontalLayout_6.addWidget(new_widget)

    def handle_book(self, full_name, coach_name):
        self.coachdetails = {
            'full_name': full_name,
            'coach_name': coach_name
        }
        self.book_button.emit()