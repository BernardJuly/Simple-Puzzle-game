import random

def create_board(size=4):
    """Create a shuffled puzzle board."""
    numbers = list(range(1, size * size)) + [None]
    random.shuffle(numbers)
    return [numbers[i:i + size] for i in range(0, len(numbers), size)]

def print_board(board):
    """Print the current state of the board."""
    for row in board:
        print(" | ".join(str(cell).rjust(2) if cell is not None else "  " for cell in row))
        print("-" * (6 * len(row) - 1))

def find_empty_position(board):
    """Find the position of the empty tile (None)."""
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is None:
                return (i, j)
    return None

def is_valid_move(board, move):
    """Check if the move is valid."""
    empty_row, empty_col = find_empty_position(board)
    move_row, move_col = move
    return abs(move_row - empty_row) + abs(move_col - empty_col) == 1

def make_move(board, move):
    """Swap the empty tile with the specified move."""
    empty_row, empty_col = find_empty_position(board)
    move_row, move_col = move
    board[empty_row][empty_col], board[move_row][move_col] = board[move_row][move_col], board[empty_row][empty_col]

def is_solved(board):
    """Check if the board is solved."""
    flat_board = [cell for row in board for cell in row if cell is not None]
    return flat_board == sorted(flat_board)

def main():
    size = 4
    board = create_board(size)
    print("Welcome to the Sliding Puzzle Game!")
    print("Arrange the numbers in ascending order by sliding the tiles.")
    print("Use row and column indices to make a move (e.g., 0 1).")

    while not is_solved(board):
        print_board(board)
        try:
            move = tuple(map(int, input("Enter your move (row col): ").split()))
            if len(move) != 2:
                print("Invalid input. Please enter two numbers.")
                continue
            if not is_valid_move(board, move):
                print("Invalid move. Try again.")
                continue
            make_move(board, move)
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    print_board(board)
    print("Congratulations! You solved the puzzle!")

if __name__ == "__main__":
    main()
