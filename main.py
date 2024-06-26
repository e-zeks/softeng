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
from screens.userdetails_func import ClientDetailsWindow
from screens.calender_func import CalendarWindow
from screens.empdetails_func import EmployeeDetailsWindow
from screens.coachselection_func import CoachSelectionWindow
from screens.maintenance_func import MaintenanceWindow
from screens.userlogs_func import UserLogsWindow
from screens.addcoach_func import AddCoachWindow
from screens.addpackage_func import AddPackageWindow
from screens.clientreport_func import ClientReportWindow

class MainWindow(QMainWindow):
    def __init__(self, conn):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Main Window")
        self.setMinimumSize(960, 540)

        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        self.email = None # OTP parameter

        # Full Screen on start
        self.showMaximized()

        # Variable Definitions - class of screen functions
        self.startup_screen = startup_win()
        self.login_screen = LoginWindow(conn)
        self.startup2_screen = startup2_win()
        self.register_screen = RegisterWindow(conn)
        self.clientreg_screen = ClientRegWindow(conn)
        self.coachselection_screen = CoachSelectionWindow()
        self.forgotpass_screen = ForgotPassWindow(conn)
        self.enterOTP_screen = OTPWindow()
        self.manageemp_screen = ManageEmpWindow(conn)
        self.manageclient_screen = ManageClientWindow(conn)
        self.maintenance_screen = MaintenanceWindow()
        self.addcoach_screen = AddCoachWindow()
        self.addpackage_screen = AddPackageWindow()
        self.userlogs_screen = UserLogsWindow(conn)
        self.adminhome_screen = AdminHomeWindow()
        self.coachhome_screen = CoachHomeWindow()
        self.calendar_screen = CalendarWindow()
        self.auditorhome_screen = AuditorHomeWindow()
        self.clientreport_screen = ClientReportWindow(conn)
        self.resetpass_screen = ResetPassWindow(conn)
        self.resetsuccess_screen = ResetSuccessWindow()
        self.clientdetails_screen = ClientDetailsWindow(conn)
        self.empdetails_screen = EmployeeDetailsWindow({}, conn)

        # Adding Screens to Stack
        self.stack.addWidget(self.startup_screen)  # startup
        self.stack.addWidget(self.login_screen)  # login
        self.stack.addWidget(self.register_screen)  # employee register
        self.stack.addWidget(self.startup2_screen)  # startup 2
        self.stack.addWidget(self.clientreg_screen)  # client register
        self.stack.addWidget(self.coachselection_screen) # coach select
        self.stack.addWidget(self.forgotpass_screen)  # forgot password
        self.stack.addWidget(self.enterOTP_screen) # enter OTP
        self.stack.addWidget(self.resetpass_screen) # reset pass
        self.stack.addWidget(self.resetsuccess_screen) # reset success
        self.stack.addWidget(self.adminhome_screen) # admin home
        self.stack.addWidget(self.coachhome_screen) # coach home
        self.stack.addWidget(self.auditorhome_screen) # auditor home
        self.stack.addWidget(self.clientdetails_screen) # client details
        self.stack.addWidget(self.manageemp_screen) # employee management
        self.stack.addWidget(self.empdetails_screen) # employee details
        self.stack.addWidget(self.manageclient_screen) # client management
        self.stack.addWidget(self.calendar_screen) # calendar screen
        self.stack.addWidget(self.maintenance_screen) # maintenance screen
        self.stack.addWidget(self.userlogs_screen) # user logs screen
        self.stack.addWidget(self.addcoach_screen) # add coach screen
        self.stack.addWidget(self.addpackage_screen) # add package screen
        self.stack.addWidget(self.clientreport_screen) # clients report screen

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
        self.login_screen.loginclient_button.connect(self.handle_clientlogin)

        self.register_screen.back_button.connect(self.handle_startup2)

        self.startup2_screen.client_signal_btn.connect(self.handle_clientreg)
        self.startup2_screen.employee_signal_btn.connect(self.handle_register)
        self.startup2_screen.back_button.connect(self.show_startupui)

        self.clientreg_screen.back_button.connect(self.handle_startup2)
        self.clientreg_screen.register_button.connect(self.handle_coachselect)

        self.clientdetails_screen.back_button.connect(self.handle_login)
        self.clientdetails_screen.save_button.connect(self.handle_coachselect)

        self.coachselection_screen.back_button.connect(self.handle_clientlogin) #back button parameter problem for details

        self.forgotpass_screen.back_button.connect(self.handle_login)
        self.forgotpass_screen.sendOTP_button.connect(self.handle_enterOTP)

        self.enterOTP_screen.back_button.connect(self.handle_forgotpass)
        self.enterOTP_screen.verifyOTP_button.connect(self.handle_resetpass)
        #self.enterOTP_screen.resend_button.connect()

        self.resetpass_screen.back_button.connect(self.handle_login)
        self.resetpass_screen.reset_button.connect(self.handle_resetsuccess)

        self.resetsuccess_screen.back_button.connect(self.handle_login)

        self.adminhome_screen.logout_button.connect(self.show_startupui)
        self.adminhome_screen.employeemanage_button.connect(self.handle_manageemp)
        self.adminhome_screen.clientmanage_button.connect(self.handle_manageclient)
        self.adminhome_screen.userlogs_button.connect(self.handle_userlogs)
        self.adminhome_screen.maintenance_button.connect(self.handle_maintenance)

        self.manageemp_screen.logout_button.connect(self.handle_login)
        self.manageemp_screen.back_button.connect(self.handle_adminlogin)
        self.manageemp_screen.clientmanage_button.connect(self.handle_manageclient)
        self.manageemp_screen.edit_button.connect(self.handle_empdetails)
        self.manageemp_screen.userlogs_button.connect(self.handle_userlogs)
        self.manageemp_screen.maintenance_button.connect(self.handle_maintenance)

        self.empdetails_screen.cancel_button.connect(self.handle_manageemp)
        self.empdetails_screen.save_button.connect(self.handle_manageemp)

        self.manageclient_screen.logout_button.connect(self.handle_login)
        self.manageclient_screen.employeemanage_button.connect(self.handle_manageemp)
        self.manageclient_screen.userlogs_button.connect(self.handle_userlogs)
        self.manageclient_screen.maintenance_button.connect(self.handle_maintenance)

        self.maintenance_screen.addcoach_button.connect(self.handle_addcoach)
        self.maintenance_screen.addpackage_button.connect(self.handle_addpackage)
        self.maintenance_screen.employeemanage_button.connect(self.handle_manageemp)
        self.maintenance_screen.clientmanage_button.connect(self.handle_manageclient)
        self.maintenance_screen.userlogs_button.connect(self.handle_userlogs)
        self.maintenance_screen.logout_button.connect(self.handle_login)

        self.addcoach_screen.cancel_button.connect(self.handle_maintenance)

        self.addpackage_screen.cancel_button.connect(self.handle_maintenance)

        self.coachhome_screen.logout_button.connect(self.handle_login)
        self.coachhome_screen.schedule_button.connect(self.handle_schedule)

        self.calendar_screen.logout_button.connect(self.handle_login)
        self.calendar_screen.back_button.connect(self.handle_coachlogin)

        self.auditorhome_screen.logout_button.connect(self.handle_login)
        self.auditorhome_screen.clientreport_button.connect(self.handle_clientreport)

        self.clientreport_screen.back_button.connect(self.handle_auditorlogin)

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
    def handle_coachselect(self):
        self.stack.setCurrentWidget(self.coachselection_screen)
    def handle_enterOTP(self, otp, email):
        self.email = email
        self.enterOTP_screen.set_otp(otp)
        self.stack.setCurrentWidget(self.enterOTP_screen)
    def handle_resetpass(self):
        self.resetpass_screen.set_email(self.email)
        self.stack.setCurrentWidget(self.resetpass_screen)
    def handle_resetsuccess(self):
        self.stack.setCurrentWidget(self.resetsuccess_screen)
    def handle_adminlogin(self):
        self.stack.setCurrentWidget(self.adminhome_screen)
    def handle_manageemp(self):
        self.manageemp_screen.refresh_data()
        self.stack.setCurrentWidget(self.manageemp_screen)
    def handle_empdetails(self, emp_details):
        self.empdetails_screen.set_empdetails(emp_details)
        self.empdetails_screen.emp_details = emp_details
        self.stack.setCurrentWidget(self.empdetails_screen)
    def handle_manageclient(self):
        self.manageclient_screen.refresh_data()
        self.stack.setCurrentWidget(self.manageclient_screen)
    def handle_userlogs(self):
        self.userlogs_screen.refresh_data()
        self.stack.setCurrentWidget(self.userlogs_screen)
    def handle_maintenance(self):
        self.stack.setCurrentWidget(self.maintenance_screen)
    def handle_addcoach(self):
        self.stack.setCurrentWidget(self.addcoach_screen)
    def handle_addpackage(self):
        self.stack.setCurrentWidget(self.addpackage_screen)
    def handle_coachlogin(self):
        self.stack.setCurrentWidget(self.coachhome_screen)
    def handle_schedule(self):
        self.stack.setCurrentWidget(self.calendar_screen)
    def handle_auditorlogin(self):
        self.stack.setCurrentWidget(self.auditorhome_screen)
    def handle_clientreport(self):
        self.stack.setCurrentWidget(self.clientreport_screen)
    def handle_clientlogin(self, client_data):
        client_details = {
            'Last_Name': client_data['Last_Name'],
            'First_Name': client_data['First_Name'],
            'Address': client_data['Address'],
            'Birthdate': client_data['Birthdate'],
            'Contact_Number': client_data['Contact_Number'],
            'Email': client_data['Email'],
            'Username': client_data['Username'],
            'Password': client_data['Password'],
            'Program_Plan': client_data['Program_Plan'],
            'Conditions': client_data['Conditions']
        }
        self.clientdetails_screen.set_clientdetails(client_details)
        self.stack.setCurrentWidget(self.clientdetails_screen)

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