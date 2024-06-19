from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from screens.auditorhomeUI import Ui_MainWindow

class AuditorHomeWindow(QMainWindow, Ui_MainWindow):
    logout_button = QtCore.pyqtSignal()

    def __init__(self):
        super(AuditorHomeWindow, self).__init__()
        self.setupUi(self)
        self.logout.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print("Logging Out")
        self.logout_button.emit()