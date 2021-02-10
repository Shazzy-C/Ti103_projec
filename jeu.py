import chess

board = chess.Board()

print(board)
print(repr(board))

print()

board.push_san("a4")
print()
print(board)

for lm in board.legal_moves:
    print(lm, repr(lm))

if not board.is_checkmate():
    print("La partie n'est pas finie")