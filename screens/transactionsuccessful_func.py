from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.transactionsuccessfulUI import Ui_MainWindow

class TransactionSuccessfulWindow(QMainWindow, Ui_MainWindow):
    confirm_button = QtCore.pyqtSignal()

    def __init__(self):
        super(TransactionSuccessfulWindow, self).__init__()
        self.setupUi(self)

        # Connect confirm button signal
        self.confirm.clicked.connect(self.handle_confirm)

    def populate_fields(self, clientdetails, selectedcoach, selectedpackage, sessioncount, selectedsched):
        # Populate line edits with data
        print(clientdetails, selectedcoach, selectedpackage, sessioncount, selectedsched)


        self.coachline.setText(selectedcoach['full_name'])

        client_details = list(clientdetails)
        self.programplanline.setText(client_details[2])
        self.packageline.setText(selectedpackage['package_name'])
        self.numberofsessionsline.setText(str(sessioncount))
        self.totalamtline.setText(str(selectedpackage['package_price']))  # Assuming Package_Price is per session

        # Populate selected schedules
        self.populate_selected_schedules(selectedsched)
        print("debug5")

    def populate_selected_schedules(self, selectedsched):
        # Assuming selectedsched is a dictionary containing session dates and times
        schedule_texts = []
        for day, time in selectedsched.items():
            schedule_texts.append(f"{day}: {time}")
        for i, text in enumerate(schedule_texts):
            if i < len(self.schedule_line_edits):
                self.schedule_line_edits[i].setText(text)

    def handle_confirm(self):
        self.confirm_button.emit()
