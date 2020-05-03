import chess
import chess.svg

board = chess.Board()
# Capital letters are black
# Small letters are white

board.push_san("e4")
board.push_san("e5")

print(board)
boardsvg = chess.svg.board(board=board) 
f = open("boardSVG", "w")
f.write(boardsvg)
f.close()