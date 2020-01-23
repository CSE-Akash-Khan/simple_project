import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Padding')

#label
labels = ['Enter your name','Enter your age','gender','country','state','city']
for i in range(len(labels)):
    cur_label = 'lebel' + str(i)
    cur_label = ttk.Label(win,text = labels[i])
    cur_label.grid(row = i,column = 0,sticky = tk.W,padx = 2,pady = 2)

#entry box
user_info = {
    'name':tk.StringVar(),
    'age':tk.StringVar(),
    'gender':tk.StringVar(),
    'country':tk.StringVar(),
    'state':tk.StringVar(),
    'city':tk.StringVar()
}
counter = 0
for i in user_info:
    cur_box = i + 'Entry box'
    cur_box = ttk.Entry(win,width = 16,textvariable = user_info[i])
    cur_box.grid(row = counter,column = 1) # we can use paddin also here
    counter += 1

#? submit button
def submit():
    for i in user_info:
        info_var = (user_info[i].get())
        print(info_var)

submit_button =  ttk.Button(win,text = 'Submit',command = submit) # we can use padding also here
submit_button.grid(row = 6,columnspan = 2)

win.mainloop()