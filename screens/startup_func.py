from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from screens.startupUI import Ui_MainWindow

class startup_win(QMainWindow, Ui_MainWindow):
    # login_signal = pyqtSignal(str, str)
    login_signal_btn = pyqtSignal()
    register_signal_btn = pyqtSignal()

    # Signal with two string parameters
    def __init__(self):
        super(startup_win, self).__init__()
        super(startup_win, self).__init__()
        self.setupUi(self)

        self.login.clicked.connect(self.handle_login)
        self.register_2.clicked.connect(self.handle_register)

    def handle_login(self):
        self.login_signal_btn.emit()

    def handle_register(self):
        self.register_signal_btn.emit()