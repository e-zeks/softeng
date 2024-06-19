import sys
import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import QStackedWidget, QMainWindow, QApplication

from screens.adminhome_func import AdminHomeWindow
from screens.booking_func import ClientRegWindow
from screens.forgotpass_func import ForgotPassWindow
from screens.login_func import LoginWindow
from screens.manageemp_func import ManageEmpWindow
from screens.manageclient_func import ManageClientWindow
from screens.resetpass_func import ResetPassWindow
from screens.resetsuccess_func import ResetSuccessWindow
from screens.startup_func import startup_win
from screens.registeremp_func import RegisterWindow
from screens.startup2_func import startup2_win
from screens.enterOTP_func import OTPWindow
from screens.coachhome_func import CoachHomeWindow
from screens.auditorhome_func import AuditorHomeWindow

class MainWindow(QMainWindow):
    def __init__(self, conn):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Main Window")
        self.setMinimumSize(960, 540)

        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        self.email = None

        # Full Screen on start
        # self.showFullScreen()

        # Variable Definitions - class of screen functions
        self.startup_screen = startup_win()
        self.login_screen = LoginWindow(conn)
        self.startup2_screen = startup2_win()
        self.register_screen = RegisterWindow(conn)
        self.clientreg_screen = ClientRegWindow(conn)
        self.forgotpass_screen = ForgotPassWindow(conn)
        self.enterOTP_screen = OTPWindow()
        self.manageemp_screen = ManageEmpWindow(conn)
        self.manageclient_screen = ManageClientWindow(conn)
        self.adminhome_screen = AdminHomeWindow()
        self.coachhome_screen = CoachHomeWindow()
        self.auditorhome_screen = AuditorHomeWindow()
        self.resetpass_screen = ResetPassWindow(conn)
        self.resetsuccess_screen = ResetSuccessWindow()

        # Adding Screens to Stack
        self.stack.addWidget(self.startup_screen)  # startup
        self.stack.addWidget(self.login_screen)  # login
        self.stack.addWidget(self.register_screen)  # employee register
        self.stack.addWidget(self.startup2_screen)  # startup 2
        self.stack.addWidget(self.clientreg_screen)  # client register
        self.stack.addWidget(self.forgotpass_screen)  # forgot password
        self.stack.addWidget(self.enterOTP_screen) # enter OTP
        self.stack.addWidget(self.resetpass_screen) # reset pass
        self.stack.addWidget(self.resetsuccess_screen) # reset success
        self.stack.addWidget(self.adminhome_screen) # admin home
        self.stack.addWidget(self.coachhome_screen) # coach home
        self.stack.addWidget(self.auditorhome_screen) # auditor home
        self.stack.addWidget(self.manageemp_screen) # employee management
        self.stack.addWidget(self.manageclient_screen) # client management

        # Startup
        self.stack.setCurrentWidget(self.startup_screen)

        # Button functions
        self.startup_screen.login_signal_btn.connect(self.handle_login)
        self.startup_screen.register_signal_btn.connect(self.handle_startup2)

        self.login_screen.back_button.connect(self.show_startupui)
        self.login_screen.forgot_button.connect(self.handle_forgotpass)
        self.login_screen.loginadmin_button.connect(self.handle_adminlogin)
        self.login_screen.logincoach_button.connect(self.handle_coachlogin)
        self.login_screen.loginauditor_button.connect(self.handle_auditorlogin)
        self.login_screen.loginclient_button.connect(self.handle_clientreg) #revise opening screen for client

        self.register_screen.back_button.connect(self.handle_startup2)

        self.startup2_screen.client_signal_btn.connect(self.handle_clientreg)
        self.startup2_screen.employee_signal_btn.connect(self.handle_register)
        self.startup2_screen.back_button.connect(self.show_startupui)

        self.clientreg_screen.back_button.connect(self.handle_startup2)

        self.forgotpass_screen.back_button.connect(self.handle_login)
        self.forgotpass_screen.sendOTP_button.connect(self.handle_enterOTP)

        self.enterOTP_screen.back_button.connect(self.handle_forgotpass)
        self.enterOTP_screen.verifyOTP_button.connect(self.handle_resetpass)

        self.resetpass_screen.back_button.connect(self.handle_login)
        self.resetpass_screen.reset_button.connect(self.handle_resetsuccess)

        self.resetsuccess_screen.back_button.connect(self.handle_login)

        self.adminhome_screen.logout_button.connect(self.show_startupui)
        self.adminhome_screen.employeemanage_button.connect(self.handle_manageemp)
        self.adminhome_screen.clientmanage_button.connect(self.handle_manageclient)

        self.coachhome_screen.logout_button.connect(self.handle_login)

        self.auditorhome_screen.logout_button.connect(self.handle_login)

        #self.manageemp_screen.back_button.connect(self.handle_adminlogin)

    def show_startupui(self):
        self.stack.setCurrentWidget(self.startup_screen)
    def handle_login(self):
        self.stack.setCurrentWidget(self.login_screen)
    def handle_forgotpass(self):
        self.stack.setCurrentWidget(self.forgotpass_screen)
    def handle_register(self):
        self.stack.setCurrentWidget(self.register_screen)
    def handle_startup2(self):
        self.stack.setCurrentWidget(self.startup2_screen)
    def handle_clientreg(self):
        self.stack.setCurrentWidget(self.clientreg_screen)
    def handle_enterOTP(self, otp, email):
        self.email = email
        self.enterOTP_screen.set_otp(otp)
        self.stack.setCurrentWidget(self.enterOTP_screen)
    def handle_resetpass(self):
        self.resetpass_screen.set_email(self.email)
        self.stack.setCurrentWidget(self.resetpass_screen)
    def handle_resetsuccess(self):
        self.stack.setCurrentWidget(self.resetsuccess_screen)
    def handle_manageemp(self):
        self.stack.setCurrentWidget(self.manageemp_screen)
    def handle_manageclient(self):
        self.stack.setCurrentWidget(self.manageclient_screen)
    def handle_adminlogin(self):
        self.stack.setCurrentWidget(self.adminhome_screen)
    def handle_coachlogin(self):
        self.stack.setCurrentWidget(self.coachhome_screen)
    def handle_auditorlogin(self):
        self.stack.setCurrentWidget(self.auditorhome_screen)

# Read and write from DB
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="softeng"
        )
        if conn.is_connected():
            print("Connected to MySQL database")
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

def main():
    conn = connect_to_db()
    app = QApplication(sys.argv)
    window = MainWindow(conn)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()