def login(username, password):
    if username == "admin" and password == "password123":
        return "Login successful"
    else:
        return "Login failed"

def logout():
    return "Logged out successfully"

def reset_password(username):
    return f"Password reset link sent to {username}'s email"

def register(username, password, email):
    return f"User {username} registered successfully with email {email}"