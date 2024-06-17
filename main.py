import sys
import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import QStackedWidget, QMainWindow, QApplication

from screens.booking_func import ClientRegWindow
from screens.login_func import LoginWindow
from screens.startup_func import startup_win
from screens.registeremp_func import RegisterWindow
from screens.startup2_func import startup2_win
from screens.enterOTP_func import OTPWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Main Window")
        self.setMinimumSize(960, 540)

        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        #Full Screen on start
        #self.showFullScreen()

        #Variable Definitions - class of screen functions
        self.startup_screen = startup_win()
        self.login_screen = LoginWindow()
        self.startup2_screen = startup2_win()
        self.register_screen = RegisterWindow()
        self.clientreg_screen = ClientRegWindow()
        self.OTP_screen = OTPWindow()

        #Adding Screens to Stack
        self.stack.addWidget(self.startup_screen) #startup
        self.stack.addWidget(self.login_screen) #login
        self.stack.addWidget(self.register_screen) #employee register
        self.stack.addWidget(self.startup2_screen) #startup 2
        self.stack.addWidget(self.clientreg_screen) #client register
        self.stack.addWidget(self.OTP_screen) #WINDOW FOR OTP SCREEN

        #startup
        self.stack.setCurrentWidget(self.startup_screen)

        #Button functions
        self.startup_screen.login_signal_btn.connect(self.handle_login)
        self.startup_screen.register_signal_btn.connect(self.handle_startup2)

        self.login_screen.back_button.connect(self.show_startupui)
        self.login_screen.forgot_button.connect(self.handle_otp)

        self.register_screen.back_button.connect(self.handle_startup2)

        self.startup2_screen.client_signal_btn.connect(self.handle_clientreg)
        self.startup2_screen.employee_signal_btn.connect(self.handle_register)
        self.startup2_screen.back_button.connect(self.show_startupui)

        self.clientreg_screen.back_button.connect(self.handle_startup2)

        self.OTP_screen.back_button.connect(self.handle_login)

    def show_startupui(self):
        self.stack.setCurrentWidget(self.startup_screen)

    def handle_login(self):
        self.stack.setCurrentWidget(self.login_screen)

    def handle_otp(self):
        self.stack.setCurrentWidget(self.OTP_screen)

    def handle_register(self):
        self.stack.setCurrentWidget(self.register_screen)

    def handle_startup2(self):
        self.stack.setCurrentWidget(self.startup2_screen)

    def handle_clientreg(self):
        self.stack.setCurrentWidget(self.clientreg_screen)

#Read and write from DB
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1234",
            database="softeng"
        )
        if conn.is_connected():
            print("Connected to MySQL database")
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

def main():
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
        main()