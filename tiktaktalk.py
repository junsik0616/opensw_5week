import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def player_move(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, choose row (0, 1, 2): "))
            col = int(input(f"Player {player}, choose column (0, 1, 2): "))
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("That cell is already occupied. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_move(board, player):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = player
            break

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        if current_player == "X":
            player_move(board, current_player)
        else:
            computer_move(board, current_player)
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if all(all(cell != " " for cell in row) for row in board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
