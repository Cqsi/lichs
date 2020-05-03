import chess
import chess.svg

board = chess.Board()
# Capital letters are black
# Small letters are white

board.push_san("e4")
board.push_san("e5")
board.push_san("Nf3")
board.push_san("d6")
board.push_san("d4")

# Print the board in the terminal
# print(board)

boardsvg = chess.svg.board(board=board) 
f = open("board.SVG", "w")
f.write(boardsvg)
f.close()

# To view results in real time, open the file with the VS-code extension "Live server"