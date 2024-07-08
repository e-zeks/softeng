from mysql.connector import Error

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from screens.adminreportsUI import Ui_MainWindow

class AdminReportsWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()

    #nav bar buttons
    employeemanage_button = QtCore.pyqtSignal()
    clientmanage_button = QtCore.pyqtSignal()
    payments_button = QtCore.pyqtSignal()
    reports_button = QtCore.pyqtSignal()
    maintenance_button = QtCore.pyqtSignal()
    userlogs_button = QtCore.pyqtSignal()
    help_button = QtCore.pyqtSignal()
    logout_button = QtCore.pyqtSignal()



    def __init__(self, conn):
        super(AdminReportsWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn
        self.current_user_id = 1  # Store the current user's ID
        self.current_user_type = 'Admin'  # Store the current user's type as a string

        self.back.clicked.connect(self.handle_backbutton)
        #nav bar buttons
        self.employees.clicked.connect(self.handle_employees)
        self.clients.clicked.connect(self.handle_clients)
        self.payments.clicked.connect(self.handle_payments)
        self.report.clicked.connect(self.handle_reports)
        self.userlogs.clicked.connect(self.handle_userlogs)
        self.maintenance.clicked.connect(self.handle_maintenance)
        self.help.clicked.connect(self.handle_help)
        self.logout.clicked.connect(self.handle_logout)

        #function buttons
        self.clientreport.clicked.connect(self.open_file_dialog)
        self.coachreport.clicked.connect(self.open_file_dialog)
        self.transactionreport.clicked.connect(self.open_file_dialog)


    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Report File", "", "All Files (*);;CSV Files (*.csv);;Excel Files (*.xlsx);;Text Files (*.txt)", options=options)
        if file_name:
            print(f"Selected file: {file_name}")

    def handle_backbutton(self):
        self.back_button.emit()

    def handle_employees(self):
        self.employeemanage_button.emit()

    def handle_clients(self):
        self.clientmanage_button.emit()

    def handle_payments(self):
        self.payments_button.emit()

    def handle_reports(self):
        self.reports_button.emit()

    def handle_userlogs(self):
        self.userlogs_button.emit()

    def handle_maintenance(self):
        self.maintenance_button.emit()

    def handle_help(self):
        self.help_button.emit()

    def log_user_logout(self):
        if self.current_user_id is None:
            print("No current user logged in")  # Debug print
            return

        try:
            cursor = self.conn.cursor()
            # Retrieve the latest LogID
            cursor.execute("SELECT MAX(LogID) FROM user_logs")
            last_log_id = cursor.fetchone()[0]

            if last_log_id is not None:
                query = """
                     UPDATE user_logs
                     SET Logout_Time = NOW()
                     WHERE LogID = %s AND Logout_Time IS NULL
                 """
                cursor.execute(query, (last_log_id,))
                self.conn.commit()
                print(f"Logout time updated for LogID: {last_log_id}")  # Debug print
            else:
                print("No LogID found to update logout time")  # Debug print

        except Error as e:
            print(f"Error logging user logout: {e}")
        finally:
            cursor.close()
            self.current_user_id = None  # Clear the current user ID after logging out
            self.current_user_type = None  # Clear the current user type after logging out

    def handle_logout(self):
        print("Logging out user")  # Log the logout time
        self.log_user_logout()
        self.logout_button.emit()