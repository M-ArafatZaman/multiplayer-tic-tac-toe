import json
import store

class TicTacToe:
    def __init__(self, gameid, player1, player2=None):
        self.board = [' '] * 9
        self.current_player = 'X'
        self.player1 = player1
        self.player2 = player2
        self.game_over = False
        self.gameid = gameid

    @classmethod
    def create_new_game(player1):
        id = store.create_game(player1)
        return TicTacToe(id, player1)
        
    @classmethod
    def load_game(game_id):
        _dict = store.get_game_details(game_id)
        game = TicTacToe(game_id, _dict["game_state"]["player1"], _dict["game_state"]["player2"])
        game.board = _dict["game_state"]["board"]
        game.game_over = _dict["game_state"]["game_over"]
        game.current_player = _dict["game_state"]["current_player"]

        return game

    def is_game_ready(self):
        return self.player1 and self.player2

    def make_move(self, position):
        if self.game_over:
            return False
        elif self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        else:
            return False

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        return None

    def get_game_state(self):
        _dict = {
            "board": self.board,
            "game_id": self.gameid,
            "current_player": self.current_player,
            "player1": self.player1,
            "player2": self.player2,
            "game_over": self.game_over
        }

        # Returns a json string
        return json.dumps(_dict)