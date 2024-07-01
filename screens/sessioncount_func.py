from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.sessioncountUI import Ui_MainWindow

class SessionCountWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    proceed_button = QtCore.pyqtSignal()

    def __init__(self):
        super(SessionCountWindow, self).__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.button_clicked)
        self.proceed.clicked.connect(self.handle_proceed)

    def button_clicked(self):
        self.back_button.emit()

    def handle_proceed(self):
        self.proceed_button.emit()

    def set_spinbox_value(self, value):
        self.spinBox.setMinimum(value)
        self.spinBox.setValue(value)

    def get_spinbox_value(self):
        return self.spinBox.value()