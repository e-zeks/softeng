import subprocess
from datetime import datetime

from mysql.connector import Error
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from screens.maintenanceUI import Ui_MainWindow

class MaintenanceWindow(QMainWindow, Ui_MainWindow):
    #screen buttons
    back_button = QtCore.pyqtSignal()
    addcoach_button = QtCore.pyqtSignal()
    editcoach_button = QtCore.pyqtSignal()
    addpackage_button = QtCore.pyqtSignal()
    editpackage_button = QtCore.pyqtSignal()

    backup_button = QtCore.pyqtSignal()
    restore_button = QtCore.pyqtSignal()

    #nav bar buttons
    employeemanage_button = QtCore.pyqtSignal()
    clientmanage_button = QtCore.pyqtSignal()
    payments_button = QtCore.pyqtSignal()
    reports_button = QtCore.pyqtSignal()
    userlogs_button = QtCore.pyqtSignal()
    help_button = QtCore.pyqtSignal()
    logout_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(MaintenanceWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn
        self.current_user_id = 1  # Store the current user's ID
        self.current_user_type = 'Admin'  # Store the current user's type as a string


        #screen buttons
        self.back.clicked.connect(self.handle_back)
        self.addcoach.clicked.connect(self.handle_addcoach)
        self.editcoach.clicked.connect(self.handle_editcoach)
        self.addpackage.clicked.connect(self.handle_addpackage)
        self.editpackage.clicked.connect(self.handle_editpackage)

        self.backup.clicked.connect(self.handle_backup)
        self.restore.clicked.connect(self.handle_restore)



        #nav bar buttons
        self.employees.clicked.connect(self.handle_employees)
        self.clients.clicked.connect(self.handle_clients)
        self.payments.clicked.connect(self.handle_payments)
        self.report.clicked.connect(self.handle_reports)
        self.userlogs.clicked.connect(self.handle_userlogs)
        self.help.clicked.connect(self.handle_help)
        self.logout.clicked.connect(self.handle_logout)

    def handle_back(self):
        self.back_button.emit()

    def handle_addcoach(self):
        self.addcoach_button.emit()

    def handle_editcoach(self):
        self.editcoach_button.emit()

    def handle_addpackage(self):
        self.addpackage_button.emit()

    def handle_editpackage(self):
        self.editpackage_button.emit()

    #nav bar screens
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

    def handle_backup(self):
        try:
            # Get the current date
            current_date = datetime.now().strftime("%Y-%m-%d")

            # Prompt the user to choose the backup file location and name
            file_dialog = QFileDialog()
            backup_file_name, _ = file_dialog.getSaveFileName(
                self,
                "Save Backup File",
                f"C:\\Users\\JC\\Desktop\\SQL backups\\softeng_backup_{current_date}_Backup_File.sql",
                "SQL Files (*.sql)"
            )

            if backup_file_name:
                subprocess.run([
                    'mysqldump',
                    '--host=localhost',
                    '--user=root',
                    '--password=12345',
                    'softeng',
                    'employees',
                    'coaches',
                    'packages',
                    'clients',
                    'user_logs',
                    f'--result-file={backup_file_name}'
                ], check=True)

                print("Backup successful.")
                QMessageBox.information(self, "Backup", "Backup successful.")
            else:
                print("Backup canceled.")
        except subprocess.CalledProcessError as e:
            print(f"Error during backup: {e}")
            QMessageBox.warning(self, "Backup Error", f"Error during backup: {e}")

    def handle_restore(self):
        try:
            # Prompt user to select the SQL backup file
            file_dialog = QFileDialog()
            dump_file_path, _ = file_dialog.getOpenFileName(self, "Select Backup File", "", "SQL Files (*.sql)")

            if dump_file_path:
                # Replace with your actual MySQL username, password, and database name
                username = "root"
                password = "12345"
                database_name = "softeng"

                # Formulate the MySQL restore command
                restore_command = [
                    'mysql',
                    '--host=localhost',
                    '--user=' + username,
                    '--password=' + password,
                    database_name,
                    '-e',
                    'source ' + dump_file_path
                ]

                # Execute the MySQL restore command using subprocess
                subprocess.run(restore_command, check=True)
                QMessageBox.information(self, "Restore Successful", "Database restore completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error during restore: {e}")
            QMessageBox.critical(self, "Restore Error", f"Failed to restore database:\n{str(e)}")
        except Exception as ex:
            print(f"Unexpected error during restore: {ex}")
            QMessageBox.critical(self, "Restore Error", f"Unexpected error during restore:\n{str(ex)}")