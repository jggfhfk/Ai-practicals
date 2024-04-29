def solve_n_queens(N):
    # Initialize the board
    board = [-1] * N

    def place_queen(board, current_row):
        if current_row == N:
            print_board(board)
            return

        for column in range(N):
            if is_valid_place(board, current_row, column):
                board[current_row] = column
                place_queen(board, current_row + 1)

    def is_valid_place(board, occupied_rows, column):
        for i in range(occupied_rows):
            if board[i] == column or \
                board[i] - i == column - occupied_rows or \
                board[i] + i == column + occupied_rows:
                return False
        return True

    def print_board(board):
        for row in range(N):
            line = ""
            for column in range(N):
                if board[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")

    place_queen(board, 0)

# Test the function
solve_n_queens(6)
