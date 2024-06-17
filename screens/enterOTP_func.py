from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.enterOTPUI import Ui_MainWindow

class OTPWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    def __init__(self):
        super(OTPWindow, self).__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.back_button.emit()
