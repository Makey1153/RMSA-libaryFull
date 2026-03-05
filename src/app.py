# src/app.py
def login(username, password):
    """Basic login function"""
    print("Login attempt detected")
    print("yooho")
    if username == "admin" and password == "secure_pw":
        return "Login Success"
    return "Login Failed"
