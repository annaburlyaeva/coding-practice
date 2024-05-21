# Design checkers

class Checkers:
    def __init__(self):
        self.size = 8
        self.board = [[' ' for _ in range(self.size)] for _ in
                      range(self.size)]
        self.current_player = 'B'  # Black starts first
        self.opponent = 'W'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.size * 2 - 1))

    def initialize_pieces(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i + j) % 2 == 0:
                    if i < 3:
                        self.board[i][j] = 'W'  # Black pieces
                    elif i > 4:
                        self.board[i][j] = 'B'  # White pieces

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        if start_row < 0 \
                or start_row >= self.size \
                or start_col < 0 \
                or start_col >= self.size:
            return False  # Start position out of bounds
        if end_row < 0 \
                or end_row >= self.size \
                or end_col < 0 \
                or end_col >= self.size:
            return False  # End position out of bounds
        if self.board[end_row][end_col] != ' ':
            return False  # End position already occupied
        return True

    def make_move(self, start_row, start_col, end_row, end_col):
        if self.is_valid_move(start_row, start_col, end_row, end_col):
            self.board[end_row][end_col] = self.board[start_row][start_col]
            self.board[start_row][start_col] = ' '  # Clear start position
            return True
        else:
            print("Invalid move. Please try again.")
            return False

    def switch_player(self):
        self.current_player, self.opponent = self.opponent, self.current_player

    def check_win_condition(self):
        # Check if the opponent has no more pieces
        # or cannot make any legal moves
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == self.opponent:
                    if self.can_capture(i, j) or self.can_move(i, j):
                        return False  # Opponent has at least one move to make
        return True  # Current player wins

    def can_capture(self, row, col):
        if self.board[row][col] == 'B':
            moves = [(1, -1), (1, 1)]
        else:
            moves = [(-1, -1), (-1, 1)]
        for dr, dc in moves:
            capture_row = row + dr
            capture_col = col + dc
            if 0 <= capture_row < self.size and 0 <= capture_col < self.size:
                if self.board[capture_row][capture_col] == self.opponent:
                    next_row = row + 2 * dr
                    next_col = col + 2 * dc
                    if 0 <= next_row < self.size and 0 <= next_col < self.size:
                        if self.board[next_row][next_col] == ' ':
                            return True  # Piece can capture opponent's piece
        return False  # No capture possible for the piece

    def can_move(self, row, col):
        if self.board[row][col] == 'B':
            moves = [(-1, -1), (-1, 1)]
        else:
            moves = [(1, -1), (1, 1)]
        for dr, dc in moves:
            next_row = row + dr
            next_col = col + dc
            # print("move" + str((next_row,next_col)) + str(self.is_valid_move(row, col, next_row, next_col)))
            if self.is_valid_move(row, col, next_row, next_col):
                return True
        return False


# Example usage:
checker_board = Checkers()
checker_board.initialize_pieces()
checker_board.print_board()

while not checker_board.check_win_condition():
    print(f"Current player: {checker_board.current_player}")
    start_row = int(input("Enter start row: "))
    start_col = int(input("Enter start column: "))
    end_row = int(input("Enter end row: "))
    end_col = int(input("Enter end column: "))

    if checker_board.make_move(start_row, start_col, end_row, end_col):
        checker_board.print_board()
        checker_board.switch_player()
