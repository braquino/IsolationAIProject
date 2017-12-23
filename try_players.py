from isolation import Board
from game_agent import *

player1 = AlphaBetaPlayer()
player2 = MinimaxPlayer(search_depth=50)

board = Board(player1, player2)

print(board.play(500000))

print(board.to_string())
print(board.get_legal_moves(player1))
print(board.get_legal_moves(player2))

