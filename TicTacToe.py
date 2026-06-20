board = ['_' for _ in range(9)]  # Each space represents a cell in the Tic Tac Toe grid

# Function to display the board in a readable format
def print_board():
    for i in range(3):  # Loop through 3 rows
        # Print each row with vertical bars separating cell

      print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
def check_win(player):
    # All possible winning combinations (rows, columns, diagonals)
    win_lines = [
        [0,1,2], [3,4,5], [6,7,8],  # Horizontal rows
        [0,3,6], [1,4,7], [2,5,8],  # Vertical columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    # Check each line to see if all positions are filled by the same player
    for line in win_lines:
        if all(board[i] == player for i in line):
           return True  # Player has won
    return False  # No win found                                         
# Function to check if the board is full (i.e., a draw)
def is_draw():
    return '_' not in board  # If no empty spaces, it's a draw
 
# Minimax algorithm to calculate the best score for AI or Human
def minimax(is_ai):
    # Base cases: check if someone has won or if it's a draw
    if check_win('O'): return 1    # AI wins → return positive score
    if check_win('X'): return -1   # Human wins → return negative score
    if is_draw(): return 0         # Draw → return neutral score

    scores = []  # List to store scores of possible moves

    # Try every empty cell
    for i in range(9):
        if board[i] == '_':
            board[i] = 'O' if is_ai else 'X'  # Simulate move for AI or Human
            score = minimax(not is_ai)        # Recursively call minimax for next turn
            scores.append(score)              # Save the score
            board[i] = '_'                    # Undo the move (backtrack)

    # Return the best score depending on whose turn it is
    return max(scores) if is_ai else min(scores)

# Function to find the best move for the AI using minimax
def find_best_move():
    best_score = -999  # Start with a very low score
    best_move = 0      # Default move

    # Try every empty cell
    for i in range(9):
        if board[i] == '_':
            board[i] = 'O'  # Simulate AI move
            score = minimax(False)  # Evaluate move assuming Human plays next
            board[i] = '_'  # Undo move

            # If this move is better than previous best, update best move
            if score > best_score:
                best_score = score
                best_move = i

    return best_move  # Return the best move found

# Main function to play the game
def play():
    print("Welcome Jani Jeet K Dikha!")  # Greeting message
    print("You are X, AI is O")       # Show player symbols
    print_board()                     # Show initial empty board

    while True:
        # Human player's turn
        move = int(input("Choose your move (0-8) (^o^): "))  # Ask for input
        if board[move] != '_':  # Check if cell is already taken
            print("Paglu it's invalid [^_^]. Try again.")  # Ask again
            continue
        board[move] = 'X'  # Place human's move
        print_board()      # Show updated board

        # Check if human won or it's a draw
        if check_win('X'):
            print("You win! [-_-]")  # Human wins
            break
        if is_draw():
            print("It's a draw!")  # No winner
            break

        # AI's turn
        print("It's AI Turn (<'-'>)")  # Message before AI moves
        ai_move = find_best_move()  # Get best move using minimax
        board[ai_move] = 'O'        # Place AI's move
        print_board()               # Show updated board

        # Check if AI won or it's a draw
        if check_win('O'):
            print("AI wins!(^,^)")  # AI wins
            break
        if is_draw():
            print("It's a draw! (-_-)")  # No winner
            break

# Start the game by calling the play function
play()