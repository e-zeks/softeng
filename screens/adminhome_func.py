from PyQt5 import QtWidgets
from . import employeemanageUI

def handle_employees(main_window):
    try:
        main_window.close()
        employeemanage_window = QtWidgets.QMainWindow()

        ui = employeemanageUI.Ui_MainWindow()
        ui.setupUi(employeemanage_window)

        ui.load_data()

        employeemanage_window.show()

        main_window.employeemanage_window = employeemanage_window
    except Exception as e:
        print(f"Exception occurred: {e}")

def handle_logout(current_window, login_window):
    print("Log out successful")
    current_window.close()
    login_window.show()