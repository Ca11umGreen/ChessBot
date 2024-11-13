from board import *
from game_logic import *
import random

def main():
    board = initialize_board()
    player_color = WHITE

    while True:
        display_board(board)

        # Check for game over conditions (simplified)
        # TODO: Implement proper check/checkmate detection

        # Player's turn
        while True:
            move_str = input("Enter your move (e.g., e2e4): ")
            from_pos, to_pos = parse_input(move_str)
            if from_pos and to_pos:
                if is_valid_move(board, from_pos, to_pos, player_color):
                    move_piece(board, from_pos, to_pos)
                    break
                else:
                    print("Invalid move. Try again.")
            else:
                print("Invalid input format. Try again.")

        # Bot's turn
        bot_move(board)

def bot_move(board):
    moves = get_all_possible_moves(board, BLACK)
    if moves:
        move = random.choice(moves)
        move_piece(board, move[0], move[1])
        print(f"Bot moves from {format_pos(move[0])} to {format_pos(move[1])}\n")
    else:
        print("Bot has no valid moves!")

def format_pos(pos):
    cols = ['a','b','c','d','e','f','g','h']
    return f"{cols[pos[1]]}{8 - pos[0]}"

if __name__ == "__main__":
    main()