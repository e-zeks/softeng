from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.finalselectionUI import Ui_MainWindow

class FinalSelectionWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()

    def __init__(self):
        super(FinalSelectionWindow, self).__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.back_button.emit()

    def set_details(self, client_details, coach_details, package_details, session_count):
        try:
            print("Setting details in final selection screen")
            print("Client Details:", client_details)
            print("Coach Details:", coach_details)
            print("Package Details:", package_details)
            print("Session Count:", session_count)

            self.coachline.setText(coach_details['full_name'])

            client_details = list(client_details)
            self.programplanline.setText(client_details[2])
            self.packageline.setText(package_details['package_name'])
            self.numberofsessionsline.setText(str(session_count))

            package_details['package_price'] += ((package_details['min_sessions'] - session_count) * 500) + package_details['package_price']

            self.totalamtline.setText(str(package_details['package_price']))

        except Exception as e:
            print(f"Error setting details: {e}")
