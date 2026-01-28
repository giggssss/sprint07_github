def login(username, password):
    if username == "admin" and password == "password123":
        return "Login successful"
    else:
        return "Login failed"