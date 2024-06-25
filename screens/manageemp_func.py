from mysql.connector import Error
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QMainWindow
from screens.manageempUI import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets


class ManageEmpWindow(QMainWindow, Ui_MainWindow):
    logout_button = QtCore.pyqtSignal()
    back_button = QtCore.pyqtSignal()
    edit_button = QtCore.pyqtSignal(dict)
    clientmanage_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(ManageEmpWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn
        self.emp_details = {}

        self.logout.clicked.connect(self.handle_logout)
        self.back.clicked.connect(self.handle_back)
        self.clients.clicked.connect(self.handle_clients)
        self.edit.clicked.connect(self.handle_edit)

        self.search_bar.textChanged.connect(self.search_table)  # search in table
        self.table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)  # Enable row selection
        self.table.itemSelectionChanged.connect(self.handle_row_selection)  # Connect the selection signal to the slot

    def refresh_data(self):
        self.table.clearContents()
        self.set_tableElements()
        self.disable_editing()

    def load_data(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM employees")
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

    def handle_logout(self):
        print("Logging Out")
        self.logout_button.emit()

    def handle_back(self):
        self.back_button.emit()

    def handle_clients(self):
        self.clientmanage_button.emit()

    def handle_row_selection(self):
        selected_items = self.table.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            column_names = ["EmployeeID", "Last_Name", "First_Name", "Username", "LOA", "Contact_Number", "Email"]
            emp_details = {}
            table_headers = [self.table.horizontalHeaderItem(i).text() for i in range(self.table.columnCount())]
            for column_name in column_names:
                if column_name in table_headers:
                    column_index = table_headers.index(column_name)
                    item = self.table.item(row, column_index)
                    if item:
                        emp_details[column_name] = item.text()

            self.emp_details = emp_details  # Store the details in the instance attribute

    def handle_edit(self):
        print(f"Selected Row Data: {self.emp_details}")
        self.edit_button.emit(self.emp_details)