import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Menu bar')

def func():
    pass

#***********simple menu bar****************
# menu_bar = tk.Menu(win)
# win.config(menu = menu_bar) #for showing
# menu_bar.add_command(label = 'save',command = func)
# menu_bar.add_command(label = 'save as',command = func)
# menu_bar.add_command(label = 'copy',command = func)

main_menu = tk.Menu(win)
win.config(menu = main_menu)
#?file menu
file_menu = tk.Menu(main_menu,tearoff = 0)
main_menu.add_cascade(label = 'File',menu = file_menu)
file_menu.add_command(label = 'New File',command = func)
file_menu.add_command(label = 'New window',command = func)
file_menu.add_separator()
file_menu.add_command(label = 'Save File',command = func)
#? edit menu
edit_menu = tk.Menu(main_menu,tearoff = 0)
main_menu.add_cascade(label = 'Edit',menu = edit_menu)
edit_menu.add_command(label = 'Undo',command = func)
edit_menu.add_command(label = 'Redu',command = func)
edit_menu.add_separator()
edit_menu.add_command(label = 'Cut',command = func)
edit_menu.add_command(label = 'Copy',command = func)
#? selection menu
selection_menu = tk.Menu(main_menu,tearoff = 0)
main_menu.add_cascade(label = 'Selection',menu = selection_menu)
selection_menu.add_command(label = 'Select All',command = func)
selection_menu.add_separator()
selection_menu.add_command(label = 'copy link up',command = func)

win.mainloop()