# from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
# from PyQt5 import QtCore
# from mysql.connector import Error
# from screens.manageempUI import Ui_MainWindow  # Import the Ui_MainWindow class from manageempUI
#
# class ManageEmpWindow(QMainWindow):
#     back_button = QtCore.pyqtSignal()
#
#     def __init__(self):
#         super(ManageEmpWindow, self).__init__()
#         #self.conn = conn
#         self.ui = Ui_MainWindow()  # Initialize the UI class
#         self.ui.setupUi(self)  # Setup the UI
#
#         # Connect UI signals/slots
#         self.ui.employees.clicked.connect(self.load_data)
#         # Connect other buttons similarly
#
#         # Example of connecting a button from Ui_MainWindow
#         #self.ui.clear_button.clicked.connect(self.clear_text_fields)
#
#     def load_data(self):
#         if self.conn is None:
#             print("Failed to connect to the database.")
#             return
#
#         cursor = self.conn.cursor()
#
#         try:
#             cursor.execute("SELECT * FROM employees")
#             rows = cursor.fetchall()
#
#             column_names = [description[0] for description in cursor.description]
#
#             self.ui.tableWidget.setRowCount(len(rows))
#             self.ui.tableWidget.setColumnCount(len(column_names))
#             self.ui.tableWidget.setHorizontalHeaderLabels(column_names)
#
#             for row_idx, row in enumerate(rows):
#                 for col_idx, item in enumerate(row):
#                     self.ui.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))
#
#         except Error as e:
#             print(f"Error: {e}")
#
#         finally:
#             cursor.close()
#             self.conn.close()
#
#     def clear_text_fields(self):
#         # Implement clear_text_fields if needed
#         pass
