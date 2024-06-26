from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.calendarUI import Ui_MainWindow

class CalendarWindow(QMainWindow, Ui_MainWindow):
    logout_button = QtCore.pyqtSignal()
    back_button = QtCore.pyqtSignal()

    def __init__(self):
        super(CalendarWindow, self).__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.button_clicked)
        self.logout.clicked.connect(self.handle_logout)

        self.calendar.selectionChanged.connect(self.date_selected)

    def button_clicked(self):
        self.back_button.emit()

    def handle_logout(self):
        self.logout_button.emit()
        print("Logging out")

    def date_selected(self):
        selected_date = self.calendar.selectedDate()
        #formatted_date = selected_date.toString("MMMM d, yyyy")
        print("Date selected:", selected_date.toString())  # Debugging print statement

        #self.date_display_window = DateDisplayWindow(formatted_date)
        #self.date_display_window.show()