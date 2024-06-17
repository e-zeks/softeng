from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from screens.bookingUI import Ui_MainWindow

class ClientRegWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()

    # Signal with two string parameters
    def __init__(self):
        super(ClientRegWindow, self).__init__()
        self.setupUi(self)

        #object name (back in this ex.)
        self.back.clicked.connect(self.button_clicked)

    #what happens when clicked
    def button_clicked(self):
        self.back_button.emit()