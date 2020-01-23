#tutorial = 235
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('TAB Control')
nb = ttk.Notebook(win) #created notebook on main windows
# nb.grid(row = 0,column = 0) # it's unnecessary. here some problem
nb.pack(expand = True , fill = 'both') #its best way for create notebook rather than grid

#? create tab/page same thing 
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
page3 = ttk.Frame(nb)

nb.add(page1, text = 'ONE') #for adding on notebook
nb.add(page2,text = 'TWO')
nb.add(page3,text = 'THREE')

#? page 1
label1 = ttk.Label(page1,text = "This is label1")
label1.grid(row = 0, column = 0)
entry1 = ttk.Entry(page1,width = 16)
entry1.grid(row = 0 ,column = 1)

#? fro tab 2
label2 = ttk.Label(page2,text = 'This is tab2')
label2.grid(row = 0,column = 0)
entry2 = ttk.Entry(page2,width = 16)
entry2.grid(row = 0,column = 1)

win.mainloop()