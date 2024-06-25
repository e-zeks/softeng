from mysql.connector import Error
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QMainWindow
from screens.manageempUI import Ui_MainWindow
from PyQt5 import QtCore

class ManageEmpWindow(QMainWindow, Ui_MainWindow):
    logout_button = QtCore.pyqtSignal()
    clientmanage_button = QtCore.pyqtSignal()
    def __init__(self, conn):
        super(ManageEmpWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn

        #self.db = dbconnect('Admin', 'Admin123')
        self.set_tableElements()
        self.disable_editing()
        self.back.clicked.connect(self.disable_editing)
        self.edit.clicked.connect(self.enable_editing)
        self.save.clicked.connect(self.save_data)
        self.search_bar.textChanged.connect(self.search_table)

        self.clients.clicked.connect(self.handle_clients)
        self.logout.clicked.connect(self.button_clicked)

    def load_data(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM employees")
        results = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        cursor.close()
        return results, column_names

    def set_tableElements(self):
        results, column_names = self.load_data()
        print(f"Column Names: {column_names}")  # Debug print
        print(f"Results: {results}")  # Debug print
        self.table.setColumnCount(len(column_names))
        self.table.setRowCount(len(results))

        # Set the column headers
        self.table.setHorizontalHeaderLabels(column_names)

        for row_number, row_data in enumerate(results):
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        pass

        self.table.resizeColumnsToContents()

        # Optionally, you can set the stretch last section property to ensure the last column expands to fill the remaining space
        self.table.horizontalHeader().setStretchLastSection(True)

    def enable_editing(self):
        for row in range(self.table.rowCount()):
            for column in range(self.table.columnCount()):
                item = self.table.item(row, column)
                if item:
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)

    def disable_editing(self):
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item:
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)

    def save_data(self):
        try:
            cursor = self.conn.cursor()

            for row in range(self.table.rowCount()):
                row_data = []
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)
                    if item:
                        row_data.append(item.text())
                    else:
                        row_data.append('')

                primary_key_value = row_data[0]
                update_query = "UPDATE employees SET "
                update_query += ", ".join([f"{self.table.horizontalHeaderItem(col).text()} = %s" for col in
                                           range(1, self.table.columnCount())])
                update_query += " WHERE EmployeeID = %s"

                update_values = row_data[1:] + [primary_key_value]
                print(f"Executing query: {update_query} with values {update_values}")
                cursor.execute(update_query, update_values)

            self.conn.commit()
            QMessageBox.information(None, "Success", "Changes saved to the database successfully!")

        except Error as e:
            print(f"Error: {e}")
            QMessageBox.critical(None, "Error", f"Failed to save changes: {e}")

        finally:
            if cursor:
                cursor.close()
            # No need to close self.db.conn here as it should be managed by your dbconnect class

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

    def button_clicked(self):
        print("Logging Out")
        self.logout_button.emit()

    def handle_clients(self):
        self.clientmanage_button.emit()