from tkinter import*
import pyautogui

win = Tk()
win.title("tic_tac_toe")
turn = "X"
board = ["b1","b2","b3","b4","b5","b6","b7","b8","b9"]

def ButtonFunction (button,place_x,place_y,num):
	global turn
	global board
	if turn == "X":
		turn = "Y"
	else:
		if turn == "Y":
			turn = "X"

	board[num] = turn

	button=Button(text=turn,width=10,height=10).grid(row=place_x,column=place_y)

	if board[0] == "X" and board[1] == "X" and board[2] == "X":
		pyautogui.alert("X wins")
		b1 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b1,0,0,0)).grid(row=0,column=0)
		b2 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b2,0,1,1)).grid(row=0,column=1)
		b3 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b3,0,2,2)).grid(row=0,column=2)

	elif board[3] == "X" and board[4] == "X" and board[5] == "X":
		pyautogui.alert("X wins")
		b4 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b4,1,0,3)).grid(row=1,column=0)
		b5 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b5,1,1,4)).grid(row=1,column=1)
		b6 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b6,1,2,5)).grid(row=1,column=2)

	elif board[6] == "X" and board[7] == "X" and board[8] == "X":
		pyautogui.alert("X wins")
		b7 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b7,2,0,6)).grid(row=2,column=0)
		b8 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b8,2,1,7)).grid(row=2,column=1)
		b9 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b9,2,2,8)).grid(row=2,column=2)
		
	elif board[0] == "X" and board[3] == "X" and board[6] == "X":
		pyautogui.alert("X wins")
		b1 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b1,0,0,0)).grid(row=0,column=0)
		b4 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b1,1,0,3)).grid(row=1,column=0)
		b7 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b1,2,0,6)).grid(row=2,column=0)

	elif board[1] == "X" and board[4] == "X" and board[7] == "X":
		pyautogui.alert("X wins")
		b2 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b2,0,1,1)).grid(row=0,column=0)
		b5 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b5,1,1,4)).grid(row=1,column=0)
		b8 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b8,2,1,7)).grid(row=2,column=0)

	elif board[2] == "X" and board[5] == "X" and board[8] == "X":
		pyautogui.alert("X wins")
		b3 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b3,0,2,2)).grid(row=0,column=2)
		b6 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b6,1,2,5)).grid(row=1,column=2)
		b9 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b9,2,2,8)).grid(row=2,column=2)
		
	elif board[0] == "X" and board[4] == "X" and board[8] == "X":
		pyautogui.alert("X wins")
		b1 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b1,0,0,0)).grid(row=0,column=0)
		b2 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b5,1,1,4)).grid(row=1,column=1)
		b3 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b9,2,2,8)).grid(row=2,column=2)

	elif board[2] == "X" and board[4] == "X" and board[6] == "X":
		pyautogui.alert("X wins")
		b3 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b1,0,2,3)).grid(row=0,column=2)
		b5 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b1,1,1,5)).grid(row=1,column=1)
		b7 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b1,2,0,7)).grid(row=2,column=0)

	elif board[0] == "Y" and board[1] == "Y" and board[2] == "Y":
		pyautogui.alert("Y wins")
		b1 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b1,0,0,0)).grid(row=0,column=0)
		b2 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b2,0,1,1)).grid(row=0,column=1)
		b3 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b3,0,2,2)).grid(row=0,column=2)

	elif board[3] == "Y" and board[4] == "Y" and board[5] == "Y":
		pyautogui.alert("Y wins")
		b4 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b4,1,0,3)).grid(row=1,column=0)
		b5 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b5,1,1,4)).grid(row=1,column=1)
		b6 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b6,1,2,5)).grid(row=1,column=2)

	elif board[6] == "Y" and board[7] == "Y" and board[8] == "Y":
		pyautogui.alert("Y wins")
		b7 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b7,2,0,6)).grid(row=2,column=0)
		b8 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b8,2,1,7)).grid(row=2,column=1)
		b9 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b9,2,2,8)).grid(row=2,column=2)

	elif board[0] == "Y" and board[3] == "Y" and board[6] == "Y":
		pyautogui.alert("Y wins")
		b1 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b1,0,0,0)).grid(row=0,column=0)
		b4 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b1,1,0,3)).grid(row=1,column=0)
		b7 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b1,2,0,6)).grid(row=2,column=0)

	elif board[1] == "Y" and board[4] == "Y" and board[7] == "Y":
		pyautogui.alert("Y wins")
		b2 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b2,0,1,1)).grid(row=0,column=0)
		b5 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b5,1,1,4)).grid(row=1,column=0)
		b8 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b8,2,1,7)).grid(row=2,column=0)
		board = ["b1","b2","b3","b4","b5","b6","b7","b8","b9"]

	elif board[2] == "Y" and board[5] == "Y" and board[8] == "Y":
		pyautogui.alert("Y wins")
		b3 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b3,0,2,2)).grid(row=0,column=2)
		b6 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b6,1,2,5)).grid(row=1,column=2)
		b9 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b9,2,2,8)).grid(row=2,column=2)

	elif board[0] == "Y" and board[4] == "Y" and board[8] == "Y":
		pyautogui.alert("Y wins")
		b1 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b1,0,0,0)).grid(row=0,column=0)
		b2 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b5,1,1,4)).grid(row=1,column=1)
		b3 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b9,2,2,8)).grid(row=2,column=2)
		
	elif board[2] == "Y" and board[4] == "Y" and board[6] == "Y":
		pyautogui.alert("Y wins")
		b3 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b1,0,2,3)).grid(row=0,column=2)
		b5 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b1,1,1,5)).grid(row=1,column=1)
		b7 = Button(text="",width=10,height=10,bg="lime",command=lambda:ButtonFunction(b1,2,0,7)).grid(row=2,column=0)

def playagain():
	global board
	b1 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b1,0,0,0)).grid(row=0,column=0)
	b2 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b2,0,1,1)).grid(row=0,column=1)
	b3 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b3,0,2,2)).grid(row=0,column=2)
	b4 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b4,1,0,3)).grid(row=1,column=0)
	b5 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b5,1,1,4)).grid(row=1,column=1)
	b6 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b6,1,2,5)).grid(row=1,column=2)
	b7 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b7,2,0,6)).grid(row=2,column=0)
	b8 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b8,2,1,7)).grid(row=2,column=1)
	b9 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b9,2,2,8)).grid(row=2,column=2)
	board = ["b1","b2","b3","b4","b5","b6","b7","b8","b9"]
   
l1 = Label (text="").grid(row=3,column=1)

b1 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b1,0,0,0)).grid(row=0,column=0)
b2 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b2,0,1,1)).grid(row=0,column=1)
b3 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b3,0,2,2)).grid(row=0,column=2)
b4 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b4,1,0,3)).grid(row=1,column=0)
b5 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b5,1,1,4)).grid(row=1,column=1)
b6 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b6,1,2,5)).grid(row=1,column=2)
b7 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b7,2,0,6)).grid(row=2,column=0)
b8 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b8,2,1,7)).grid(row=2,column=1)
b9 = Button(text="",width=10,height=10,command=lambda:ButtonFunction(b9,2,2,8)).grid(row=2,column=2)
clear_button = Button(text="play again",width=10,command=playagain).grid(row=3,column=1)

win.mainloop()