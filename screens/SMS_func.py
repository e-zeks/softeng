import serial
import time
from datetime import datetime, timedelta
import mysql.connector
from PyQt5 import QtCore, QtWidgets
from screens.SMSUI import Ui_MainWindow
from mysql.connector import Error as MySQLError

class SMSWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    send_message = QtCore.pyqtSignal()

    def __init__(self, conn):
        super(SMSWindow, self).__init__()
        self.setupUi(self)

        self.conn = conn

        self.back.clicked.connect(self.handle_back)
        self.sendmessage.clicked.connect(self.sms_button)

        self.populate_clients_combo()

        self.comboBox.currentIndexChanged.connect(self.populate_client_details)

    def populate_clients_combo(self):
        try:
            cursor = self.conn.cursor()
            query = "SELECT Last_Name, First_Name FROM clients"
            cursor.execute(query)
            clients = cursor.fetchall()

            self.comboBox.clear()  # Clear existing items
            for client in clients:
                last_name, first_name = client
                full_name = f"{last_name}, {first_name}"
                self.comboBox.addItem(full_name)

        except MySQLError as e:
            print(f"MySQL Error occurred: {e}")

    def populate_client_details(self, index):
        try:
            cursor = self.conn.cursor()
            selected_name = self.comboBox.itemText(index)
            last_name, first_name = selected_name.split(", ")

            # Query to retrieve details from clients table
            query_client = """
                          SELECT ClientID, Username, Contact_Number 
                          FROM clients 
                          WHERE Last_Name = %s AND First_Name = %s
                          """
            cursor.execute(query_client, (last_name.strip(), first_name.strip()))
            client_details = cursor.fetchone()

            if client_details:
                client_id, username, contact_number = client_details
                self.clientid.setText(str(client_id))
                self.username.setText(username)
                self.number.setText(contact_number)
                self.contact_number = contact_number  # Store contact number for later use
                print(
                    f"Client details found: ClientID={client_id}, Username={username}, Contact_Number={contact_number}")

                # Query to retrieve coach name from booking table based on Client_Name
                query_coach = """
                                SELECT Coach_Name 
                                FROM booking 
                                WHERE Client_Name = %s OR Client_Name = %s
                             """
                cursor.execute(query_coach, (last_name.strip(), first_name.strip()))
                coach_name = cursor.fetchone()

                if coach_name:
                    self.coach.setText(coach_name[0])
                    print(f"Coach name found: {coach_name[0]}")
                else:
                    self.coach.setText("Coach not assigned")  # Or any default message
                    print("No coach name found.")

            else:
                self.clientid.setText("")
                self.username.setText("")
                self.number.setText("")
                self.coach.setText("Coach not assigned")  # Clear coach text if client not found
                print("No client details found.")

        except MySQLError as e:
            print(f"MySQL Error occurred: {e}")

        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")

        finally:
            cursor.close()

    def send_coach_session_notification(self, contact_number):
        try:
            ser = serial.Serial('COM7', 9600, timeout=10)  # Adjust COM port as necessary
            time.sleep(3)  # Timer for initialization
            print("Connected to Arduino port")

            # Calculate session time 24 hours from now
            session_time = datetime.now() + timedelta(days=1)
            session_time_str = session_time.strftime('%Y-%m-%d %H:%M:%S')

            message = f"Hello, you have a session tomorrow at {session_time_str}. See you!"

            # Format the contact number if it's not empty
            if contact_number:
                # Remove any leading zeros if present
                formatted_contact_number = contact_number.lstrip('0')

                # Ensure the number starts with "+63"
                formatted_contact_number = f"{formatted_contact_number}"

                self.send_message_to_serial(ser, formatted_contact_number, message)
            else:
                print("No valid contact number found.")

        except serial.SerialException as se:
            print(f"Serial Error occurred: {se}")

        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")

        finally:
            if ser:
                ser.close()

    def send_no_coach_notification(self, contact_number):
        try:
            current_date = datetime.now()
            day_of_month = current_date.day
            notification_time = datetime.strptime("08:00:00", "%H:%M:%S").time()  # 8:00 AM

            if day_of_month in [1, 15] and current_date.time() >= notification_time:
                # Formulate the message based on whether a coach is assigned or not
                if self.coach.text() != "Coach name found":
                    message = f"Hello, you have a session tomorrow at {current_date + timedelta(days=1)} AM. See you!"
                else:
                    message = ("Hello, we have determined that you are not enrolled in our coaching program. "
                               "Our coaches will help you all the way through your fitness journey. "
                               "So, what are you waiting for? Sign up for a coaching program now!")

                # Format the contact number if it's not empty
                if contact_number:
                    # Remove any leading zeros if present
                    formatted_contact_number = contact_number.lstrip('0')

                    # Ensure the number starts with "+63"
                    formatted_contact_number = f"{formatted_contact_number}"

                    ser = serial.Serial('COM7', 9600, timeout=10)  # Adjust COM port as necessary
                    time.sleep(3)  # Timer for initialization

                    print(f"Sending notification to {formatted_contact_number}")
                    ser.write(f"{formatted_contact_number},{message}\n".encode())
                    time.sleep(5)  # Delay to ensure message is sent

                    print("Notification sent successfully.")

            else:
                print("Notification not sent. Conditions not met.")

        except MySQLError as e:
            print(f"MySQL Error occurred: {e}")

        except serial.SerialException as se:
            print(f"Serial Error occurred: {se}")

        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")

        finally:
            if ser:
                ser.close()

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

    def sms_button(self):
        print("Sending SMS...")
        self.send_sms()
        print("SMS sent")

    def send_message_to_serial(self, ser, contact_number, message):
        try:
            if contact_number:
                contact_number = "+63" + contact_number  # Format the number properly
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