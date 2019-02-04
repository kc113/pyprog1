#import the tkinter module 
import tkinter as tk
#import math module
import math

class CalcHyp:
    #constructor
    def __init__(self):
        
        self.window = tk.Tk() #create the window
        self.title = self.window.title("Right Triangle Calculator") #title of the window
        # Create four frames
        self.a_frame = tk.Frame(self.window)
        self.b_frame = tk.Frame(self.window)
        self.c_frame = tk.Frame(self.window)
        self.button_frame = tk.Frame(self.window)
        
        #create the widgets for the frame
        self.a_label = tk.Label(self.a_frame,text='   Side A:')
        self.a_entry = tk.Entry(self.a_frame,width=20)
        self.a_label.pack(side='left')
        self.a_entry.pack(side='left')

        self.b_label = tk.Label(self.b_frame,text='   Side B:')
        self.b_entry = tk.Entry(self.b_frame,width=20)
        self.b_label.pack(side='left')
        self.b_entry.pack(side='left')

        self.c_label = tk.Label(self.c_frame,text='   Side C:')
        self.c_entry = tk.Entry(self.c_frame,width=20)
        self.c_label.pack(side='left')
        self.c_entry.pack(side='left')
        

        
        self.calc_button = tk.Button(self.button_frame,text='Calculate',command=self.calc_ans)
        self.exit_button = tk.Button(self.button_frame,text='Exit',command=self.window.destroy)
        self.calc_button.pack(side='left')
        self.exit_button.pack(side='left')

        
        #pack the frames
        self.a_frame.pack()
        self.b_frame.pack()
        self.c_frame.pack()
        self.button_frame.pack()

        tk.mainloop() #enter the mainloop
        
    #function to calculate the hypotenuse
    def calc_ans(self):
        a_side = float(self.a_entry.get()) #get the value for side A
        b_side = float(self.b_entry.get()) #get the value for side B
        c_side = math.sqrt((a_side * a_side) + (b_side * b_side)) #calculate the hypotenuse
        self.c_entry.delete(0,20) #delete the previous entry
        self.c_entry.insert(0,c_side) #display the hypotenuse value
               
#create object
trihyp = CalcHyp()
