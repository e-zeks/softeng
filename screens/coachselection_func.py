from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.coachselectionUI import Ui_MainWindow

class CoachSelectionWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()

    def __init__(self):
        super(CoachSelectionWindow, self).__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.back_button.emit()