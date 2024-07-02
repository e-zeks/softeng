from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.aboutUI import Ui_MainWindow

class AboutWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    usermanual_button = QtCore.pyqtSignal()
    about_button = QtCore.pyqtSignal()

    def __init__(self):
        super(AboutWindow, self).__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.handle_backbutton)

    def handle_backbutton(self):
        self.back_button.emit()
