from PyQt5 import QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from screens.coachhomeUI import Ui_MainWindow
from mysql.connector import Error

class CoachHomeWindow(QMainWindow, Ui_MainWindow):
    logout_button = QtCore.pyqtSignal()
    schedule_button = QtCore.pyqtSignal()
    clients_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(CoachHomeWindow, self).__init__()
        self.conn = conn
        self.log_ids = []
        self.setupUi(self)
        self.logout.clicked.connect(self.handle_logout)
        self.schedule.clicked.connect(self.handle_schedule)
        self.clients.clicked.connect(self.handle_clients)
        self.help.clicked.connect(self.handle_help)

    def handle_help(self):
        pdf_path = "C:\\Users\\JC\\Desktop\\softeng-main\\Anytime Fitness User Manual.pdf"
        QDesktopServices.openUrl(QUrl.fromLocalFile(pdf_path))


    def log_user_logout(self):
        cursor = self.conn.cursor()
        print(f"Logging out users with LogIDs: {self.log_ids}")  # Debug print

        sql = " SELECT COUNT(*) FROM user_logs"
        cursor.execute(sql)
        lastrow = cursor.fetchone()[0]
        print(lastrow)
        if not self.log_ids:
            print("No log IDs to log out")  # Debug print
        try:
            print("ttest")
            # this gets the last row and adds date
            query = """
                       UPDATE user_logs
                       SET Logout_Time = NOW()
                       WHERE LogID = %s AND Logout_Time IS NULL
                   """
            cursor.execute(query, (lastrow,))
            self.conn.commit()
            print("Logout times updated successfully")  # Debug print
        except Error as e:
            print(f"Error logging user logout: {e}")
        finally:
            cursor.close()
            self.log_ids.clear()  # Clear the list of LogIDs after logging out

    def handle_logout(self):
        self.log_user_logout()
        self.logout_button.emit()

    def handle_schedule(self):
        self.schedule_button.emit()

    def handle_clients(self):
        self.clients_button.emit()
