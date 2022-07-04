from tkinter import *
root = Tk()
root.title("calculator")
root.configure(bg="black")
a = ""

l1 = Label(text="",font = "ariel",bg = "white")
l1.grid(row=0, column=1)

def NumberButtonFunction (number):
	global a 
	a = a + str(number)
	l1["text"] = a

b1 = Button(text="1",width=10,command = lambda:NumberButtonFunction(1)).grid(row=1, column=0)
b2 = Button(text="2",width=10,command = lambda:NumberButtonFunction(2)).grid(row=1, column=1)
b3 = Button(text="3",width=10,command = lambda:NumberButtonFunction(3)).grid(row=1, column=2)
b4 = Button(text="4",width=10,command = lambda:NumberButtonFunction(4)).grid(row=2, column=0)
b5 = Button(text="5",width=10,command = lambda:NumberButtonFunction(5)).grid(row=2, column=1)
b6 = Button(text="6",width=10,command = lambda:NumberButtonFunction(6)).grid(row=2, column=2)
b7 = Button(text="7",width=10,command = lambda:NumberButtonFunction(7)).grid(row=3, column=0)
b8 = Button(text="8",width=10,command = lambda:NumberButtonFunction(8)).grid(row=3, column=1)
b9 = Button(text="9",width=10,command = lambda:NumberButtonFunction(9)).grid(row=3, column=2)
b10 = Button(text="0",width=10,command = lambda:NumberButtonFunction(0)).grid(row=4, column=1)

def OperationButtonFunction (operation):
	global a 
	a = a + str(operation)
	l1["text"] = a 
	
def clearButtonFunction ():
	global a 
	a = ""
	l1["text"] = a

def answer ():
	global a
	e_answer = eval(l1["text"])
	l1["text"] = e_answer

SubmitButton = Button(text="calculate",width=10,command = answer).grid(row=5, column=1)
additionButton = Button(text="+",width=10,command = lambda:OperationButtonFunction("+")).grid(row=1, column=3)
substarctionButton = Button(text="-",width=10,command = lambda:OperationButtonFunction("-")).grid(row=2, column=3)
multiplyButton = Button(text="*",width=10,command = lambda:OperationButtonFunction("*")).grid(row=3, column=3)
divisionButton = Button(text="/",width=10,command = lambda:OperationButtonFunction("/")).grid(row=4,column=3)
clearButton = Button(text="clear",width=10,command = clearButtonFunction).grid(row=5,column=3)
percentageButton = Button(text="%",width=10,command = lambda:OperationButtonFunction("%")).grid(row=5,column=2)
decimalButton = Button(text=".",width=10,command = lambda:OperationButtonFunction(".")).grid(row=5,column=0)
forwardbracketButton = Button(text="(",width=10,command = lambda:OperationButtonFunction("(")).grid(row=4,column=0)
backwardbracketButton = Button(text=")",width=10,command = lambda:OperationButtonFunction(")")).grid(row=4,column=2)

root.mainloop()
