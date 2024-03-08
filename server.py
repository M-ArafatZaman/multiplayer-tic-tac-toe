from bottle import Bottle, request
import HTMLProvider

HOST = "localhost"
PORT = 8000

class BottleServer(Bottle):

    def __init__(self):
        super(BottleServer, self).__init__()
        
        # Add routes
        self.route("/", callback=self.welcome_page)

    def welcome_page(self):
        return HTMLProvider.get_welcome_page()

if __name__ == "__main__":
    app = BottleServer()
    app.run(host=HOST, port=PORT, debug=True)
