import random

ROWS = 6
COLUMNS = 7

def create_board():
    return [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    print("\n  " + "   ".join(str(i) for i in range(COLUMNS)))
    print(" +" + "---+" * COLUMNS)
    for row in board:
        print(" | " + " | ".join(row) + " |")
        print(" +" + "---+" * COLUMNS)

def is_valid_column(board, col):
    return 0 <= col < COLUMNS and board[0][col] == " "

def get_valid_columns(board):
    return [c for c in range(COLUMNS) if is_valid_column(board, c)]

def get_next_open_row(board, col):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == " ":
            return r
    return None

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    for r in range(ROWS):
        for c in range(COLUMNS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
    for r in range(3, ROWS):
        for c in range(COLUMNS - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True
    return False

def is_draw(board):
    return all(board[0][c] != " " for c in range(COLUMNS))

def computer_move(board):
    valid_columns = get_valid_columns(board)
    return random.choice(valid_columns)

def play_game_vs_computer():
    board = create_board()
    game_over = False
    turn = 0  # 0 = Player, 1 = Computer

    print_board(board)

    while not game_over:
        if turn % 2 == 0:
            # Player's turn
            player = "X"
            try:
                col = int(input(f"\nYour turn (Player {player}) - choose a column (0-{COLUMNS-1}): "))
                if not is_valid_column(board, col):
                    print("Invalid column. Try again.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue
        else:
            # Computer's turn
            player = "O"
            col = computer_move(board)
            print(f"\nComputer (Player {player}) chooses column {col}")

        row = get_next_open_row(board, col)
        drop_piece(board, row, col, player)
        print_board(board)

        if winning_move(board, player):
            if turn % 2 == 0:
                print("🎉 You win!")
            else:
                print("💻 The computer wins!")
            game_over = True
        elif is_draw(board):
            print("It's a draw!")
            game_over = True
        else:
            turn += 1

if __name__ == "__main__":
    play_game_vs_computer()
