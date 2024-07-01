from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from screens.OLDcoachselectionUI import Ui_MainWindow
from mysql.connector import Error

class CoachSelectionWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    book_button1 = QtCore.pyqtSignal(str)
    book_button2 = QtCore.pyqtSignal(str)
    book_button3 = QtCore.pyqtSignal(str)

    def __init__(self, conn):
        super(CoachSelectionWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn

        self.back.clicked.connect(self.button_clicked)
        self.booknow1.clicked.connect(self.book_button1_clicked)
        self.booknow2.clicked.connect(self.book_button2_clicked)
        self.booknow3.clicked.connect(self.book_button3_clicked)

        self.coachname_1 = None
        self.coachname_2 = None
        self.coachname_3 = None

    def refresh_data(self):
        self.retrieve_coach_details()

    def button_clicked(self):
        self.back_button.emit()

    def book_button1_clicked(self):
        coach_name = self.get_coach_name(self.coachname)
        if coach_name:
            print(f"Booked Coach 1: {coach_name}")
            self.book_button1.emit(coach_name)

    def book_button2_clicked(self):
        coach_name = self.get_coach_name(self.coachname_2)
        if coach_name:
            print(f"Booked Coach 2: {coach_name}")
            self.book_button2.emit(coach_name)

    def book_button3_clicked(self):
        coach_name = self.get_coach_name(self.coachname_3)
        if coach_name:
            print(f"Booked Coach 3: {coach_name}")
            self.book_button3.emit(coach_name)

    def get_coach_name(self, label):
        if label:
            return label.text()
        return None

    def retrieve_coach_details(self):
        try:
            cursor = self.conn.cursor()
            query = "SELECT Coach_Name, First_Name, Last_Name, Experiences, Specialties FROM coaches LIMIT 1"
            cursor.execute(query)
            result = cursor.fetchone()

            if result:
                coach_name, first_name, last_name, experience, specialties = result
                self.coachname.setText(f"Coach {coach_name}")
                self.label_2.setText(f"{first_name} {last_name}")
                self.coachexp1.setText(experience)
                self.coachexp1.setStyleSheet("color: white;")  # Set text color to white
                self.coachspec1.setText(specialties)
                self.coachspec1.setStyleSheet("color: white;")  # Set text color to white

            cursor.close()
        except Error as e:
            QMessageBox.critical(self, 'Error', f"Error retrieving coach details: {e}")