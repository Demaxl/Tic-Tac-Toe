import threading
from pprint import pprint
from algorithm import *
from tkinter import *

# Global variables

X_ATTR = {'text':'X', 'fg':'#FF5B00', 'bg':'#1B2430'} # attributes of X
O_ATTR = {'text':'O', 'fg':'#FFEE63', 'bg':'#1B2430'} # attributes of O
BACKGROUND = '#1B2430'
WIN_COLOR = '#111314'

class Game:
    def __init__(self, master, board):
        self.master = master
        self.board = board
        
        self.state = [[0 for c in range(3)] for r in range(3)]

        self.running = True
        self.drawUI()

       
    def drawUI(self):
        'Draws the UI'
        self.draw_buttons()

        self.status_lbl = Label(text='Your turn', font=('Verdana', 15, 'bold'), fg='white', bg=BACKGROUND)
        self.status_lbl.grid(row=3, column=0, columnspan=3)

        menubar = Menu(root)
        root.config(menu = menubar)
        menubar.add_radiobutton(label = 'RESTART', command = self.restart)


    def draw_buttons(self):
        for r in range(3):
            for c in range(3):
                self.board[r][c] = Button(self.master, font=('Verdana', 56, 'bold'), width=3, bg=BACKGROUND, 
                                          command=lambda r=r, c=c: self.player_move(r, c), relief=SOLID, highlightthickness=1)
                self.board[r][c].grid(row = r, column = c)
                self.state[r][c] = 0

        


    def player_move(self, r, c):
        'Callback function for the buttons'

        if self.running and (self.state[r][c] == 0) and ('turn' in self.status_lbl['text']):
            self.board[r][c].config(**X_ATTR)
            self.state[r][c] = 'X'

            if not self.check(self.state):
                self.status_lbl.configure(text='Computer is playing.')
                threading.Thread(target=self.computer_move).start()
                return

            self.show_message()

    def show_message(self):
        val = utility(self.state)

        if val == 0:
            msg = 'Draw'
        elif val == -1:
            msg = 'Computer Wins'
        else:
            msg = 'You win'
        
        self.status_lbl.configure(text=msg)
        self.running = False

    def computer_move(self):
        val, action = minValue(self.state)

        r, c = action

        self.board[r][c].config(**O_ATTR)
        self.state[r][c] = 'O'

        if self.check(self.state):
            return self.show_message()
        
        self.status_lbl.configure(text='Your turn')


    def change(self, board, **kwargs):
        for pos in board:
            pos.configure(**kwargs)
            

    def check(self, states):
        if terminal(states):
            value = utility(states)

            if value == 0:
                temp = [c for r in self.board for c in r]
                self.change(temp, bg=WIN_COLOR)
            else:
                for i in range(3):
                    if states[i][0]==states[i][1]==states[i][2]!=0:
                        self.board[i][0].configure(bg=WIN_COLOR)
                        self.board[i][1].configure(bg=WIN_COLOR)
                        self.board[i][2].configure(bg=WIN_COLOR)
                        
                for i in range(3):
                    if states[0][i]==states[1][i]==states[2][i]!=0:
                        self.board[0][i].configure(bg=WIN_COLOR)
                        self.board[1][i].configure(bg=WIN_COLOR)
                        self.board[2][i].configure(bg=WIN_COLOR)   

                if states[0][0]==states[1][1]==states[2][2]!=0:
                    self.board[0][0].configure(bg=WIN_COLOR)
                    self.board[1][1].configure(bg=WIN_COLOR)
                    self.board[2][2].configure(bg=WIN_COLOR)
                    
                if states[2][0]==states[1][1]==states[0][2]!=0:
                    self.board[2][0].configure(bg=WIN_COLOR)
                    self.board[1][1].configure(bg=WIN_COLOR)
                    self.board[0][2].configure(bg=WIN_COLOR)
            

            return True
        return False

    def restart(self):
        self.draw_buttons()

        self.status_lbl.configure(text='Your turn')
        self.running = True


if __name__ == '__main__':  # main program
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]
    
    root = Tk()
    root.title('Tic Tac Toe')
    root.wm_attributes('-topmost', 1)
    root.config(bg=BACKGROUND)


    game = Game(root, board)

    
    root.mainloop()


