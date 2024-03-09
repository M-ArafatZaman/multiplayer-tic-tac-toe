import sqlite3
import signal
import json


DB_FILE = "database.db"
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

def handle_exit(*args, **kwargs):
    print("Closing database connection.")
    conn.close()
    exit(0)

signal.signal(signal.SIGTERM, handle_exit)
signal.signal(signal.SIGINT, handle_exit)

def initialize_database():
    """
    Initializes an SQLite database with two tables: "User" and "Game".

    Returns:
        None
    """
    try:
        # Create the "User" table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS User (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                wins INTEGER DEFAULT 0,
                losses INTEGER DEFAULT 0,
                games_played INTEGER DEFAULT 0,
                score INTEGER DEFAULT 0
            )
        ''')

        # Create the "Game" table 
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Game (
                id INTEGER PRIMARY KEY,
                player1_id INTEGER,
                player2_id INTEGER,
                game_state TEXT,
                -- Add other game-related fields here
                FOREIGN KEY (player1_id) REFERENCES User (id)
                FOREIGN KEY (player2_id) REFERENCES User (id)
            )
        ''')

        conn.commit()
        print("Database initialized successfully!")

    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")


def create_user(username, password):
    """
    Creates a new user in the SQLite database.

    Args:
        username (str): User's desired username.
        password (str): User's password.

    Returns:
        bool: True if user creation is successful, False otherwise.
    """
    try:
        # Check if the username already exists
        cursor.execute("SELECT COUNT(*) FROM User WHERE username = ?", (username,))
        if cursor.fetchone()[0] > 0:
            # User already exists
            return False

        # Insert the new user into the User table
        cursor.execute("INSERT INTO User (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True

    except sqlite3.Error as e:
        print(f"Error creating user: {e}")
        return False
    
def get_user_details(username):
    """
    Retrieves user details from the SQLite database.

    Args:
        username (str): User's username.

    Returns:
        dict: A dictionary containing user details (wins, losses, games_played, score).
              Returns None if the user does not exist.
    """
    try:
        # Retrieve user details based on the provided username
        cursor.execute("SELECT id, password, wins, losses, games_played, score FROM User WHERE username = ?", (username,))
        user_details = cursor.fetchone()

        if user_details:
            id, password, wins, losses, games_played, score = user_details
            return {
                "id": id,
                "username": username,
                "password": password,
                "wins": wins,
                "losses": losses,
                "games_played": games_played,
                "score": score
            }
        else:
            print(f"User '{username}' not found.")
            return None
        
    except sqlite3.Error as e:
        print(f"Error retrieving user details: {e}")
        return None

def create_game(player1):
    try:
        # Get user details
        player1_details = get_user_details(player1)

        cursor.execute("INSERT INTO Game (player1_id) VALUES (?, ?) RETURNING id", (player1_details["id"],))
        conn.commit()
        id = cursor.fetchone()

        return id

    except sqlite3.Error as e:
        # Some error
        return None

def get_game_details(game_id):
    try:
        # Get user details
        cursor.execute("SELECT player1_id, player2_id, game_state FROM Game WHERE id = ?", (game_id,))
        player1, player2, game_state = cursor.fetchone()

        return {
            "player1": player1,
            "player2": player2,
            "game_state": json.loads(game_state)
        }

    except sqlite3.Error as e:
        # Some error
        return None

if __name__ == '__main__':
    initialize_database()