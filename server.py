from bottle import Bottle, request, response, redirect
import HTMLProvider
import user

HOST = "localhost"
PORT = 8000

class BottleServer(Bottle):

    def __init__(self):
        super(BottleServer, self).__init__()
        
        # Add routes
        self.route("/", callback=self.get_welcome_page)
        self.route("/login", method="GET", callback=self.get_login_page)
        self.route("/register", method="GET", callback=self.get_register_page)
        self.route("/game/<game_id>", method="GET", callback=self.get_game_page)
        self.route("/game", method="GET", callback=self.get_gamelobby_page)
        # Post methods
        self.route("/register", method="POST", callback=self.register)
        self.route("/login", method="POST", callback=self.login)
        self.route("/join-game", method="POST", callback=self.join_game)

    def get_welcome_page(self):
        username = request.get_cookie("user", None)
        if username:
            return redirect("/game")
        return HTMLProvider.get_welcome_page()
    
    def get_login_page(self):
        username = request.get_cookie("user", None)
        if username:
            return redirect("/game")
        return HTMLProvider.get_login_page()
    
    def get_register_page(self):
        username = request.get_cookie("user", None)
        if username:
            return redirect("/game")
        return HTMLProvider.get_register_page()
    
    def get_game_page(self, game_id):
        username = request.get_cookie("user", None)
        if username:
            data = {
                "name": username
            }
            return HTMLProvider.get_game_page().format(**data)
        else:
            return redirect("/login")
    
    def get_gamelobby_page(self):
        return HTMLProvider.get_gamelobby_page()
    
    def login(self):
        username = request.forms.get("username", None)
        password = request.forms.get("password", None)          
        if user.login_user(username, password):
            # Use cookies to login user
            response.set_cookie("user", username, path="/")
            return redirect("/game")
        return redirect("/login")

    def register(self):
        username = request.forms.get("username", None)
        password = request.forms.get("password", None)    
        if user.register_user(username, password):
            # Use cookies to login user
            response.set_cookie("user", username, path="/")
            return redirect("/game")
        return redirect("/register")
    
    def join_game(self):
        username = request.get_cookie("user", None)
        if username:
            # Is logged in
            game_code = request.forms["game-code"]
            if game_code.strip() == "":
                # Empty game code, so create a new game
                pass
        else:
            return redirect("/login")
    
if __name__ == "__main__":
    app = BottleServer()
    app.run(host=HOST, port=PORT, debug=True)
