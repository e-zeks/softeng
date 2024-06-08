from mysql.connector import Error
import re

def handle_register(conn, lname, fname, email, contactnum, username, password, confirm_password):
    if not validate_password(password):
        print("Password does not meet requirements.")
        return

    if password != confirm_password:
        print("Passwords do not match.")
        return

    if is_username_taken(conn, username):
        print("Username is already taken.")
        return

    try:
        cursor = conn.cursor()
        query = "INSERT INTO employees (Last_Name, First_Name, Email, Contact_Number, Username, Password) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (lname, fname, email, contactnum, username, password))
        conn.commit()
        print("Registration successful.")
    except Error as e:
        conn.rollback()
        print(f"Error: {e}")

def is_username_taken(conn, username):
    try:
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM employees WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result[0] > 0
    except Error as e:
        print(f"Error: {e}")
        return True

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if re.search("[^A-Za-z0-9]", password):
        return False
    return True

def handle_back(current_window, startup_window):
    current_window.close()
    startup_window.show()
