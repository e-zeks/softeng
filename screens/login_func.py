from mysql.connector import Error
from PyQt5 import QtWidgets
from . import forgotpassUI
from . import adminhomeUI

# Function to fetch login data
def fetch_login_data(conn):
    if conn is None:
        return []
    try:
        with conn.cursor() as cursor:
            query = "SELECT Username, Password, LOA FROM employees"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
    except Error as e:
        print(f"Error: {e}")
        return []

# Function to handle login
def handle_login(conn, username, password, main_window):
    login_data = fetch_login_data(conn)
    for db_username, db_password, db_loa in login_data:
        if username == db_username and password == db_password:
            print("Log in successful")
            if db_loa == 'Admin':
                try:
                    main_window.close()
                    adminhome_window = QtWidgets.QMainWindow()

                    ui = adminhomeUI.Ui_MainWindow()
                    ui.setupUi(adminhome_window, login_window=main_window)

                    adminhome_window.show()

                    main_window.adminhome_window = adminhome_window
                except Exception as e:
                    print(f"Exception occurred: {e}")
            elif db_loa == 'Coach':
                print("coach screen")
            elif db_loa == 'Auditor':
                print("auditor screen")
            elif db_loa == 'Client':
                print("client screen")
            return True
    print("Login failed")
    return False

#forgot password button
def handle_forgot(main_window):
    try:
        main_window.close()
        forgotpass_window = QtWidgets.QMainWindow()

        ui = forgotpassUI.Ui_MainWindow()
        ui.setupUi(forgotpass_window, login_window=main_window)

        forgotpass_window.show()

        main_window.forgotpass_window = forgotpass_window
    except Exception as e:
        print(f"Exception occurred: {e}")

def handle_back(current_window, startup_window):
    current_window.close()
    startup_window.show()