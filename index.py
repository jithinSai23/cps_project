import os

# Function to print the game board
def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check for a winner
def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

# Function to check if the board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Main function to run the game
def main():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        current_player = players[turn % 2]
        print(f"Player {current_player}'s turn")

        # Get player input
        while True:
            try:
                row, col = map(int, input("Enter row and column (1-3, space-separated): ").split())
                row, col = row - 1, col - 1  # Adjust for 0-based indexing
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Invalid move! Cell is either out of bounds or already occupied. Try again.")
            except ValueError:
                print("Invalid input! Please enter two numbers separated by a space.")

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check for a tie
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch turn
        turn += 1

if __name__ == "__main__":
    main()