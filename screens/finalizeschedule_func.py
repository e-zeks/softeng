from PyQt5.QtCore import QTime, Qt, pyqtSignal
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from screens.finalizescheduleUI import Ui_MainWindow

class FinalizeSchedWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    confirm_button = QtCore.pyqtSignal(dict)

    def __init__(self):
        super(FinalizeSchedWindow, self).__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.button_clicked)
        self.confirm.clicked.connect(self.handle_confirm)

        # Set the time constraints
        min_time = QTime(7, 0)  # 7:00 AM
        max_time = QTime(18, 0)  # 6:00 PM

        self.sunstart.setMinimumTime(min_time)
        self.sunstart.setMaximumTime(max_time)
        self.monstart.setMinimumTime(min_time)
        self.monstart.setMaximumTime(max_time)
        self.tuesstart.setMinimumTime(min_time)
        self.tuesstart.setMaximumTime(max_time)
        self.wedstart.setMinimumTime(min_time)
        self.wedstart.setMaximumTime(max_time)
        self.thursstart.setMinimumTime(min_time)
        self.thursstart.setMaximumTime(max_time)
        self.fristart.setMinimumTime(min_time)
        self.fristart.setMaximumTime(max_time)
        self.satstart.setMinimumTime(min_time)
        self.satstart.setMaximumTime(max_time)

        self.sunend.setTime(self.sunstart.time().addSecs(3600))
        self.monend.setTime(self.monstart.time().addSecs(3600))
        self.tuesend.setTime(self.tuesstart.time().addSecs(3600))
        self.wedend.setTime(self.wedstart.time().addSecs(3600))
        self.thursend.setTime(self.thursstart.time().addSecs(3600))
        self.fridayend.setTime(self.fristart.time().addSecs(3600))
        self.satend.setTime(self.satstart.time().addSecs(3600))

        self.sunstart.timeChanged.connect(lambda time: self.updateEndTime(self.sunstart, self.sunend))
        self.monstart.timeChanged.connect(lambda time: self.updateEndTime(self.monstart, self.monend))
        self.tuesstart.timeChanged.connect(lambda time: self.updateEndTime(self.tuesstart, self.tuesend))
        self.wedstart.timeChanged.connect(lambda time: self.updateEndTime(self.wedstart, self.wedend))
        self.thursstart.timeChanged.connect(lambda time: self.updateEndTime(self.thursstart, self.thursend))
        self.fristart.timeChanged.connect(lambda time: self.updateEndTime(self.fristart, self.fridayend))
        self.satstart.timeChanged.connect(lambda time: self.updateEndTime(self.satstart, self.satend))

    def button_clicked(self):
        self.back_button.emit()

    def handle_confirm(self):
        schedule_details = self.get_sched_details()
        print("Finalized Schedule:", schedule_details)
        self.confirm_button.emit(schedule_details)

    def updateEndTime(self, start_widget, end_widget):
        new_end_time = start_widget.time().addSecs(3600)
        end_widget.setTime(new_end_time)
        end_widget.setEnabled(False)

    def get_sched_details(self):
        schedule = {}

        if self.sunday.isChecked():
            schedule['Sunday'] = {
                'start': self.sunstart.time().toString(Qt.DefaultLocaleShortDate),
                'end': self.sunend.time().toString(Qt.DefaultLocaleShortDate)
            }
        if self.monday.isChecked():
            schedule['Monday'] = {
                'start': self.monstart.time().toString(Qt.DefaultLocaleShortDate),
                'end': self.monend.time().toString(Qt.DefaultLocaleShortDate)
            }
        if self.tuesday.isChecked():
            schedule['Tuesday'] = {
                'start': self.tuesstart.time().toString(Qt.DefaultLocaleShortDate),
                'end': self.tuesend.time().toString(Qt.DefaultLocaleShortDate)
            }
        if self.wednesday.isChecked():
            schedule['Wednesday'] = {
                'start': self.wedstart.time().toString(Qt.DefaultLocaleShortDate),
                'end': self.wedend.time().toString(Qt.DefaultLocaleShortDate)
            }
        if self.thursday.isChecked():
            schedule['Thursday'] = {
                'start': self.thursstart.time().toString(Qt.DefaultLocaleShortDate),
                'end': self.thursend.time().toString(Qt.DefaultLocaleShortDate)
            }
        if self.friday.isChecked():
            schedule['Friday'] = {
                'start': self.fristart.time().toString(Qt.DefaultLocaleShortDate),
                'end': self.fridayend.time().toString(Qt.DefaultLocaleShortDate)
            }
        if self.saturday.isChecked():
            schedule['Saturday'] = {
                'start': self.satstart.time().toString(Qt.DefaultLocaleShortDate),
                'end': self.satend.time().toString(Qt.DefaultLocaleShortDate)
            }

        return schedule
