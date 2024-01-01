import levels_of_difficult

class TicTacToe():
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'
    
    # printing the game board
    def print_board(self):
        for i in range(0,9,3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print('-' * 9)
    # take player input
    def player_input(self):
        inp = int(input("Enter a number 1-9: "))
        if inp >= 1 and inp <=9 and self.board[inp-1] == ' ':
            self.board[inp-1] = self.current_player
            self.switch_player()
        else:
            print("Ooops player is already in that spot!")

    # checking winner
    def check_winner(self):
        # checking Horizontle
        for i in range(0,9,3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                return True
        # checking Rows
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                return True
        # checking Diagonally
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != ' ':
            return True
        elif self.board[2] == self.board[4] == self.board[6] and self.board[2] != ' ':
            return True
        return False
    
    def is_board_full(self):
        return ' ' not in self.board
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def computer(self,level):
        while self.current_player == 'O':
            position = level
            if self.board[position] == ' ':
                self.board[position] = 'O'
                self.switch_player()
        
        
                
    
def start_game():

    level = int(input("Select level: "))
    game = TicTacToe()

    if level == 1:
        level = levels_of_difficult.easy_level(game.board)

    while True:
        game.print_board()
        game.player_input()
        game.computer(level)
        
        if game.check_winner():
            game.print_board()
            print(f'Player {game.current_player} wins')
            break

        if game.is_board_full():
            game.print_board()
            print("It's a tie!")
            break

if __name__ == "__main__":
    start_game()