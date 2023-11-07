"""
Tic Tac Toe Game

This program allows two players to play the game of Tic Tac Toe.

"""

# Function to create the Tic Tac Toe board
def create_board():
    """
    Create the Tic Tac Toe board.

    Returns:
    board (list): A list representing the Tic Tac Toe board.
    """
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

# Function to display the Tic Tac Toe board
def display_board(board):
    """
    Display the Tic Tac Toe board.

    Args:
    board (list): A list representing the Tic Tac Toe board.
    """
    print("-------------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n-------------")

# Function to check if a player has won
def check_win(board, player):
    """
    Check if a player has won.

    Args:
    board (list): A list representing the Tic Tac Toe board.
    player (str): The player's symbol ('X' or 'O').

    Returns:
    bool: True if the player has won, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True

    # Check diagonals
    if [board[i][i] for i in range(3)].count(player) == 3:
        return True
    if [board[i][2-i] for i in range(3)].count(player) == 3:
        return True

    return False

# Function to check if the board is full
def check_draw(board):
    """
    Check if the board is full.

    Args:
    board (list): A list representing the Tic Tac Toe board.

    Returns:
    bool: True if the board is full, False otherwise.
    """
    for row in board:
        if ' ' in row:
            return False
    return True

# Function to play the game
def play_game():
    """
    Play the game of Tic Tac Toe.
    """
    board = create_board()
    current_player = 'X'

    while True:
        display_board(board)
        print(f"Player {current_player}'s turn.")

        # Get the player's move
        while True:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if board[row][col] == ' ':
                break
            else:
                print("Invalid move. Try again.")

        # Update the board
        board[row][col] = current_player

        # Check if the current player has won
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if the game is a draw
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()

