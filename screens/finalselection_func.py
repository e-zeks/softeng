from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.finalselectionUI import Ui_MainWindow

class FinalSelectionWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    proceed_button = QtCore.pyqtSignal()

    def __init__(self):
        super(FinalSelectionWindow, self).__init__()
        self.setupUi(self)
        self.initial_package_price = 0  # Store initial package price

        self.back.clicked.connect(self.button_clicked)
        self.proceed.clicked.connect(self.handle_proceed)

    def button_clicked(self):
        self.back_button.emit()

    def handle_proceed(self):
        self.proceed_button.emit()

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

            # Calculate the additional cost for the sessions correctly
            additional_sessions = session_count - package_details['min_sessions']
            additional_cost = additional_sessions * 500

            # Calculate total amount
            total_amount = package_details['package_price'] + additional_cost

            self.totalamtline.setText(str(total_amount))

        except Exception as e:
            print(f"Error setting details: {e}")
