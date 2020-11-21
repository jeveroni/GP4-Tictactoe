import tkinter
import tkinter.messagebox
import numpy as np
from tkinter import *

window = tkinter.Tk()
window.geometry("955x455")
window.resizable(0, 0)
window.title("Jev's Tic-Tac-Toe Game")

left_frame = tkinter.Frame(window,height=455,width=455, background= 'black')
left_frame.place(x=0,y=0)
right_frame = tkinter.Frame(window,height=455,width=500,background='lightblue')
right_frame.place(x=455,y=0)

 

def press_click(event):
    global hold_board
    global player
    x = event.widget.winfo_x()
    y = event.widget.winfo_y()
    if(opponent == 'Player'):
        if(hold_board[spot_check(x,y)[0]][spot_check(x,y)[1]] != 0):
            ''
    #        print('nothing happens')
        else:
            if(player == 'x'):
                event.widget.configure(text='x', font = "Helvetica 200 bold")
                hold_board[spot_check(x,y)[0]][spot_check(x,y)[1]] = 1
            elif(player == 'o'):
                event.widget.configure(text='o', font = "Helvetica 200 bold")
                hold_board[spot_check(x,y)[0]][spot_check(x,y)[1]] = 2
            if(check_win(1)):
                for i in range(3):
                    for j in range(3):
                        hold_board[i][j] = 3
            if(player == 'x'):
                player =  'o'
            elif(player =='o'):
                player =  'x'
            current_player.configure(text = f"The current player is {player}")
    if(opponent == 'AI'):
        if(hold_board[spot_check(x,y)[0]][spot_check(x,y)[1]] != 0):
            ''
        else:
            event.widget.configure(text='x', font = "Helvetica 200 bold")
            hold_board[spot_check(x,y)[0]][spot_check(x,y)[1]] = 1
            if(check_win(1)):
                for i in range(3):
                    for j in range(3):
                        hold_board[i][j] = 3
            ai_pick_spot(hold_board)
            if(check_win(1)):
                for i in range(3):
                    for j in range(3):
                        hold_board[i][j] = 3
            



def check_win(x):
    for i in range(3):
        if(np.array_equal(hold_board[i],np.array([1,1,1])) or np.array_equal(hold_board[i],np.array([2,2,2]))):
            print(i,'row')
            for j in range(3):
                if(x==1):
                    board[j][i].configure(bg='green')
            return True
#        if(np.array_equal(hold_board[i],np.array([2,2,2]))):
#            print(i,'row')
#            for j in range(3):
#                board[j][i].configure(bg='green')
        if(np.array_equal(hold_board[:,i],np.array([1,1,1])) or np.array_equal(hold_board[:,i],np.array([2,2,2]))):
            print(i,'col')
            for j in range(3):
                if(x==1):
                    board[i][j].configure(bg='green')
            return True 
#        if(np.array_equal(hold_board[:,i],np.array([2,2,2]))):
#            print(i,'col')
#            for j in range(3):
#                board[i][j].configure(bg='green')
        if(np.array_equal(np.diagonal(hold_board),([1,1,1])) or np.array_equal(np.diagonal(hold_board),([2,2,2])) ):
            for i in range(3):
                if(x==1):
                    board[i][i].configure(bg='green')
            return True
        if(np.array_equal(np.fliplr(hold_board).diagonal(),([1,1,1])) or np.array_equal(np.fliplr(hold_board).diagonal(),([2,2,2]))):
            for i in range(3):
                if(x==1):
                    board[i][2-i].configure(bg='green')
            return True
    if(np.count_nonzero(hold_board) == 9):
        for i in range(3):
            for j in range(3):
                if(x==1):
                    board[i][j].configure(bg='orange')
        return 'draw'

    
    
    
def spot_check(y,x):
    new_x = (x-5)/150
    new_y = (y-5)/150
    return([int(new_x), int(new_y)])
    
def reset_game():
    global player
    for i in range(3):
        for j in range(3):
            board[i][j].configure(bg='white',text = '')
            hold_board[i][j] = 0
    player = 'x'
    current_player.configure(text = f"The current player is {player}")
    
def pvp():
    global opponent
    reset_game()
    opponent = 'Player'
    opponent_label.configure(text = f"Your current opponent is {opponent}")
  
def ai():
    global opponent
    reset_game()
    opponent = 'AI'
    opponent_label.configure(text = f"Your current opponent is {opponent}")
    
def ai_pick_spot(hold_board):
    if(np.count_nonzero(hold_board) == 1):
        if(hold_board[1][1]==0):
            hold_board[1][1] = 2
            board[1][1].configure(text='o', font = "Helvetica 200 bold")
        if(hold_board[1][1]==1):
            hold_board[0][0] = 2
            board[0][0].configure(text='o', font = "Helvetica 200 bold")
    else:
        spot = max()[1]
        hold_board[spot[0]][spot[1]] = 2
        board[spot[1]][spot[0]].configure(text='o',font = 'Helvetica 200 bold')
  

                
def max():
    check_board = np.zeros([3,3])
    print('max')
    for i in range(3):
        for j in range(3):
            if(hold_board[i][j] != 0):
                check_board[i][j] = -1000
            else:
                hold_board[i][j] = 2
                if(check_win(0) == True):
                    
                    check_board[i][j] = 1
                elif(check_win(0) == 'draw'):
                    check_board[i][j] = 0
                else:
                    check_board[i][j] = min()[0]
                hold_board[i][j] = 0
    print('max gives',check_board)
    for i in range(3): 
        for j in range(3):
            if(check_board[i][j] == np.max(check_board)):
                return (check_board[i][j], [i,j])
def min():
    print('min')
    check_board = np.zeros([3,3])
    for i in range(3):
        for j in range(3):
            if(hold_board[i][j] != 0):
                check_board[i][j] = 1000
            else:
                hold_board[i][j] = 1
                if(check_win(0) == True):
                    check_board[i][j] = -1
                elif(check_win(0) == 'draw'):
                    check_board[i][j] = 0
                else:
                    check_board[i][j] = max()[0]
                hold_board[i][j] = 0
    print('min gives', check_board)
    for i in range(3):
        for j in range(3):
            if(check_board[i][j] == np.min(check_board)):
                return (check_board[i][j], [i,j])                
                
                
                
                
                
                
opponent = 'Player'
player = 'x'
board=[]
hold_board=np.array([
            [0,0,0],
            [0,0,0],
            [0,0,0]])

for i in range(0,3):
    button_row=[]
    for j in range(0,3):
        button = tkinter.Label(window)
        button.place(x=(150*i)+5,y=(150*j)+5, width = 145, height = 145)
        button_row.append(button)
    board.append(button_row)

for i in range(0,3):
    for j in range(0,3):
        board[i][j].bind("<ButtonPress-1>", press_click)
   
 
    
current_player = tkinter.Label(right_frame, text = f"The current player is {player}", font = "Helvetica 20 bold", bg= 'lightblue')
current_player.place(x=0, y=0, height = 150)
opponent_label = tkinter.Label(right_frame, text = f"Your current opponent is {opponent}", font = 'Helvetica 20 bold', bg='lightblue')
opponent_label.place(x=0, y=225)
restart_button = tkinter.Button(right_frame, command = reset_game, text='Reset')
restart_button.place(x=100,y=350,height=100,width=300)
pvp_button = tkinter.Button(right_frame, command = pvp, text='1v1')
pvp_button.place(x=100,y=300,height=50,width=150)
ai_button = tkinter.Button(right_frame,command = ai, text='AI')
ai_button.place(x=250,y=300,height=50,width=150)
tkinter.mainloop()