from PyQt5 import QtCore
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow
from screens.helpUI import Ui_MainWindow

class HelpWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    usermanual_button = QtCore.pyqtSignal()
    about_button = QtCore.pyqtSignal()

    def __init__(self):
        super(HelpWindow, self).__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.handle_backbutton)
        self.usermanual.clicked.connect(self.handle_usermanual)
        self.about.clicked.connect(self.handle_about)

    def handle_backbutton(self):
        self.back_button.emit()

    def handle_usermanual(self):
        pdf_path = "D:\zek\3rd yr comsci\summer\CS 304\soft eng\github\Anytime Fitness User Manual.pdf"
        QDesktopServices.openUrl(QUrl.fromLocalFile(pdf_path))

    def handle_about(self):
        self.about_button.emit()