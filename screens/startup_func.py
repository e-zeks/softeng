from PyQt5 import QtWidgets
from . import loginUI
def handle_guest():
    print("Guest")

def handle_login(main_window):
    main_window.close()
    login_window = QtWidgets.QMainWindow()

    ui = loginUI.Ui_MainWindow()
    ui.setupUi(login_window)

    login_window.show()

    main_window.login_window = login_window

def handle_register():
    print("Register")
