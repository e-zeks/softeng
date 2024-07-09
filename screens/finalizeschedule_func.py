from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore
from screens.finalizescheduleUI import Ui_MainWindow
from mysql.connector import Error

class FinalizeSchedWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    confirm_button = QtCore.pyqtSignal(dict)

    def __init__(self, conn):
        super(FinalizeSchedWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn
        self.selectedcoach = None
        self.days = None
        self.times = None

        self.back.clicked.connect(self.button_clicked)
        self.confirm.clicked.connect(self.handle_confirm)
        self.help.clicked.connect(self.handle_help)
        # Connect signals for updating end time comboboxes

        self.sunstart.currentIndexChanged.connect(self.updateEndTime)
        self.monstart.currentIndexChanged.connect(self.updateEndTime)
        self.tuesstart.currentIndexChanged.connect(self.updateEndTime)
        self.wedstart.currentIndexChanged.connect(self.updateEndTime)
        self.thursstart.currentIndexChanged.connect(self.updateEndTime)
        self.fristart.currentIndexChanged.connect(self.updateEndTime)
        self.satstart.currentIndexChanged.connect(self.updateEndTime)

        self.sunend.setDisabled(True)
        self.monend.setDisabled(True)
        self.tuesend.setDisabled(True)
        self.wedend.setDisabled(True)
        self.thursend.setDisabled(True)
        self.fridayend.setDisabled(True)
        self.satend.setDisabled(True)

    def set_selections(self, selectedcoach, selectedpackage):
        self.selectedcoach = selectedcoach

        if selectedpackage['package_name'] == 'Private Package':
            self.retrieve_start_times()
            print(f"COACH: {self.selectedcoach}, PACKAGE:{selectedpackage['package_name']}")

        print(f"COACH: {self.selectedcoach}, PACKAGE:{selectedpackage['package_name']}")

    def retrieve_start_times(self):
        try:
            with self.conn.cursor(dictionary=True) as cursor:
                query = """
                    SELECT s.Day, s.StartTime, b.BookingID, b.Package_Name
                    FROM sessions s
                    JOIN booking b ON s.BookingID = b.BookingID
                    WHERE s.Session_Counter > 0 AND b.Package_Name != 'Public Package'
                """
                cursor.execute(query)
                start_times = cursor.fetchall()

                # Separate days, times, BookingID, and Package_Name using a loop
                days = []
                times = []
                booking_ids = []
                package_names = []
                for start_time in start_times:
                    days.append(start_time['Day'])
                    times.append(start_time['StartTime'])
                    booking_ids.append(start_time['BookingID'])
                    package_names.append(start_time['Package_Name'])

                self.days = days
                self.times = times
                booking_ids = booking_ids
                package_names = package_names

                print("UNAVAILABLE START TIMES: ", start_times)
                print("Days: ", self.days)
                print("Start Times: ", self.times)
                print("Booking IDs: ", booking_ids)
                print("Package Names: ", package_names)

                self.disable_conflicts()

        except Error as e:
            print(f"Error executing query: {e}")

    def disable_conflicts(self):
        # Create a mapping of days to their respective comboboxes
        day_combobox_map = {
            'Sunday': self.sunstart,
            'Monday': self.monstart,
            'Tuesday': self.tuesstart,
            'Wednesday': self.wedstart,
            'Thursday': self.thursstart,
            'Friday': self.fristart,
            'Saturday': self.satstart
        }

        # Iterate over the days and times together
        for day, start_times in zip(self.days, self.times):
            if day in day_combobox_map:
                self.disable_items(day_combobox_map[day], start_times)

    def disable_items(self, combobox, items_to_disable):
        for index in range(combobox.count()):
            item_text = combobox.itemText(index)
            if item_text in items_to_disable:
                item = combobox.model().item(index)
                item.setFlags(item.flags() & ~Qt.ItemIsEnabled)

    def handle_help(self):
        pdf_path = "C:\\Users\\JC\\Desktop\\softeng-main\\Anytime Fitness User Manual.pdf"
        QDesktopServices.openUrl(QUrl.fromLocalFile(pdf_path))

    def updateEndTime(self):
        sender = self.sender()

        # Depending on the sender, update the corresponding end time combo box
        if sender == self.sunstart:
            current_index = self.sunstart.currentIndex()
            self.sunend.setCurrentIndex(current_index + 1)
        elif sender == self.monstart:
            current_index = self.monstart.currentIndex()
            self.monend.setCurrentIndex(current_index + 1)
        elif sender == self.tuesstart:
            current_index = self.tuesstart.currentIndex()
            self.tuesend.setCurrentIndex(current_index + 1)
        elif sender == self.wedstart:
            current_index = self.wedstart.currentIndex()
            self.wedend.setCurrentIndex(current_index + 1)
        elif sender == self.thursstart:
            current_index = self.thursstart.currentIndex()
            self.thursend.setCurrentIndex(current_index + 1)
        elif sender == self.fristart:
            current_index = self.fristart.currentIndex()
            self.fridayend.setCurrentIndex(current_index + 1)
        elif sender == self.satstart:
            current_index = self.satstart.currentIndex()
            self.satend.setCurrentIndex(current_index + 1)
    def button_clicked(self):
        self.back_button.emit()

    def handle_confirm(self):
        schedule_details = self.get_sched_details()
        if schedule_details is not None:  # Check if schedule_details is not None
            print("Finalized Schedule:", schedule_details)
            self.confirm_button.emit(schedule_details)

    def get_sched_details(self):
        schedule = {}

        if self.sunday.isChecked():
            start_time = self.sunstart.currentText()
            end_time = self.sunend.currentText()
            if not start_time or not end_time:
                self.showTimeSelectionError('Sunday')
                return None
            schedule['Sunday'] = {
                'start': start_time,
                'end': end_time
            }
        if self.monday.isChecked():
            start_time = self.monstart.currentText()
            end_time = self.monend.currentText()
            if not start_time or not end_time:
                self.showTimeSelectionError('Monday')
                return None
            schedule['Monday'] = {
                'start': start_time,
                'end': end_time
            }
        if self.tuesday.isChecked():
            start_time = self.tuesstart.currentText()
            end_time = self.tuesend.currentText()
            if not start_time or not end_time:
                self.showTimeSelectionError('Tuesday')
                return None
            schedule['Tuesday'] = {
                'start': start_time,
                'end': end_time
            }
        if self.wednesday.isChecked():
            start_time = self.wedstart.currentText()
            end_time = self.wedend.currentText()
            if not start_time or not end_time:
                self.showTimeSelectionError('Wednesday')
                return None
            schedule['Wednesday'] = {
                'start': start_time,
                'end': end_time
            }
        if self.thursday.isChecked():
            start_time = self.thursstart.currentText()
            end_time = self.thursend.currentText()
            if not start_time or not end_time:
                self.showTimeSelectionError('Thursday')
                return None
            schedule['Thursday'] = {
                'start': start_time,
                'end': end_time
            }
        if self.friday.isChecked():
            start_time = self.fristart.currentText()
            end_time = self.fridayend.currentText()
            if not start_time or not end_time:
                self.showTimeSelectionError('Friday')
                return None
            schedule['Friday'] = {
                'start': start_time,
                'end': end_time
            }
        if self.saturday.isChecked():
            start_time = self.satstart.currentText()
            end_time = self.satend.currentText()
            if not start_time or not end_time:
                self.showTimeSelectionError('Saturday')
                return None
            schedule['Saturday'] = {
                'start': start_time,
                'end': end_time
            }

        return schedule

    def showTimeSelectionError(self, day):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(f"Please select start and end times for {day}.")
        msg.setWindowTitle("Time Selection Error")
        msg.setStandardButtons(QMessageBox.Ok)  # Set standard button(s)
        msg.exec_()

    def clearSelections(self):
        # Clear all checkbox selections
        self.sunday.setChecked(False)
        self.monday.setChecked(False)
        self.tuesday.setChecked(False)
        self.wednesday.setChecked(False)
        self.thursday.setChecked(False)
        self.friday.setChecked(False)
        self.saturday.setChecked(False)

        # Reset all combobox selections
        self.sunstart.setCurrentIndex(0)
        self.sunend.setCurrentIndex(0)
        self.monstart.setCurrentIndex(0)
        self.monend.setCurrentIndex(0)
        self.tuesstart.setCurrentIndex(0)
        self.tuesend.setCurrentIndex(0)
        self.wedstart.setCurrentIndex(0)
        self.wedend.setCurrentIndex(0)
        self.thursstart.setCurrentIndex(0)
        self.thursend.setCurrentIndex(0)
        self.fristart.setCurrentIndex(0)
        self.fridayend.setCurrentIndex(0)
        self.satstart.setCurrentIndex(0)
        self.satend.setCurrentIndex(0)