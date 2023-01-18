import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter.ttk import Radiobutton
import random
import time
import os
import socket

root = tk.Tk()
root.title("hack")
root.geometry('430x270')

	
	


tab_control = ttk.Notebook(root)  
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)  
tab_control.add(tab1, text='Первая')  
tab_control.add(tab2, text='Вторая')  
lbl1 = tk.Label(tab1, text='Вкладка 1')  
lbl1.grid(column=0, row=0)  
lbl2 = tk.Label(tab2, text='Вкладка 2')  
lbl2.grid(column=0, row=0)  
tab_control.pack(expand=1, fill='both')





def ip():
	ip3 = socket.gethostbyname(socket.gethostname())
	lbl1 = tk.Label(tab1, text=ip3)
	lbl1.place_configure(x=100,y=500)

btn1 = tk.Button(tab1,text="узнать свой ip", command=ip)
btn1.place_configure(x=10,y=100)


root.mainloop()