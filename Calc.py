import random as rn
from tkinter import *
def GeneratTwoNumbers():
    """ () -> int,int
    returns two integers in the range random values.
    """
    return rn.randint(0,11), rn.randint
    

def GeneratOperation():
    """ () -> int
    returns one integer between 0 and 2.
    0 represents addition, 1 represents subtraction and 2 represents multiplication.
    """
    return rn.randint(0,2)

def OperationResult(num1, num2, op):
    """(int,int,int) -> int
    returns the result of mathematical operation represented by op
    between the two operands num1 and num2.
    """
    #if operation is 0, then add the two operands.
    if op == 0:
        return num1 + num2
    #if operation is 0, then subtract the two operands.
    elif op == 1:
        return num1 - num2
    #if operation is 0, then multiply the two operands.
    elif op == 2:
        return num1 * num2
    else:
        return None
        
        

def VerifyOperation(num):
    """(int) -> boolean
    returns True if number is between 0 and 100, otherwise it returns False.
    """
    if num in range(0,101):
        return True
    else:
        return False


def DisplayProblem(num1, num2, op, win, qn):
    """(int, int, int, window, int) -> None
    Displays the problem to the user and an Entry for the user to enter the answer.
    after user clicks on the window, calls the function InstantFeedback.
    returns nothing.
    """
    # Application Name  
    win.title("Math Quiz")
    #Display the problem
    if op == 0:
        Label(win, text = str(num1) + " + " + str(num2)).grid(row = 0)
    if op == 1:
        Label(win, text = str(num1) + " - " + str(num2)).grid(row = 0)
    if op == 2:
        Label(win, text = str(num1) + " * " + str(num2)).grid(row = 0)
    #Entry for the user
    e1 = Entry(win)
    e1.grid(row=1, column=0)
    #click button on the window and call to instantFeedback function.
    Button(win, text='Click', command=instanFeedback(e1, res, qn, win)).grid(row=3, column=1, sticky=W, pady=4)

def instantFeedback(uans, rans, qn, win):
    if uans == rans:
        Label(win, text = "Correct answer" ).grid(row = 0)
    else:
        Label(win, text = "Wrong answer" ).grid(row = 0)

def main():
    win = Tk()
    for qn in (0,15):
        in1, in2 = GeneratTwoNumbers()
        op1 = GeneratOperation()
        res = OperationResult(in1, in2, op1)
        if verifyOperation(res):
            DisplayProblem(in1,in2,res,win,qn)
    
    
    


    
    
    
