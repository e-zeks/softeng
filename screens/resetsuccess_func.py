from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.resetsuccessUI import Ui_MainWindow

class ResetSuccessWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()

    def __init__(self):
        super(ResetSuccessWindow, self).__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.button_clicked)
        self.backtologin.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.back_button.emit()