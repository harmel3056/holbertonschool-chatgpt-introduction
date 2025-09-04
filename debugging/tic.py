def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def board_full(board):
    """Check if the board has any empty spaces left"""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        # Get valid row
        while True:
            try:
                row = int(input(f"Enter row (0, 1, 2) for player {player}: "))
                if row not in [0,1,2]:
                    print("Row must be 0, 1, or 2.")
                    continue
                break
            except ValueError:
                print("Please enter a number.")
        
        # Get valid column
        while True:
            try:
                col = int(input(f"Enter column (0, 1, 2) for player {player}: "))
                if col not in [0,1,2]:
                    print("Column must be 0, 1, or 2.")
                    continue
                break
            except ValueError:
                print("Please enter a number.")
        
        # Place the move
        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("That spot is already taken! Try again.")
            continue
        
        # Check for winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        # Check for draw
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        player = "O" if player == "X" else "X"

tic_tac_toe()
