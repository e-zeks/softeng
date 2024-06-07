import mysql.connector
from mysql.connector import Error

from screens import startupUI
from screens import startup_func


#Read and write from DB
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345",
            database="softeng"
        )
        if conn.is_connected():
            print("Connected to MySQL database")
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    MainWindow = startupUI.MainWindow()
    MainWindow.show()
    startupUI.connect_functions(MainWindow, startup_func)
    sys.exit(app.exec_())