from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog, QMessageBox
from screens.transactionreportUI import Ui_MainWindow
import mysql.connector
import csv
from datetime import datetime

class TransactionReportWindow(QMainWindow, Ui_MainWindow):
    # Signals for button actions
    save_button = QtCore.pyqtSignal()
    back_button = QtCore.pyqtSignal()
    logout_button = QtCore.pyqtSignal()
    help_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(TransactionReportWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn  # Store the database connection

        # Connect UI signals to methods
        self.savetodesktop.clicked.connect(self.generate_report)
        self.back.clicked.connect(self.backbutton_clicked)
        self.logout.clicked.connect(self.logoutbutton_clicked)
        self.help.clicked.connect(self.handle_help)

        # Initialize table
        self.set_tableElements()
        self.disable_editing()

    def load_data(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM transactions_report")
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

        # Set font and background color for the table
        font = QtGui.QFont("Arial Black", 14)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: white;")

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

        # Get additional metadata
        company_name = "Anytime Fitness - The Garden Walk"  # Replace with actual company name
        address = "105 Felix Ave, Santo Domingo, Cainta, 1900 Rizal"  # Replace with actual address
        contact_details = "0926 679 1189"  # Replace with actual contact details
        report_title = self.reportname.toPlainText().strip()  # Use the reportname QTextEdit for the report title
        created_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        report_creator = "Report Creator"  # Replace with actual report creator

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
                    writer.writerow(["Name of Company:", company_name])
                    writer.writerow(["Address:", address])
                    writer.writerow(["Contact Details:", contact_details])
                    writer.writerow(["Title of Report:", report_title])
                    writer.writerow(["Date and Time Created:", created_datetime])
                    writer.writerow(["Report Creator:", report_creator])
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

    def logoutbutton_clicked(self):
        print("Logging Out")
        self.logout_button.emit()

    def handle_help(self):
        self.help_button.emit()

    def generate_report(self):
        # Get report name and current month
        report_name = self.reportname.toPlainText().strip()
        current_month = self.currentmonth.currentText()

        if not report_name:
            QMessageBox.warning(self, "Warning", "Please enter a report name.")
            return

        # Get additional metadata
        company_name = "Anytime Fitness - The Garden Walk"  # Replace with actual company name
        address = "105 Felix Ave, Santo Domingo, Cainta, 1900 Rizal"  # Replace with actual address
        contact_details = "0926 679 1189"  # Replace with actual contact details
        report_title = self.reportname.toPlainText().strip()  # Use the reportname QTextEdit for the report title
        created_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Fetch report creator (assuming you have user details in your database)
        report_creator = self.fetch_report_creator()  # Replace with actual method to fetch user's first name and last name

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
                    writer.writerow(["Name of Company:", company_name])
                    writer.writerow(["Address:", address])
                    writer.writerow(["Contact Details:", contact_details])
                    writer.writerow(["Title of Report:", report_title])
                    writer.writerow(["Date and Time Created:", created_datetime])
                    writer.writerow(["Report Creator:", report_creator])
                    writer.writerow(["Month:", current_month])
                    writer.writerow([])  # Empty line for separation

                    # Write table headers
                    headers = [self.tableWidget.horizontalHeaderItem(i).text() for i in
                               range(self.tableWidget.columnCount())]
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

    def fetch_report_creator(self):
        # Assuming you have a method to fetch the logged-in user's first name and last name from the database
        # Replace with actual query and logic to fetch user's name
        user_id = 3  # Replace with actual user ID or identifier of the logged-in user
        cursor = self.conn.cursor()
        cursor.execute("SELECT first_name, last_name FROM employees WHERE EmployeeID = %s", (user_id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            first_name, last_name = result
            return f"{first_name} {last_name}"
        else:
            return "Unknown User"  # Handle if no user found or default value
