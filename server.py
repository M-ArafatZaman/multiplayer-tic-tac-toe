from bottle import Bottle, request
import HTMLProvider

HOST = "localhost"
PORT = 8000

class BottleServer(Bottle):

    def __init__(self):
        super(BottleServer, self).__init__()
        
        # Add routes
        self.route("/", callback=self.get_welcome_page)
        self.route("/login", method="GET", callback=self.get_login_page)
        self.route("/register", metho="GET", callback=self.get_register_page)
        self.route("/game/<game_id>", method="GET", callback=self.get_game_page)

    def get_welcome_page(self):
        return HTMLProvider.get_welcome_page()
    
    def get_login_page(self):
        return HTMLProvider.get_login_page()
    
    def get_register_page(self):
        return HTMLProvider.get_register_page()
    
    def get_game_page(self, game_id):
        return HTMLProvider.get_game_page()

if __name__ == "__main__":
    app = BottleServer()
    app.run(host=HOST, port=PORT, debug=True)
