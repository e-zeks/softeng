from PyQt5 import QtWidgets
from . import loginUI
from . import registerUI

def handle_guest():
    print("booking screen")

def handle_login(main_window):
    main_window.close()
    login_window = QtWidgets.QMainWindow()

    ui = loginUI.Ui_MainWindow()
    ui.setupUi(login_window)

    login_window.show()

    main_window.login_window = login_window

def handle_register(main_window):
    main_window.close()
    register_window = QtWidgets.QMainWindow()

    ui = registerUI.Ui_MainWindow()
    ui.setupUi(register_window)

    register_window.show()

    main_window.register_window = register_window
