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
from screens.bookingOTP_func import BookingOTPWindow
from screens.registerOTP_func import RegisterOTPWindow
from screens.coachhome_func import CoachHomeWindow
from screens.auditorhome_func import AuditorHomeWindow
from screens.userdetails_func import UserDetailsWindow
from screens.calender_func import CalendarWindow
from screens.empdetails_func import EmployeeDetailsWindow
from screens.coachselection_func import CoachSelectionWindow
from screens.packageselection_func import PackageSelectionWindow
from screens.maintenance_func import MaintenanceWindow
from screens.userlogs_func import UserLogsWindow
from screens.addcoach_func import AddCoachWindow
from screens.editcoach_func import EditCoachWindow
from screens.addpackage_func import AddPackageWindow
from screens.editpackage_func import EditPackageWindow
from screens.clientreport_func import ClientReportWindow
from screens.clientdetails_func import ClientDetailsWindow
from screens.payments_func import PaymentWindow
from screens.sessioncount_func import SessionCountWindow
from screens.finalselection_func import FinalSelectionWindow
from screens.finalizeschedule_func import FinalizeSchedWindow
from screens.help_func import HelpWindow
from screens.about_func import AboutWindow
from screens.coachesreport_func import CoachReportWindow
from screens.transactionreport_func import TransactionReportWindow
from screens.transactionsuccessful_func import TransactionSuccessfulWindow

