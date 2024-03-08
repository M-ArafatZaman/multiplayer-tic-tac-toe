import sqlite3

DB_FILE = "database.db"
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

def initialize_database():
    """
    Initializes an SQLite database with two tables: "User" and "Game".

    Args:
        db_file (str): Path to the database file.

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


if __name__ == '__main__':
    initialize_database()