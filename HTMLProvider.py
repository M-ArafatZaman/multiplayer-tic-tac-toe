
WELCOME_PAGE = "welcome.html"
LOGIN_PAGE = "login.html"
REGISTER_PAGE = "register.html"
GAME_PAGE = "game.html"
GAME_LOBBY_PAGE = "gamelobby.html"

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

def get_register_page():
    response = ""
    with open(f"html/{REGISTER_PAGE}") as file:
        response = file.read()
    return response

def get_game_page():
    response = ""
    with open(f"html/{GAME_PAGE}") as file:
        response = file.read()
    return response

def get_gamelobby_page():
    response = ""
    with open(f"html/{GAME_LOBBY_PAGE}") as file:
        response = file.read()
    return response