from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QMainWindow
from screens.manageclientUI import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
from mysql.connector import Error

class ManageClientWindow(QMainWindow, Ui_MainWindow):
    #screen buttons
    back_button = QtCore.pyqtSignal()
    edit_button = QtCore.pyqtSignal(dict)

    #nav bar buttons
    employeemanage_button = QtCore.pyqtSignal()
    payments_button = QtCore.pyqtSignal()
    reports_button = QtCore.pyqtSignal()
    userlogs_button = QtCore.pyqtSignal()
    maintenance_button = QtCore.pyqtSignal()
    help_button = QtCore.pyqtSignal()
    logout_button = QtCore.pyqtSignal()
    sms_button =  QtCore.pyqtSignal()

    def __init__(self, conn):
        super(ManageClientWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn
        self.client_details = {}  # To store selected client details

        self.current_user_id = 1  # Store the current user's ID
        self.current_user_type = 'Admin'  # Store the current user's type as a string


        #screen buttons
        self.back.clicked.connect(self.handle_back)
        self.edit.clicked.connect(self.handle_edit)

        #nav bar buttons
        self.employees.clicked.connect(self.handle_employees)
        self.payments.clicked.connect(self.handle_payments)
        self.report.clicked.connect(self.handle_reports)
        self.userlogs.clicked.connect(self.handle_userlogs)
        self.maintenance.clicked.connect(self.handle_maintenance)
        self.help.clicked.connect(self.handle_help)
        self.logout.clicked.connect(self.handle_logout)

        self.search_bar.textChanged.connect(self.search_table)  # search in table
        self.table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)  # Enable row selection
        self.table.itemSelectionChanged.connect(self.handle_row_selections)  # Connect the selection signal to the slot

        self.sms.clicked.connect(self.handle_sms)

    def refresh_data(self):
        self.table.clearContents()
        self.set_tableElements()
        self.disable_editing()

    def load_data(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM clients")
        results = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        cursor.close()
        return results, column_names

    def set_tableElements(self):
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

    def disable_editing(self):
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item:
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)

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

    def handle_row_selections(self):
        selected_items = self.table.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            column_names = ["ClientID", "Last_Name", "First_Name", "Address", "Birthdate",
                            "Contact_Number", "Email", "Username", "Password", "Program_Plan", "Conditions"]
            client_details = {}
            table_headers = [self.table.horizontalHeaderItem(i).text() for i in range(self.table.columnCount())]
            for column_name in column_names:
                if column_name in table_headers:
                    column_index = table_headers.index(column_name)
                    item = self.table.item(row, column_index)
                    if item:
                        client_details[column_name] = item.text()

            self.client_details = client_details  # Store the details in the instance attribute

    def handle_edit(self):
        print(f"Selected Row Data: {self.client_details}")
        self.edit_button.emit(self.client_details)

    def handle_back(self):
        self.back_button.emit()

    #nav bar buttons
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

    def handle_sms(self):
        self.sms_button.emit()

    def handle_logout(self):
        print("Logging Out User")
        self.log_user_logout()
        self.logout_button.emit()