from PyQt5 import QtCore, QtGui, QtWidgets
from screens.coachclienteditUI import Ui_MainWindow  # Assuming this is your generated UI file
from mysql.connector import connect, Error

class CoachClientEditWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()

    def __init__(self, client_details2, conn):
        super(CoachClientEditWindow, self).__init__()
        self.conn = conn
        self.client_details2 = client_details2
        self.setupUi(self)

        # Connect signals
        self.back.clicked.connect(self.handle_back)
        self.save.clicked.connect(self.handle_save)

        # Populate UI with initial client details
        self.set_clientdetails(client_details2)

    def set_clientdetails(self, client_details2):
        # Populate UI fields with initial client details
        self.clientname.setText(client_details2.get('Client_Name', ''))
        self.contactnumber.setText(client_details2.get('Contact_Number', ''))
        self.package_2.setText(client_details2.get('Package', ''))
        self.completedsessions.setText(client_details2.get('Completed_Sessions', ''))
        self.cancelledsessions.setText(client_details2.get('Cancelled_Sessions', ''))
        self.initialweight.setText(client_details2.get('Initial_Weight', ''))
        self.currentweight.setText(client_details2.get('Current_Weight', ''))

    def load_client_details2(self, client_details2):
        # Load and populate UI fields with selected client details
        self.client_details2 = client_details2
        self.set_clientdetails(client_details2)

    def handle_back(self):
        self.back_button.emit()

    def handle_save(self):
        # Retrieve updated client details from UI
        clientname = self.clientname.text()
        contactnumber = self.contactnumber.text()
        package = self.package_2.text()
        completedsessions = self.completedsessions.text()
        cancelledsessions = self.cancelledsessions.text()
        initialweight = self.initialweight.text()
        currentweight = self.currentweight.text()

        # Update database with new client details
        try:
            cursor = self.conn.cursor()
            sql = """
                UPDATE coach_clients 
                SET ClientName = %s, ContactNumber = %s, Package = %s, 
                    CompletedSessions = %s, CancelledSessions = %s, 
                    InitialWeight = %s, CurrentWeight = %s 
                WHERE ClientID = %s
            """
            cursor.execute(sql, (clientname, contactnumber, package, completedsessions,
                                 cancelledsessions, initialweight, currentweight, self.client_details2.get('Client_ID')))
            self.conn.commit()
            QtWidgets.QMessageBox.information(self, "Success", "Client details updated successfully.")
        except Error as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error updating client details: {str(e)}")
        finally:
            if cursor:
                cursor.close()

# Example usage:
if __name__ == "__main__":
    try:
        conn = connect(host="localhost", user="root", password="12345", database="softeng")
        cursor = conn.cursor(dictionary=True)

        # Example query to fetch client details
        client_id = 1  # Replace with your actual client ID or method to retrieve it
        sql = "SELECT * FROM coach_clients WHERE ClientID = %s"
        cursor.execute(sql, (client_id,))
        client_details = cursor.fetchone()

        # Launching the window with fetched client details
        app = QtWidgets.QApplication([])
        window = CoachClientEditWindow(client_details, conn)
        window.show()
        app.exec_()
    except Error as e:
        print(f"Database error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
