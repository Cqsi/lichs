import threading

class Game(threading.Thread):
    def __init__(self, board, game_id, **kwargs):
        super().__init__(**kwargs)
        self.game_id = game_id
        self.board = board
        self.stream = board.stream_game_state(game_id)
        self.current_state = next(self.stream)

    def run(self):
        for event in self.stream:
            if event['type'] == 'gameState':
                self.handle_state_change(event)
            elif event['type'] == 'chatLine':
                self.handle_chat_line(event)

    def handle_state_change(self, game_state):
        print("White moved!!!")

    def handle_chat_line(self, chat_line):
        pass