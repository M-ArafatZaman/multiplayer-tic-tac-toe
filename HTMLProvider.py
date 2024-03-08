
WELCOME_PAGE = "welcome.html"
LOGIN_PAGE = "login.html"

def get_welcome_page():
    response = ""
    with open(f"html/{WELCOME_PAGE}") as file:
        response = file.read()
    return response

def get_login_page():
    response = ""
    with open(f"html/{LOGIN_PAGE}") as file:
        response = file.read()
    return response