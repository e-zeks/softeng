from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLineEdit
from screens.coachscheduleUI import Ui_MainWindow
from mysql.connector import Error
import datetime
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

class CoachScheduleWindow(QMainWindow, Ui_MainWindow):
    logout_button = QtCore.pyqtSignal()
    back_button = QtCore.pyqtSignal(dict)
    next_button = QtCore.pyqtSignal(str, list, dict)
    clients_button = QtCore.pyqtSignal(dict)

    screen_user = None
    coach_name = None

    def __init__(self, conn):
        super(CoachScheduleWindow, self).__init__()
        self.setupUi(self)
        self.conn = conn
        self.selected_day = None

        self.back.clicked.connect(self.button_clicked)
        self.logout.clicked.connect(self.handle_logout)
        self.clients.clicked.connect(self.handle_clients)
        self.help.clicked.connect(self.handle_help)
        self.next.clicked.connect(self.handle_next)

    def set_user(self, current_user):
        self.screen_user = current_user
        self.coach_name = f"{current_user['First_Name']} {current_user['Last_Name']}"
        self.set_sessions()

    def button_clicked(self):
        self.back_button.emit(self.screen_user)

    def handle_logout(self):
        self.logout_button.emit()
        print("Logging out")

    def handle_clients(self):
        self.clients_button.emit(self.screen_user)

    def handle_help(self):
        pdf_path = "C:\\Users\\JC\\Desktop\\softeng-main\\Anytime Fitness User Manual.pdf"
        QDesktopServices.openUrl(QUrl.fromLocalFile(pdf_path))

    def handle_next(self):
        self.next_button.emit(self.formatted_date, self.details, self.screen_user)

    def update_date(self, formatted_date):
        self.formatted_date = formatted_date

        # Format the date for display
        date_obj = datetime.datetime.strptime(formatted_date, "%B %d, %Y")
        day_of_week = date_obj.strftime("%A")  # Get the day of the week

        # Set the text with formatted date and day of the week
        display_text = f"{formatted_date} ({day_of_week})"
        self.date.setText(display_text)
        self.date.setDisabled(True)  # Disable editing

        self.selected_day = day_of_week  # Store the selected day of the week
        self.set_sessions()  # Update sessions based on the selected date


    def set_sessions(self):
        if self.selected_day is None:
            print("Selected day is None")
            return

        try:
            with self.conn.cursor(dictionary=True) as cursor:
                sql = """
                SELECT s.SessionID, s.BookingID, s.Day, s.StartTime, s.EndTime, c.First_Name, c.Last_Name, b.Program_Plan
                FROM sessions s
                JOIN booking b ON s.BookingID = b.BookingID
                JOIN clients c ON b.Client_Name = c.Username
                WHERE s.Day = %s AND b.Coach_Name = %s AND s.Status IN ('Not Done', 'Cancelled') AND s.Session_Counter > 0
                ORDER BY s.StartTime, s.BookingID ASC
                """
                print(f"Executing SQL with selected_day: {self.selected_day} and coach_name: {self.coach_name}")
                cursor.execute(sql, (self.selected_day, self.coach_name,))
                sessions = cursor.fetchall()

                if not sessions:
                    self.clear_textedits()
                    self.next.setDisabled(True)
                    print(f"No sessions found for {self.selected_day} and coach {self.coach_name}")
                    return

                self.clear_textedits()

                clients = []
                times = []
                self.details = []

                for session in sessions:
                    session_id = session['SessionID']
                    booking_id = session['BookingID']
                    client_first_name = session['First_Name']
                    client_last_name = session['Last_Name']
                    start_time = session['StartTime']
                    end_time = session['EndTime']
                    program_plan = session['Program_Plan']

                    print(
                        f"SessionID: {session_id}, BookingID: {booking_id}, Client: {client_first_name} {client_last_name}, Time: {start_time}-{end_time}, Program Plan: {program_plan}")

                    clients.append(f"{client_first_name} {client_last_name}")
                    times.append(f"{start_time}-{end_time}")
                    self.details.append(session_id)
                    self.details.append(booking_id)
                    self.details.append(program_plan)

                self.add_textedits(clients, times)
                self.next.setDisabled(False)

        except Error as e:
            print("Error querying database:", e)

    def clear_textedits(self):
        layout_clients = self.widget_10.layout()
        layout_times = self.widget_11.layout()

        while layout_clients.count() > 0:
            layout_clients.takeAt(0).widget().deleteLater()

        while layout_times.count() > 0:
            layout_times.takeAt(0).widget().deleteLater()

    def add_textedits(self, clients, times):
        try:
            for client, time in zip(clients, times):
                new_client_edit = QtWidgets.QLineEdit(client)
                self.apply_rounded_style(new_client_edit, "white", "#5e3b96")

                new_time_edit = QtWidgets.QLineEdit(time)
                self.apply_rounded_style(new_time_edit, "#5e3b96", "white")

                new_client_edit.setFixedWidth(200)  # Adjust the width as needed
                new_time_edit.setFixedWidth(200)  # Adjust the width as needed

                self.widget_10.layout().addWidget(new_client_edit)
                self.widget_11.layout().addWidget(new_time_edit)

        except Exception as e:
            print(f"Error adding line edits: {e}")

    def apply_rounded_style(self, widget, bg_color, text_color):
        widget.setStyleSheet(f"background-color: {bg_color}; color: {text_color}; border-radius: 10px;")
        font = QFont("Arial Black", 14)  # Adjust font family and size as per coachscheduleUI.py
        widget.setFont(font)

    def get_sessions_data(self):
        sessions_data = []
        layout_clients = self.widget_10.layout()
        layout_times = self.widget_11.layout()

        for i in range(layout_clients.count()):
            client_widget = layout_clients.itemAt(i).widget()
            time_widget = layout_times.itemAt(i).widget()
            if client_widget and time_widget:
                client = client_widget.text()
                time = time_widget.text()
                sessions_data.append((client, time))

        return sessions_data