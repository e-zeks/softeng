from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QMessageBox
from screens.specifictimeUI import Ui_MainWindow
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

class SpecificTimeWindow(QMainWindow, Ui_MainWindow):
    logout_button = QtCore.pyqtSignal()
    back_button = QtCore.pyqtSignal(dict)
    save_button = QtCore.pyqtSignal(dict)
    clients_button = QtCore.pyqtSignal(dict)

    screen_user = None

    def __init__(self, conn):
        super(SpecificTimeWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn

        self.back.clicked.connect(self.handle_back)
        self.logout.clicked.connect(self.handle_logout)
        self.clients.clicked.connect(self.handle_clients)
        self.help.clicked.connect(self.handle_help)
        self.save.clicked.connect(self.handle_save)
        self.comboBox.currentIndexChanged.connect(self.filter_sessions)

        self.sessions = []

    def set_user(self, current_user):
        self.screen_user = current_user
        print(current_user)

    def handle_back(self):
        print(self.details)
        #self.back_button.emit(self.details)
        self.back_button.emit(self.screen_user)

    def handle_logout(self):
        self.logout_button.emit()
        print("Logging out")

    def handle_clients(self):
        self.clients_button.emit(self.screen_user)

    def handle_help(self):
        pdf_path = "C:\\Users\\JC\\Desktop\\softeng-main\\Anytime Fitness User Manual.pdf"
        QDesktopServices.openUrl(QUrl.fromLocalFile(pdf_path))

    def handle_save(self):
        print("Saving...")
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Session Status")

        if not self.completed.isChecked() and not self.cancelled.isChecked():
            msg_box.setText("Please select either 'Completed' or 'Cancelled' before saving.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
            return

        if self.completed.isChecked():
            self.decrease_session_counter()
            msg_box.setText("Session marked as completed.")
            self.update_status()
            self.save_button.emit(self.screen_user)
        elif self.cancelled.isChecked():
            print("Cancelled")
            msg_box.setText("Session is marked as cancelled.")
            self.update_status()
            self.save_button.emit(self.screen_user)

        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def decrease_session_counter(self):
        try:
            with self.conn.cursor() as cursor:
                # Iterate through the details list to find booking IDs and decrease their session counters
                for i in range(1, len(self.details), 3):  # Start at index 1 and step by 3
                    booking_id = self.details[i]
                    sql = "UPDATE sessions SET Session_Counter = Session_Counter - 1 WHERE BookingID = %s"
                    cursor.execute(sql, (booking_id,))
                self.conn.commit()
                print(f"Session Counter decreased for BookingIDs {[self.details[i] for i in range(1, len(self.details), 3)]}")
        except Exception as e:
            print(f"Error updating Session Counter: {e}")

    def update_status(self):
        try:
            with self.conn.cursor() as cursor:
                # Query to update the Status column
                update_query = """
                    UPDATE sessions
                    SET Status = 'Completed'
                    WHERE Session_Counter = 0
                """
                cursor.execute(update_query)
                self.conn.commit()
                print("Status updated to 'Completed' for sessions with Session_Counter = 0")

        except Exception as e:
            print(f"Error updating Session Status: {e}")

    def update_date(self, formatted_date, sessions, details):
        self.date.setText(formatted_date)
        self.date.setDisabled(True)
        self.sessions = sessions
        self.details = details
        self.filter_sessions()

    def filter_sessions(self):
        selected_time = self.comboBox.currentText()
        filtered_sessions = [session for session in self.sessions if session[1] == selected_time]
        print(f"Filtered Sessions: {filtered_sessions}")  # Print filtered sessions for debugging
        self.add_textedits(filtered_sessions)
        print(selected_time)
        print(self.sessions)

    def add_textedits(self, sessions):
        layout_clients = self.widget_12.layout()
        layout_programs = self.widget_13.layout()

        print(f"Adding text edits for sessions: {sessions}")  # Print sessions for debugging

        self.clear_textedits()

        for client_name, program_plan in sessions:
            client_edit = QLineEdit(client_name)
            program_edit = QLineEdit(program_plan)

            self.apply_rounded_style(client_edit, "white", "#5e3b96")
            self.apply_rounded_style(program_edit, "#5e3b96", "white")

            client_edit.setFixedWidth(200)  # Adjust the width as needed
            program_edit.setFixedWidth(200)  # Adjust the width as needed

            layout_clients.addWidget(client_edit)
            layout_programs.addWidget(program_edit)

        print("Text edits added successfully.")  # Print success message

    def clear_textedits(self):
        layout_clients = self.widget_12.layout()
        layout_programs = self.widget_13.layout()

        while layout_clients.count() > 0:
            layout_clients.takeAt(0).widget().deleteLater()

        while layout_programs.count() > 0:
            layout_programs.takeAt(0).widget().deleteLater()

    def apply_rounded_style(self, widget, bg_color, text_color):
        widget.setStyleSheet(f"background-color: {bg_color}; color: {text_color}; border-radius: 10px;")
        font = QFont("Arial Black", 14)  # Adjust font family and size as per specifictimeUI.py
        widget.setFont(font)