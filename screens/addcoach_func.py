from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.addcoachUI import Ui_MainWindow

class AddCoachWindow(QMainWindow, Ui_MainWindow):
    cancel_button = QtCore.pyqtSignal()

    def __init__(self):
        super(AddCoachWindow, self).__init__()
        self.setupUi(self)
        self.cancel.clicked.connect(self.handle_cancel)

    def handle_cancel(self):
        self.cancel_button.emit()