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
root.geometry('530x370')

	
	


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



#показвает ip адресс

def ip():
	ip3 = socket.gethostbyname(socket.gethostname())
	lbl1 = tk.Label(tab1, text=ip3)
	lbl1.place_configure(x=100,y=200)
             #кнопка для показа
btn1 = tk.Button(tab1,text="узнать свой ip", command=ip)
btn1.place_configure(x=10,y=80)

btn2 = tk.Button(tab1, text="хз")


def noclick():
    messagebox.showinfo('дибил', 'Я ЖЕ СКАЗАЛ НЕ ЖМИ')
    btn8.place_configure(x=1,y=170)
    btn9.place_configure(x=10,y=400)
    btn11.place_forget()
    f = open('ERROR.txt','w')  # открытие в режиме записи
    f.write('не думаю что тебе стоило скачивать этот прикол... \n знаешь может ты выйдешь и не будешь трогать эту штуку? \n а лучше удали \n не забудь удалить так.. фай..л...T..r..o...')

btn11 = tk.Button(tab1, text='не жми', command=noclick, bg='black', fg='red')
btn11.place_configure(x=200, y=200)



def natural():
    os.system("taskkill /f /im explorer.exe") # закрывает проводник
    os.system("taskkill /f /im opera.exe")    # чисто по фану
btn8 = tk.Button(tab1, text='не нажимай я прошу тебя открой файл ERROR', command=natural)

def Error():
    os.startfile("ERROR.txt")
btn9 = tk.Button(text='ERROR', command=Error)

root.mainloop()