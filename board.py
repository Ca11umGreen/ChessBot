# Displays pieces and intialises board

from constants import *

def initialize_board():
    board = [[(EMPTY, None) for _ in range(8)] for _ in range(8)]

    # Place pawns
    for i in range(8):
        board[1][i] = (PAWN, WHITE)
        board[6][i] = (PAWN, BLACK)

    # Place other pieces
    placement = [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK]
    for i, piece in enumerate(placement):
        board[0][i] = (piece, WHITE)
        board[7][i] = (piece, BLACK)

    return board

def display_board(board):
    piece_symbols = {
        (EMPTY, None): '.',
        (PAWN, WHITE): 'P', (PAWN, BLACK): 'p',
        (KNIGHT, WHITE): 'N', (KNIGHT, BLACK): 'n',
        (BISHOP, WHITE): 'B', (BISHOP, BLACK): 'b',
        (ROOK, WHITE): 'R', (ROOK, BLACK): 'r',
        (QUEEN, WHITE): 'Q', (QUEEN, BLACK): 'q',
        (KING, WHITE): 'K', (KING, BLACK): 'k',
    }

    print("  a b c d e f g h")
    for i, row in enumerate(board):
        row_display = [piece_symbols[cell] for cell in row]
        print(f"{8 - i} " + ' '.join(row_display) + f" {8 - i}")
    print("  a b c d e f g h\n")