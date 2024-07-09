from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.calendarUI import Ui_MainWindow
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

class CalendarWindow(QMainWindow, Ui_MainWindow):
    logout_button = QtCore.pyqtSignal()
    back_button = QtCore.pyqtSignal(dict)
    date_selected_signal = QtCore.pyqtSignal(str, dict)  # Custom signal with a string argument
    clients_button = QtCore.pyqtSignal(dict)

    screen_user = None

    def __init__(self):
        super(CalendarWindow, self).__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.button_clicked)
        self.logout.clicked.connect(self.handle_logout)
        self.clients.clicked.connect(self.handle_clients)
        self.help.clicked.connect(self.handle_help)

        self.calendar.selectionChanged.connect(self.date_selected)

    def set_user(self, current_user):
        self.screen_user = current_user
        print(current_user)

    def button_clicked(self):
        self.back_button.emit(self.screen_user)

    def handle_help(self):
        pdf_path = "C:\\Users\\JC\\Desktop\\softeng-main\\Anytime Fitness User Manual.pdf"
        QDesktopServices.openUrl(QUrl.fromLocalFile(pdf_path))

    def handle_clients(self):
        self.clients_button.emit(self.screen_user)

    def handle_logout(self):
        self.logout_button.emit()
        print("Logging out")

    def date_selected(self):
        selected_date = self.calendar.selectedDate()
        formatted_date = selected_date.toString("MMMM d, yyyy")
        print("Date selected:", formatted_date)  # Debugging print statement
        self.date_selected_signal.emit(formatted_date, self.screen_user)  # Emit the signal with the formatted date