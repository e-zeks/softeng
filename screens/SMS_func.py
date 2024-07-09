import serial
import time
from PyQt5 import QtCore, QtWidgets
from screens.SMSUI import Ui_MainWindow
import mysql.connector
from mysql.connector import Error as MySQLError

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

                # Fetch Session_Counter for the BookingID
                query_sessions = """
                    SELECT Session_Counter 
                    FROM sessions 
                    WHERE BookingID = %s
                """
                cursor.execute(query_sessions, (booking_id,))
                print("booking id: ", booking_id)
                session_counter = cursor.fetchone()
                cursor.fetchall()  # Ensure all results are fetched
                session_counter = session_counter[0] if session_counter else 0
                print(f"Sessions left for BookingID {booking_id}: {session_counter}")

                if session_counter > 0:
                    self.coach.setText(coach_name)
                    self.messagefield.setText("yes")
                else:
                    self.coach.setText("No sessions left")
                    self.messagefield.setText("no")

            else:
                self.coach.setText("No booking found")
                print("No booking found for client.")

            print("session retrieving done: ", session_counter)

            # Fetch client details
            query_client = """
                SELECT ClientID, Username, Contact_Number 
                FROM clients 
                WHERE Username = %s
            """
            print(f"Executing query: {query_client} with username: {username}")
            cursor.execute(query_client, (username,))
            print("yes")
            client_details = cursor.fetchone()
            cursor.fetchall()  # Ensure all results are fetched
            print("Client details fetched:", client_details)

            if client_details:
                client_id, username, contact_number = client_details
                self.clientid.setText(str(client_id))
                self.username.setText(username)
                self.number.setText(contact_number)
                self.contact_number = contact_number  # Store contact number for later use
                print(
                    f"Client details found: ClientID={client_id}, Username={username}, Contact_Number={contact_number}")
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

            # Get the message from the messageField
            message = self.messagefield.toPlainText()

            # Example: Directly send the message without altering send_coach_session_notification or send_no_coach_notification
            if message:
                ser = serial.Serial('COM7', 9600, timeout=10)  # Adjust COM port as necessary
                time.sleep(3)  # Timer for initialization

                # Format the contact number if it's not empty
                if contact_number:
                    # Remove any leading zeros if present
                    formatted_contact_number = contact_number.lstrip('0')

                    # Ensure the number starts with "+63"
                    formatted_contact_number = f"{formatted_contact_number}"

                    self.send_message_to_serial(ser, formatted_contact_number, message)
                    print(f"Sending custom message to {formatted_contact_number}")
                    print(f"Message: {message}")

                    time.sleep(5)  # Delay to ensure message is sent
                    print("Custom message sent successfully.")

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