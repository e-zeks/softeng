import mysql.connector
import sys
import os
from PyQt5.QtWidgets import QApplication

#Database connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="softeng"
    )

#db connection check
if conn.is_connected():
    print("Connected to MySQL database")

#Folder Directory
ui_directory = os.path.join(os.path.dirname(__file__), 'ui')
sys.path.append(ui_directory)

from startup import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

