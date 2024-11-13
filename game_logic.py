# Handles game logic, such as determining legal moves and parsing inputs

from constants import *

def parse_input(move_str):
    cols = {'a': 0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    try:
        from_col = cols[move_str[0]]
        from_row = 8 - int(move_str[1])
        to_col = cols[move_str[2]]
        to_row = 8 - int(move_str[3])
        return (from_row, from_col), (to_row, to_col)
    except (KeyError, ValueError, IndexError):
        return None, None


def move_piece(board, from_pos, to_pos):
    piece = board[from_pos[0]][from_pos[1]]
    board[to_pos[0]][to_pos[1]] = piece
    board[from_pos[0]][from_pos[1]] = (EMPTY, None)
    
    
def is_valid_move(board, from_pos, to_pos, player_color):
    piece, color = board[from_pos[0]][from_pos[1]]
    dest_piece, dest_color = board[to_pos[0]][to_pos[1]]

    # Check if the piece belongs to the player
    if color != player_color:
        return False

    # Can't move to a square occupied by own piece
    if dest_color == player_color:
        return False

    # Basic pawn movement (forward by one)
    if piece == PAWN:
        direction = -1 if color == WHITE else 1
        start_row = 6 if color == BLACK else 1
        row_diff = to_pos[0] - from_pos[0]
        col_diff = to_pos[1] - from_pos[1]

        # Moving forward
        if col_diff == 0 and board[to_pos[0]][to_pos[1]][0] == EMPTY:
            if row_diff == direction:
                return True
            # Initial double move
            if row_diff == 2 * direction and from_pos[0] == start_row:
                between_square = (from_pos[0] + direction, from_pos[1])
                if board[between_square[0]][between_square[1]][0] == EMPTY:
                    return True
        # Capturing
        elif abs(col_diff) == 1 and row_diff == direction and dest_color == (BLACK if color == WHITE else WHITE):
            return True
        return False

    # TODO: Implement other pieces
    # For now, allow the bot to move any piece to any empty square (not legal)
    return False

def get_all_possible_moves(board, player_color):
    moves = []
    for i in range(8):
        for j in range(8):
            piece, color = board[i][j]
            if color == player_color:
                for x in range(8):
                    for y in range(8):
                        from_pos = (i, j)
                        to_pos = (x, y)
                        if is_valid_move(board, from_pos, to_pos, player_color):
                            moves.append((from_pos, to_pos))
    return moves