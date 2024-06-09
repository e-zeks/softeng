def handle_logout(current_window, login_window):
    print("Log out successful")
    current_window.close()
    login_window.show()