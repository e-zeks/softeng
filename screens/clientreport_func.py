from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog, QMessageBox
from screens.clientreportUI import Ui_MainWindow
import mysql.connector
import csv
from datetime import datetime

class ClientReportWindow(QMainWindow, Ui_MainWindow):
    # Signals for button actions
    save_button = QtCore.pyqtSignal()
    back_button = QtCore.pyqtSignal()
    getdata_button = QtCore.pyqtSignal()
    logout_button = QtCore.pyqtSignal()
    help_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(ClientReportWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn  # Store the database connection

        # Connect UI signals to methods
        self.savetodesktop.clicked.connect(self.generate_report)
        self.back.clicked.connect(self.backbutton_clicked)
        self.getdata.clicked.connect(self.getdatabutton_clicked)
        self.logout.clicked.connect(self.logoutbutton_clicked)
        self.help.clicked.connect(self.handle_help)

        # Initialize table
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
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(results))

        # Set the column headers
        self.tableWidget.setHorizontalHeaderLabels(column_names)

        for row_number, row_data in enumerate(results):
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

    def disable_editing(self):
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)

    def generate_report(self):
        # Get report name and current month
        report_name = self.reportname.toPlainText().strip()
        current_month = self.currentmonth.currentText()

        if not report_name:
            QMessageBox.warning(self, "Warning", "Please enter a report name.")
            return

        # Generate filename with current date, selected month, and report name
        current_date = datetime.now().strftime('%Y-%m-%d')
        filename = f"{current_date}_{current_month}_{report_name}.csv"

        # Open file dialog to save the report
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Report", "", "CSV Files (*.csv)")

        if file_path:
            try:
                with open(file_path, mode='w', newline='') as file:
                    writer = csv.writer(file)

                    # Write metadata or header with date and report name
                    writer.writerow(["Date:", current_date])
                    writer.writerow(["Report Name:", report_name])
                    writer.writerow(["Month:", current_month])
                    writer.writerow([])  # Empty line for separation

                    # Write table headers
                    headers = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(self.tableWidget.columnCount())]
                    writer.writerow(headers)

                    # Write table data
                    for row in range(self.tableWidget.rowCount()):
                        row_data = []
                        for column in range(self.tableWidget.columnCount()):
                            item = self.tableWidget.item(row, column)
                            if item is not None:
                                row_data.append(item.text())
                            else:
                                row_data.append("")
                        writer.writerow(row_data)

                QMessageBox.information(self, "Success", f"Report saved successfully as {filename}")
                self.save_button.emit()

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error saving report: {str(e)}")

    def backbutton_clicked(self):
        print("Back")
        self.back_button.emit()

    def getdatabutton_clicked(self):
        print("Got data")
        self.getdata_button.emit()

    def logoutbutton_clicked(self):
        print("Logging Out")
        self.logout_button.emit()

    def handle_help(self):
        self.help_button.emit()
