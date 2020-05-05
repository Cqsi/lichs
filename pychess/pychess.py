import chess
import chess.svg

board = chess.Board()
# Capital letters are black
# Small letters are white

# Test moves
board.push_uci("e2e4")
board.push_uci("g8f6")

# Print the board in the terminal
# print(board)

boardsvg = chess.svg.board(board=board) 
f = open("board.SVG", "w")
f.write(boardsvg)
f.close()

# To view results in real time, open the file with the VS-code extension "Live server"