from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from screens.enterOTPUI import Ui_MainWindow

class OTPWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    verifyOTP_button = QtCore.pyqtSignal()
    def __init__(self):
        super(OTPWindow, self).__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.button_clicked)
        self.verifyOTP.clicked.connect(self.handle_verifyOTP)
        sent_otp = ""

    def set_otp(self, otp):
        self.sent_otp = otp

    def button_clicked(self):
        self.back_button.emit()

    def handle_verifyOTP(self):
        print(self.sent_otp)
        entered_otp = self.otp1.text()
        if entered_otp == self.sent_otp:
            QMessageBox.information(self, "Success", "OTP Verified Successfully!")
            self.verifyOTP_button.emit()
        else:
            QMessageBox.warning(self, "Failed", "Invalid OTP! Please try again.")
