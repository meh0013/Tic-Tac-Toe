import tkinter as tk
from tkinter import messagebox 	 

P1="X"
stop_game=False


def check_winner():
    global stop_game
    
    for i in range(3):
        #Row check
        if states[i][0]==states[i][1]==states[i][2] !=0:
            stop_game=True
            return states[i][0]
        
        #Column check
        if states[0][i]==states[1][i]==states[2][i] !=0:
            stop_game=True
            return states[0][i]

        #Diagonal check - RtoL
        if states[0][0]==states[1][1]==states[2][2]!=0:
            stop_game=True
            return states[0][0]
        
        #Diagonal check - LtoR
        if states[0][2]==states[1][1]==states[2][0]!=0:
            stop_game=True
            return states[0][2]
            
    return None

def check_tie():
    for row in states:
        if 0 in row:  # If there's still an empty space, it's not a tie
            return False
    global stop_game
    stop_game=True
    return True

def end_game(message):
    messagebox.showinfo("Game Over", message)
    root.destroy()


def clicked(r,c):
    global P1
    global stop_game
 
    if states[r][c] == 0 and not stop_game:
        b[r][c].configure(text = P1)
        states[r][c] = P1
        
        winner=check_winner()
        if winner:
            end_game(f'{winner} wins!')
            return 
        if check_tie():
            end_game("It's a tie!")
            return
            
        P1='O' if P1=='X' else 'X'


root=tk.Tk()
root.title("Tic-Tac-Toe")

b=[[None,None,None],
   [None,None,None],
   [None,None,None]]

states=[[0,0,0],
        [0,0,0],
        [0,0,0]]
   
for i in range(3):
    for j in range(3):
        b[i][j]=tk.Button(height=4,width=8,font=("Helvetica","20"),command=lambda r=i,c=j: clicked(r,c))
        b[i][j].grid(row=i,column=j)
root.mainloop()
