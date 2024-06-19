from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from screens.coachhomeUI import Ui_MainWindow

class CoachHomeWindow(QMainWindow, Ui_MainWindow):
    logout_button = QtCore.pyqtSignal()

    def __init__(self):
        super(CoachHomeWindow, self).__init__()
        self.setupUi(self)
        self.logout.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print("Logging Out")
        self.logout_button.emit()