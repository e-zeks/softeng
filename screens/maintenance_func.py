import subprocess

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

    def __init__(self):
        super(MaintenanceWindow, self).__init__()
        self.setupUi(self)

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
        self.logout.clicked.connect(self.button_clicked)

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

    def button_clicked(self):
        print("Logging Out")
        self.logout_button.emit()


    def handle_backup(self):
        try:
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
                '--result-file=C:\\Users\\JC\\Desktop\\SQL backups\\softeng_backup.sql'
            ], check=True)
            print("Backup successful.")
            QMessageBox.information(self, "Backup", "Backup successful.")
        except subprocess.CalledProcessError as e:
            print(f"Error during backup: {e}")
            QMessageBox.warning(self, "Backup Error", f"Error during backup: {e}")

    def handle_restore(self):
        # Replace with your actual MySQL username, password, and database name
        username = "root"
        password = "12345"
        database_name = "softeng"

        # Prompt user to select the SQL backup file
        file_dialog = QFileDialog()
        dump_file_path, _ = file_dialog.getOpenFileName(self, "Select Backup File", "", "SQL Files (*.sql)")

        if dump_file_path:
            try:
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
                QMessageBox.critical(self, "Restore Error", f"Failed to restore database:\n{str(e)}")