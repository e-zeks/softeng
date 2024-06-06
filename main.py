import mysql.connector
from screens import startupUI
from screens import startup_func

# Database connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="softeng"
)

# Database connection check
if conn.is_connected():
    print("Connected to MySQL database")

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    MainWindow = startupUI.MainWindow()
    MainWindow.show()
    startupUI.connect_functions(MainWindow, startup_func)
    sys.exit(app.exec_())