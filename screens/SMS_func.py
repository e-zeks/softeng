import serial
import time
from PyQt5 import QtCore, QtWidgets
from screens.SMSUI import Ui_MainWindow
import mysql.connector
from mysql.connector import Error as MySQLError
import datetime

class SMSWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    send_message = QtCore.pyqtSignal()

    def __init__(self, conn):
        super().__init__()
        self.setupUi(self)

        self.conn = conn

        self.back.clicked.connect(self.handle_back)
        self.sendmessage.clicked.connect(self.send_sms)

        self.populate_clients_combo()
        self.comboBox.currentIndexChanged.connect(self.populate_client_details)

    # def set_combobox_value(self, value):
    #     value_str = str(value)  # Convert value to string explicitly
    #     index = self.comboBox.findText(value_str)
    #     if index >= 0:
    #         self.comboBox.setCurrentIndex(index)
    #     else:
    #         print(f"Value '{value_str}' not found in comboBox.")

    def populate_clients_combo(self):
        try:
            cursor = self.conn.cursor()
            query = "SELECT Username, Last_Name, First_Name FROM clients"
            cursor.execute(query)
            clients = cursor.fetchall()

            self.comboBox.clear()  # Clear existing items
            for username, last_name, first_name in clients:
                full_name = f"{username} - {last_name}, {first_name}"
                self.comboBox.addItem(full_name)

        except MySQLError as e:
            print(f"MySQL Error occurred: {e}")

        finally:
            if cursor:
                cursor.close()

    def populate_client_details(self, index):
        if index == -1:
            return  # No selection

        selected_name = self.comboBox.itemText(index)
        parts = selected_name.split(" - ")
        username = parts[0]
        last_name_first_name = parts[1]
        last_name, first_name = last_name_first_name.split(", ")

        try:
            cursor = self.conn.cursor()

            # Fetch the latest BookingID
            query_booking_id = """
                SELECT BookingID 
                FROM booking 
                WHERE Client_Name = %s
                ORDER BY BookingID DESC 
                LIMIT 1
            """
            cursor.execute(query_booking_id, (username,))
            booking_id = cursor.fetchone()
            cursor.fetchall()  # Ensure all results are fetched

            if booking_id:
                booking_id = booking_id[0]

                # Fetch Coach_Name for the BookingID
                query_coach = """
                    SELECT Coach_Name 
                    FROM booking 
                    WHERE BookingID = %s
                """
                cursor.execute(query_coach, (booking_id,))
                coach_name = cursor.fetchone()
                cursor.fetchall()  # Ensure all results are fetched
                coach_name = coach_name[0] if coach_name else "Coach not assigned"
                self.coach.setText(coach_name)
                print(f"Coach name found from booking table: {coach_name}")

                # Fetch Session_Counter and StartTime for the BookingID
                query_sessions = """
                    SELECT Session_Counter, StartTime 
                    FROM sessions 
                    WHERE BookingID = %s
                """
                cursor.execute(query_sessions, (booking_id,))
                result = cursor.fetchone()
                cursor.fetchall()  # Ensure all results are fetched
                if result:
                    session_counter, start_time = result
                    print(f"Sessions left for BookingID {booking_id}: {session_counter}")

                    if session_counter > 0:
                        # Get current day index (0=Monday, 6=Sunday)
                        current_day_index = datetime.datetime.today().weekday()

                        # Calculate tomorrow's day index
                        tomorrow_day_index = (current_day_index + 1) % 7

                        # Determine tomorrow's day name based on index
                        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                        tomorrow_day = days_of_week[tomorrow_day_index]

                        # Fetch StartTime for tomorrow's session
                        query_start_time = """
                            SELECT StartTime 
                            FROM sessions 
                            WHERE BookingID = %s AND Day = %s
                        """
                        cursor.execute(query_start_time, (booking_id, tomorrow_day))
                        start_time = cursor.fetchone()
                        cursor.fetchall()  # Ensure all results are fetched

                        if start_time:
                            start_time = start_time[0]
                            self.messagefield.setText(f"Good day, Client {username}! Just a reminder that you have a coaching session scheduled for tomorrow at {start_time}. Looking forward to seeing you!")
                        else:
                            self.messagefield.setText("No session scheduled for tomorrow.")

                        self.coach.setText(coach_name)
                    else:
                        self.coach.setText("No sessions left")
                        self.messagefield.setText("Good day, Dear Client! You have used up all you sessions in your package. If you would like to book another package, let us know and we will help you set it up! ")
                else:
                    self.coach.setText("No sessions found")
                    self.messagefield.setText("No sessions found")

            else:
                self.coach.setText("No Coach Assigned")
                self.messagefield.setText("Good day, Dear Client! Would you like to book a session with one of our professional coaches? Let us know and we will set it up for you!")

            print("Session retrieving done.")

            # Fetch client details
            query_client = """
                SELECT ClientID, Username, Contact_Number 
                FROM clients 
                WHERE Username = %s
            """
            print(f"Executing query: {query_client} with username: {username}")
            cursor.execute(query_client, (username,))
            client_details = cursor.fetchone()
            cursor.fetchall()  # Ensure all results are fetched
            print("Client details fetched:", client_details)

            if client_details:
                client_id, username, contact_number = client_details
                self.clientid.setText(str(client_id))
                self.username.setText(username)
                self.number.setText(contact_number)
                self.contact_number = contact_number  # Store contact number for later use
                print(f"Client details found: ClientID={client_id}, Username={username}, Contact_Number={contact_number}")
            else:
                self.clientid.setText("")
                self.username.setText("")
                self.number.setText("")
                print("No client details found.")

        except Exception as e:
            print(f"Error retrieving client details: {e}")

        finally:
            if cursor:
                cursor.close()

    def send_sms(self):
        try:
            # Use the stored contact number for sending SMS
            contact_number = self.number.text()

            # Get the message from the messageField as a string
            message = self.messagefield.toPlainText().strip()  # Ensure no leading/trailing whitespace
            message = message.replace('\n', ' ')  # Replace newlines with spaces
            message = ' '.join(message.split())  # Replace multiple spaces with single spaces

            if message:
                # Check message length (adjust max_length according to your SMS service limits)
                max_length = 160  # Adjust based on SMS service provider limits
                if len(message) > max_length:
                    print(f"Message exceeds maximum length ({max_length} characters). Truncating...")
                    message = message[:max_length]

                ser = serial.Serial('COM7', 9600, timeout=10)  # Adjust COM port as necessary
                time.sleep(3)  # Timer for initialization

                # Format the contact number if it's not empty
                if contact_number:
                    # Remove any leading zeros if present
                    formatted_contact_number = contact_number.lstrip('0')

                    # Ensure the number starts with "+63"
                    formatted_contact_number = f"+63{formatted_contact_number}"

                    # Split the message into chunks
                    max_chunk_size = 50  # Each chunk will be 50 characters long
                    for i in range(0, len(message), max_chunk_size):
                        chunk = message[i:i + max_chunk_size]
                        # Add "END" to the last chunk to indicate the end of the message
                        if i + max_chunk_size >= len(message):
                            chunk += "END"
                        self.send_message_to_serial(ser, formatted_contact_number, chunk)
                        time.sleep(1)  # Small delay to ensure the Arduino can process each chunk

                    print(f"Sending message to {formatted_contact_number}")
                    print(f"Message: {message}")

                    print("Message sent successfully.")
                else:
                    print("No valid contact number found.")
            else:
                print("No message to send.")

        except serial.SerialException as se:
            print(f"Serial Error occurred: {se}")

        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")

        finally:
            if ser:
                ser.close()

    def send_message_to_serial(self, ser, contact_number, message):
        try:
            if contact_number:
                print(f"Sending to {contact_number}")
                ser.write(f"{contact_number},{message}\n".encode())
                time.sleep(5)  # Delay to ensure message is sent
            else:
                print("No valid contact number found.")

        except serial.SerialException as se:
            print(f"Serial Error occurred: {se}")

        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")


    def handle_back(self):
        self.back_button.emit()
