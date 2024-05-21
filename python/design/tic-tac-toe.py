# Design a Tic Tac Toe game

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        else:
            print("Invalid move. Please try again.")
            return False

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        # Check for draw
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return None
        return 'Draw'


# Example usage:
game = TicTacToe()
game.print_board()
while True:
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    if game.make_move(row, col):
        game.print_board()
        winner = game.check_winner()
        if winner:
            if winner == 'Draw':
                print("It's a draw!")
            else:
                print(f"{winner} wins!")
            break
