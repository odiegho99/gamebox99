"""
Tic Tac Toe Game

This program allows two players to play the game of Tic Tac Toe.
The game is played on a 3x3 grid and the players take turns marking
their symbol (X or O) on an empty cell. The first player to get
three of their symbols in a row (horizontally, vertically, or diagonally)
wins the game. If all cells are filled and no player has won, the game
ends in a draw.

The game is implemented using Python and can be played in the console.

"""

# Function to create the game board
def create_board():
    """
    Create an empty Tic Tac Toe board.

    Returns:
    - board: A list of lists representing the game board.
    """
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

# Function to print the game board
def print_board(board):
    """
    Print the Tic Tac Toe board.

    Parameters:
    - board: A list of lists representing the game board.
    """
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check if a player has won
def check_win(board, player):
    """
    Check if a player has won the game.

    Parameters:
    - board: A list of lists representing the game board.
    - player: The symbol (X or O) of the player.

    Returns:
    - win: True if the player has won, False otherwise.
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
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if the game is a draw
def check_draw(board):
    """
    Check if the game is a draw.

    Parameters:
    - board: A list of lists representing the game board.

    Returns:
    - draw: True if the game is a draw, False otherwise.
    """
    for row in board:
        if ' ' in row:
            return False
    return True

# Function to play the game
def play_game():
    """
    Play the Tic Tac Toe game.
    """
    board = create_board()
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        # Get the player's move
        while True:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))

            if board[row][col] == ' ':
                break
            else:
                print("Invalid move. Try again.")

        # Make the move
        board[row][col] = current_player

        # Check if the current player has won
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if the game is a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
