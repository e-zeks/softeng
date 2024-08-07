from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from mysql.connector import Error
from screens.userlogsUI import Ui_MainWindow

class UserLogsWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()

    # nav bar buttons
    employeemanage_button = QtCore.pyqtSignal()
    clientmanage_button = QtCore.pyqtSignal()
    payments_button = QtCore.pyqtSignal()
    reports_button = QtCore.pyqtSignal()
    maintenance_button = QtCore.pyqtSignal()
    help_button = QtCore.pyqtSignal()
    logout_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(UserLogsWindow, self).__init__()
        self.conn = conn
        self.current_user_id = 1  # Store the current user's ID
        self.current_user_type = 'Admin'  # Store the current user's type as a string
        self.setupUi(self)

        self.set_table_elements()
        self.search_bar.textChanged.connect(self.search_table)

        self.back.clicked.connect(self.handle_back)

        # nav bar button
        self.employees.clicked.connect(self.handle_employees)
        self.clients.clicked.connect(self.handle_clients)
        self.payments.clicked.connect(self.handle_payments)
        self.report.clicked.connect(self.handle_reports)
        self.maintenance.clicked.connect(self.handle_maintenance)
        self.help.clicked.connect(self.handle_help)
        self.logout.clicked.connect(self.handle_logout)

    def refresh_data(self):
        self.table.clearContents()
        self.set_table_elements()
        self.disable_editing()

    def log_user_login(self, user_id, user_type, last_name, first_name):
        print("Logging user login data")
        try:
            cursor = self.conn.cursor()
            query = """
                INSERT INTO user_logs (EmployeeID, ClientID, UserType, Last_Name, First_Name, Login_Time)
                VALUES (%s, %s, %s, %s, %s, NOW())
            """
            if user_type == 'Employee':
                cursor.execute(query, (user_id, None, user_type, last_name, first_name))
            elif user_type == 'Client':
                cursor.execute(query, (None, user_id, user_type, last_name, first_name))
            self.conn.commit()
            self.current_user_id = user_id
            self.current_user_type = user_type
            print(f"User logged in with UserID: {user_id}, UserType: {user_type}")  # Debug print
        except Error as e:
            print(f"Error logging user login: {e}")
        finally:
            cursor.close()

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
    def load_data(self):
        print("load_data method called")  # Debug print
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM user_logs ORDER BY Login_Time DESC")
        results = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        cursor.close()
        return results, column_names

    def set_table_elements(self):
        results, column_names = self.load_data()
        self.table.setColumnCount(len(column_names))
        self.table.setRowCount(len(results))

        # Set the column headers
        self.table.setHorizontalHeaderLabels(column_names)

        for row_number, row_data in enumerate(results):
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setStretchLastSection(True)

    def search_table(self):
        search_text = self.search_bar.text().strip().lower()
        for row in range(self.table.rowCount()):
            row_visible = False
            for column in range(self.table.columnCount()):
                item = self.table.item(row, column)
                if item and search_text in item.text().lower():
                    row_visible = True
                    break  # Exit the loop once any match is found in the row

            self.table.setRowHidden(row, not row_visible)

    def disable_editing(self):
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item:
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)

    def handle_back(self):
        self.back_button.emit()

    # nav bar
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

    def handle_logout(self):
        print("Logging out user")  # Log the logout time
        self.log_user_logout()
        self.logout_button.emit()
