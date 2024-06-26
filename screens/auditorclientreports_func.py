from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.auditorclientreportsUI import Ui_MainWindow

class AuditorClientsWindow(QMainWindow, Ui_MainWindow):
    logout_button = QtCore.pyqtSignal()
    save_button = QtCore.pyqtSignal()
    back_button = QtCore.pyqtSignal()

    def __init__(self):
        super(AuditorClientsWindow, self).__init__()
        self.setupUi(self)
        self.logout.clicked.connect(self.logoutbutton_clicked)
        self.savetodesktop.clicked.connect(self.generate_report)
        self.back.clicked.connect(self.backbutton_clicked)

    def logoutbutton_clicked(self):
        print("Logging Out")
        self.logout_button.emit()

    def generate_report(self):
        print("Generated report")
        self.save_button.emit()

    def backbutton_clicked(self):
        print("Back")
        self.back_button.emit()
