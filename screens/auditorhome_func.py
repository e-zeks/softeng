from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from screens.auditorhomeUI import Ui_MainWindow
from mysql.connector import Error

class AuditorHomeWindow(QMainWindow, Ui_MainWindow):
    logout_button = QtCore.pyqtSignal()
    clientreport_button = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(AuditorHomeWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn
        self.log_ids = []

        self.clients.clicked.connect(self.handle_clientreport)
        self.logout.clicked.connect(self.handle_logout)

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
    def handle_clientreport(self):
        self.clientreport_button.emit()

    def handle_logout(self):
        self.log_user_logout()
        self.logout_button.emit()