class MainWindow(QMainWindow):
    def __init__(self, conn):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Main Window")
        self.setMinimumSize(960, 540)

        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        self.email = None # OTP parameter

        # data retrievers for client booking
        self.clientdetails = {}
        self.selectedcoach = {}
        self.selectedpackage = {}
        self.sessioncount = ""
        self.selectedsched = {}

        # Full Screen on start
        self.showMaximized()

        # Variable Definitions - class of screen functions
        self.startup_screen = startup_win()
        self.login_screen = LoginWindow(conn)
        self.startup2_screen = startup2_win()
        self.register_screen = RegisterWindow(conn)
        self.clientreg_screen = ClientRegWindow(conn)
        self.coachselection_screen = CoachSelectionWindow(conn)
        self.packageselection_screen = PackageSelectionWindow(conn)
        self.forgotpass_screen = ForgotPassWindow(conn)
        self.enterOTP_screen = OTPWindow()
        self.bookingOTP_screen = BookingOTPWindow(conn)
        self.registerOTP_screen = RegisterOTPWindow(conn)
        self.manageemp_screen = ManageEmpWindow(conn)
        self.manageclient_screen = ManageClientWindow(conn)
        self.maintenance_screen = MaintenanceWindow()
        self.addcoach_screen = AddCoachWindow(conn)
        self.editcoach_screen = EditCoachWindow(conn)
        self.addpackage_screen = AddPackageWindow(conn)
        self.editpackage_screen = EditPackageWindow(conn)
        self.userlogs_screen = UserLogsWindow(conn)
        self.adminhome_screen = AdminHomeWindow()
        self.coachhome_screen = CoachHomeWindow(conn)
        self.calendar_screen = CalendarWindow()
        self.auditorhome_screen = AuditorHomeWindow(conn)
        self.clientreport_screen = ClientReportWindow(conn)
        self.resetpass_screen = ResetPassWindow(conn)
        self.resetsuccess_screen = ResetSuccessWindow()
        self.userdetails_screen = UserDetailsWindow(conn)
        self.clientdetails_screen = ClientDetailsWindow({}, conn)
        self.empdetails_screen = EmployeeDetailsWindow({}, conn)
        self.payments_screen = PaymentWindow(conn)
        self.sessioncount_screen = SessionCountWindow()
        self.finalselection_screen = FinalSelectionWindow()
        self.finalizesched_screen = FinalizeSchedWindow()
        self.help_screen = HelpWindow()
        self.about_screen = AboutWindow()
        self.coachesreport_screen = CoachReportWindow(conn)
        self.transactionreport_screen = TransactionReportWindow(conn)
        self.transactionsuccessful_screen = TransactionSuccessfulWindow(conn)

        # Adding Screens to Stack
        self.stack.addWidget(self.startup_screen)  # startup
        self.stack.addWidget(self.login_screen)  # login
        self.stack.addWidget(self.register_screen)  # employee register
        self.stack.addWidget(self.startup2_screen)  # startup 2
        self.stack.addWidget(self.clientreg_screen)  # client register
        self.stack.addWidget(self.coachselection_screen) # coach select
        self.stack.addWidget(self.packageselection_screen) # package select
        self.stack.addWidget(self.forgotpass_screen)  # forgot password
        self.stack.addWidget(self.enterOTP_screen) # enter OTP
        self.stack.addWidget(self.bookingOTP_screen) # booking OTP
        self.stack.addWidget(self.registerOTP_screen) # register OTP
        self.stack.addWidget(self.resetpass_screen) # reset pass
        self.stack.addWidget(self.resetsuccess_screen) # reset success
        self.stack.addWidget(self.adminhome_screen) # admin home
        self.stack.addWidget(self.coachhome_screen) # coach home
        self.stack.addWidget(self.auditorhome_screen) # auditor home
        self.stack.addWidget(self.userdetails_screen) # client details
        self.stack.addWidget(self.manageemp_screen) # employee management
        self.stack.addWidget(self.empdetails_screen) # employee details
        self.stack.addWidget(self.manageclient_screen) # client management
        self.stack.addWidget(self.clientdetails_screen) # client details
        self.stack.addWidget(self.calendar_screen) # calendar screen
        self.stack.addWidget(self.maintenance_screen) # maintenance screen
        self.stack.addWidget(self.userlogs_screen) # user logs screen
        self.stack.addWidget(self.addcoach_screen) # add coach screen
        self.stack.addWidget(self.editcoach_screen) # edit coach screen
        self.stack.addWidget(self.addpackage_screen) # add package screen
        self.stack.addWidget(self.editpackage_screen) # edit package screen
        self.stack.addWidget(self.clientreport_screen) # clients report screen
        self.stack.addWidget(self.payments_screen) # payment screen
        self.stack.addWidget(self.sessioncount_screen) # session count screen
        self.stack.addWidget(self.finalselection_screen) # final selection screen
        self.stack.addWidget(self.finalizesched_screen) # finalize schedule screen
        self.stack.addWidget(self.help_screen) # help screen
        self.stack.addWidget(self.about_screen) # about screen
        self.stack.addWidget(self.coachesreport_screen) # coach report screen
        self.stack.addWidget(self.transactionreport_screen) # transaction report screen
        self.stack.addWidget(self.transactionsuccessful_screen) # transaction successful screen

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
        self.register_screen.register_button.connect(self.handle_registerOTP)

        self.startup2_screen.client_signal_btn.connect(self.handle_clientreg)
        self.startup2_screen.employee_signal_btn.connect(self.handle_register)
        self.startup2_screen.back_button.connect(self.show_startupui)

        self.clientreg_screen.back_button.connect(self.handle_startup2)
        self.clientreg_screen.register_button.connect(self.handle_bookingOTP)

        self.userdetails_screen.back_button.connect(self.handle_login)
        self.userdetails_screen.save_button.connect(self.handle_coachselect)

        self.coachselection_screen.back_button.connect(self.handle_login) #back button parameter problem if clientdetails
        self.coachselection_screen.book_button.connect(self.handle_packageselect)

        self.packageselection_screen.back_button.connect(self.handle_coachselect)
        self.packageselection_screen.book_button.connect(self.handle_sessioncount)

        self.sessioncount_screen.back_button.connect(self.handle_packageselect)
        self.sessioncount_screen.proceed_button.connect(self.handle_finalselection)

        self.finalselection_screen.back_button.connect(self.handle_sessioncount)
        self.finalselection_screen.proceed_button.connect(self.handle_finalizesched)

        self.finalizesched_screen.back_button.connect(self.handle_finalselection)
        self.finalizesched_screen.confirm_button.connect(self.handle_transactionsuccessful)

        self.transactionsuccessful_screen.confirm_button.connect(self.handle_login)

        self.forgotpass_screen.back_button.connect(self.handle_login)
        self.forgotpass_screen.sendOTP_button.connect(self.handle_enterOTP)

        self.enterOTP_screen.back_button.connect(self.handle_forgotpass)
        self.enterOTP_screen.verifyOTP_button.connect(self.handle_resetpass)
        #self.enterOTP_screen.resend_button.connect()

        self.bookingOTP_screen.back_button.connect(self.handle_clientreg)
        self.bookingOTP_screen.verifyOTP_button.connect(self.handle_login)

        self.registerOTP_screen.back_button.connect(self.handle_register)
        self.registerOTP_screen.verifyOTP_button.connect(self.handle_login)

        self.resetpass_screen.back_button.connect(self.handle_login)
        self.resetpass_screen.reset_button.connect(self.handle_resetsuccess)

        self.resetsuccess_screen.back_button.connect(self.handle_login)

        self.adminhome_screen.logout_button.connect(self.show_startupui)
        self.adminhome_screen.employeemanage_button.connect(self.handle_manageemp)
        self.adminhome_screen.clientmanage_button.connect(self.handle_manageclient)
        self.adminhome_screen.userlogs_button.connect(self.handle_userlogs)
        self.adminhome_screen.maintenance_button.connect(self.handle_maintenance)
        self.adminhome_screen.help_button.connect(self.handle_help)
        self.adminhome_screen.payments_button.connect(self.handle_payments)

        self.manageemp_screen.logout_button.connect(self.handle_login)
        self.manageemp_screen.edit_button.connect(self.handle_empdetails)
        self.manageemp_screen.back_button.connect(self.handle_adminlogin)
        self.manageemp_screen.clientmanage_button.connect(self.handle_manageclient)
        self.manageemp_screen.userlogs_button.connect(self.handle_userlogs)
        self.manageemp_screen.maintenance_button.connect(self.handle_maintenance)
        self.manageemp_screen.help_button.connect(self.handle_help)
        self.manageemp_screen.payments_button.connect(self.handle_payments)

        self.empdetails_screen.cancel_button.connect(self.handle_manageemp)
        self.empdetails_screen.save_button.connect(self.handle_manageemp)

        self.manageclient_screen.back_button.connect(self.handle_adminlogin)
        self.manageclient_screen.edit_button.connect(self.handle_clientdetails)
        self.manageclient_screen.logout_button.connect(self.handle_login)
        self.manageclient_screen.employeemanage_button.connect(self.handle_manageemp)
        self.manageclient_screen.userlogs_button.connect(self.handle_userlogs)
        self.manageclient_screen.maintenance_button.connect(self.handle_maintenance)
        self.manageclient_screen.help_button.connect(self.handle_help)
        self.manageclient_screen.payments_button.connect(self.handle_payments)

        self.clientdetails_screen.cancel_button.connect(self.handle_manageclient)
        self.clientdetails_screen.save_button.connect(self.handle_manageclient)

        self.userlogs_screen.back_button.connect(self.handle_adminlogin)
        self.userlogs_screen.logout_button.connect(self.show_startupui)
        self.userlogs_screen.employeemanage_button.connect(self.handle_manageemp)
        self.userlogs_screen.clientmanage_button.connect(self.handle_manageclient)
        self.userlogs_screen.maintenance_button.connect(self.handle_maintenance)
        self.userlogs_screen.help_button.connect(self.handle_help)
        self.userlogs_screen.payments_button.connect(self.handle_payments)

        self.maintenance_screen.addcoach_button.connect(self.handle_addcoach)
        self.maintenance_screen.editcoach_button.connect(self.handle_editcoach)
        self.maintenance_screen.addpackage_button.connect(self.handle_addpackage)
        self.maintenance_screen.editpackage_button.connect(self.handle_editpackage)
        self.maintenance_screen.back_button.connect(self.handle_adminlogin)
        self.maintenance_screen.employeemanage_button.connect(self.handle_manageemp)
        self.maintenance_screen.clientmanage_button.connect(self.handle_manageclient)
        self.maintenance_screen.userlogs_button.connect(self.handle_userlogs)
        self.maintenance_screen.logout_button.connect(self.handle_login)
        self.maintenance_screen.help_button.connect(self.handle_help)
        self.maintenance_screen.payments_button.connect(self.handle_payments)

        self.addcoach_screen.cancel_button.connect(self.handle_maintenance)
        self.addcoach_screen.save_button.connect(self.handle_maintenance)
        self.addcoach_screen.logout_button.connect(self.show_startupui)
        self.addcoach_screen.employeemanage_button.connect(self.handle_manageemp)
        self.addcoach_screen.clientmanage_button.connect(self.handle_manageclient)
        self.addcoach_screen.userlogs_button.connect(self.handle_userlogs)
        self.addcoach_screen.maintenance_button.connect(self.handle_maintenance)
        self.addcoach_screen.help_button.connect(self.handle_help)
        self.addcoach_screen.payments_button.connect(self.handle_payments)

        self.editcoach_screen.cancel_button.connect(self.handle_maintenance)
        self.editcoach_screen.save_button.connect(self.handle_maintenance)
        self.editcoach_screen.logout_button.connect(self.show_startupui)
        self.editcoach_screen.employeemanage_button.connect(self.handle_manageemp)
        self.editcoach_screen.clientmanage_button.connect(self.handle_manageclient)
        self.editcoach_screen.userlogs_button.connect(self.handle_userlogs)
        self.editcoach_screen.maintenance_button.connect(self.handle_maintenance)
        self.editcoach_screen.help_button.connect(self.handle_help)
        self.editcoach_screen.payments_button.connect(self.handle_payments)

        self.addpackage_screen.cancel_button.connect(self.handle_maintenance)
        self.addpackage_screen.save_button.connect(self.handle_maintenance)
        self.addpackage_screen.logout_button.connect(self.show_startupui)
        self.addpackage_screen.employeemanage_button.connect(self.handle_manageemp)
        self.addpackage_screen.clientmanage_button.connect(self.handle_manageclient)
        self.addpackage_screen.userlogs_button.connect(self.handle_userlogs)
        self.addpackage_screen.maintenance_button.connect(self.handle_maintenance)
        self.addpackage_screen.help_button.connect(self.handle_help)
        self.addpackage_screen.payments_button.connect(self.handle_payments)

        self.editpackage_screen.cancel_button.connect(self.handle_maintenance)
        self.editpackage_screen.save_button.connect(self.handle_maintenance)
        self.editpackage_screen.logout_button.connect(self.show_startupui)
        self.editpackage_screen.employeemanage_button.connect(self.handle_manageemp)
        self.editpackage_screen.clientmanage_button.connect(self.handle_manageclient)
        self.editpackage_screen.userlogs_button.connect(self.handle_userlogs)
        self.editpackage_screen.maintenance_button.connect(self.handle_maintenance)
        self.editpackage_screen.help_button.connect(self.handle_help)
        self.editpackage_screen.payments_button.connect(self.handle_payments)

        self.payments_screen.back_button.connect(self.handle_adminlogin)
        self.payments_screen.logout_button.connect(self.show_startupui)
        self.payments_screen.employeemanage_button.connect(self.handle_manageemp)
        self.payments_screen.clientmanage_button.connect(self.handle_manageclient)
        self.payments_screen.userlogs_button.connect(self.handle_userlogs)
        self.payments_screen.maintenance_button.connect(self.handle_maintenance)

        self.coachhome_screen.logout_button.connect(self.handle_login)
        self.coachhome_screen.schedule_button.connect(self.handle_schedule)

        self.calendar_screen.logout_button.connect(self.handle_login)
        self.calendar_screen.back_button.connect(self.handle_coachlogin)

        self.auditorhome_screen.logout_button.connect(self.handle_login)
        self.auditorhome_screen.clientreport_button.connect(self.handle_clientreport)
        self.auditorhome_screen.transactionreport_button.connect(self.handle_transactionreport)
        self.auditorhome_screen.coachesreport_button.connect(self.handle_coachesreport)

        self.clientreport_screen.logout_button.connect(self.handle_login)
        self.clientreport_screen.back_button.connect(self.handle_auditorlogin)
        self.clientreport_screen.transactionreport_button.connect(self.handle_transactionreport)
        self.clientreport_screen.coachesreport_button.connect(self.handle_coachesreport)

        self.coachesreport_screen.logout_button.connect(self.handle_login)
        self.coachesreport_screen.back_button.connect(self.handle_auditorlogin)
        self.coachesreport_screen.transactionreport_button.connect(self.handle_transactionreport)
        self.coachesreport_screen.clientreport_button.connect(self.handle_clientreport)

        self.transactionreport_screen.logout_button.connect(self.handle_login)
        self.transactionreport_screen.back_button.connect(self.handle_auditorlogin)
        self.transactionreport_screen.clientreport_button.connect(self.handle_clientreport)
        self.transactionreport_screen.coachesreport_button.connect(self.handle_coachesreport)

        self.about_screen.back_button.connect(self.handle_help)

    def show_startupui(self):
        self.stack.setCurrentWidget(self.startup_screen)
    def handle_login(self):
        self.stack.setCurrentWidget(self.login_screen)
    def handle_forgotpass(self):
        self.stack.setCurrentWidget(self.forgotpass_screen)
    def handle_register(self):
        self.register_screen.clear_fields()
        self.stack.setCurrentWidget(self.register_screen)
    def handle_startup2(self):
        self.stack.setCurrentWidget(self.startup2_screen)
    def handle_clientreg(self):
        self.clientreg_screen.clear_fields()
        self.stack.setCurrentWidget(self.clientreg_screen)
    def handle_enterOTP(self, otp, email):
        self.email = email
        self.enterOTP_screen.set_otp(otp)
        self.stack.setCurrentWidget(self.enterOTP_screen)
    def handle_bookingOTP(self, otp, data_tuple):
        self.email = data_tuple[5]
        self.bookingOTP_screen.set_otp(otp)
        self.bookingOTP_screen.set_data_tuple(data_tuple)
        self.stack.setCurrentWidget(self.bookingOTP_screen)
    def handle_registerOTP(self, otp, data_tuple):
        self.email = data_tuple[2]
        self.registerOTP_screen.set_otp(otp)
        self.registerOTP_screen.set_data_tuple(data_tuple)
        self.stack.setCurrentWidget(self.registerOTP_screen)
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
    def handle_payments(self):
        self.stack.setCurrentWidget(self.payments_screen)
    def handle_maintenance(self):
        self.stack.setCurrentWidget(self.maintenance_screen)
    def handle_addcoach(self):
        self.addcoach_screen.refresh_fields()
        self.stack.setCurrentWidget(self.addcoach_screen)
    def handle_editcoach(self):
        #self.editcoach_screen.refresh_fields()
        self.stack.setCurrentWidget(self.editcoach_screen)
    def handle_addpackage(self):
        self.stack.setCurrentWidget(self.addpackage_screen)
    def handle_editpackage(self):
        self.editpackage_screen.refresh_data()
        self.stack.setCurrentWidget(self.editpackage_screen)
    def handle_help(self):
        self.stack.setCurrentWidget(self.help_screen)
    def handle_about(self):
        self.stack.setCurrentWidget(self.about_screen)
    def handle_coachlogin(self):
        self.stack.setCurrentWidget(self.coachhome_screen)
    def handle_schedule(self):
        self.stack.setCurrentWidget(self.calendar_screen)
    def handle_auditorlogin(self):
        self.stack.setCurrentWidget(self.auditorhome_screen)
    def handle_clientreport(self):
        self.stack.setCurrentWidget(self.clientreport_screen)
    def handle_coachesreport(self):
        self.stack.setCurrentWidget(self.coachesreport_screen)
    def handle_transactionreport(self):
        self.stack.setCurrentWidget(self.transactionreport_screen)
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
        self.clientdetails = self.userdetails_screen.get_bookingdetails(client_details)
        self.userdetails_screen.set_clientdetails(client_details)
        self.stack.setCurrentWidget(self.userdetails_screen)
    def handle_clientdetails(self, client_details):
        self.clientdetails_screen.set_clientdetails(client_details)
        self.clientdetails_screen.client_details = client_details
        self.stack.setCurrentWidget(self.clientdetails_screen)
    def handle_coachselect(self):
        self.coachselection_screen.add_initial_coach_widgets()
        self.stack.setCurrentWidget(self.coachselection_screen)
    def handle_packageselect(self):
        self.selectedcoach = self.coachselection_screen.coachdetails
        print(self.selectedcoach)

        self.packageselection_screen.add_initial_packages_widgets()
        self.stack.setCurrentWidget(self.packageselection_screen)
    def handle_sessioncount(self):
        self.selectedpackage = self.packageselection_screen.packagedetails
        print(self.selectedpackage)

        self.sessioncount_screen.set_spinbox_value(self.selectedpackage['min_sessions'])
        self.stack.setCurrentWidget(self.sessioncount_screen)
    def handle_finalselection(self):
        self.sessioncount = self.sessioncount_screen.get_spinbox_value()
        self.finalselection_screen.set_details(self.clientdetails, self.selectedcoach, self.selectedpackage, self.sessioncount)
        self.stack.setCurrentWidget(self.finalselection_screen)
    def handle_finalizesched(self):
        self.finalizesched_screen.clearSelections()
        self.stack.setCurrentWidget(self.finalizesched_screen)
    def handle_transactionsuccessful(self):
        self.selectedsched = self.finalizesched_screen.get_sched_details()
        self.transactionsuccessful_screen.populate_fields(self.clientdetails, self.selectedcoach, self.selectedpackage, self.sessioncount, self.selectedsched)
        self.stack.setCurrentWidget(self.transactionsuccessful_screen)

# Read and write from DB
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            #host="25.48.148.190",
            #user="softengprogram",
            # passwd="pass123",
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