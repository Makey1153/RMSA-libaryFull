def login(username, password):
    """Basic login function"""
    if username == "admin" and \
       password == "secure_pw":
        return True

def login(username, password):
        print("Login attempt detected") # เพิ่ม
        if username == "admin":
            return "Login Success"
        return "Login Failed"
