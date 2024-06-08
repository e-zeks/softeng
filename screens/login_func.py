from mysql.connector import Error

# Function to fetch login data
def fetch_login_data(conn):
    if conn is None:
        return []

    try:
        with conn.cursor() as cursor:
            query = "SELECT Username, Password FROM employees"
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
    except Error as e:
        print(f"Error: {e}")
        return []

# Function to handle login
def handle_login(conn, username, password):
    login_data = fetch_login_data(conn)
    for db_username, db_password in login_data:
        if username == db_username and password == db_password:
            print("Login successful")
            return True
    print("Login failed")
    return False

def handle_back(current_window, startup_window):
    current_window.close()
    startup_window.show()