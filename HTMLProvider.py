
WELCOME_PAGE = "welcome.html"

def get_welcome_page():
    response = ""
    with open(f"html/{WELCOME_PAGE}") as file:
        response = file.read()

    return response