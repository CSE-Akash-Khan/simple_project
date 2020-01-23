import tkinter as tk
from tkinter import ttk
import os
from csv import DictWriter
win = tk.Tk()
win.title('Loop')

#todo: create label
#? its a normal way
# name_label = ttk.Label(win,text = 'Enter your name: ')
# name_label.grid(row = 0,column = 0,sticky = tk.W)

#? create label using loop
labels = ['Enter your name','Enter your age','gender ','Country','state','city']
for i in range(len(labels)):
    cur_label = 'label' + str(i) #label0,lalbel1--2-3-4-5---
    cur_label = ttk.Label(win,text = labels[i])
    cur_label.grid(row = i,column = 0,sticky = tk.W)

#todo: create entry box
#? normal way
# name_var = tk.StringVar()
# name_entry = ttk.Entry(win,width = 16,textvariable = name_var)
# name_entry.grid(row = 0,column = 1)

#? using for loop
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
    cur_entry = i + 'Entry'#nameEntry,ageEntry----
    cur_entry = ttk.Entry(win,width=16,textvariable = user_info[i])
    cur_entry.grid(row = counter,column = 1)
    if i == 'name':
        cur_entry.focus()
    counter += 1


#?combo box for gender
# gender = tk.StringVar()
# combo_box = ttk.Combobox(win,width = 14,textvariable = gender,state = 'readonly')
# combo_box['values'] = ('Male','Female','Other')
# combo_box.current(0)
# combo_box.grid(row = 5,column = 1)

#?write data into csv file

#?button
def submit():
    for i in user_info:
        info_var = (user_info[i].get())
        print(info_var)
    # gender_var = gender.get()
    # print(gender_var)

    # with open('file1.csv','a',newline='') as wf:
    #     dict_writer = DictWriter(wf,fieldnames = user_info.keys())
    #     if os.stat('file1.csv').st_size == 0:
    #         dict_writer.writeheader()
     
    #     dict_writer.writerows([
    #         {user_info:info_var},
    #     ])

submit_button =  ttk.Button(win,text = 'Submit',command = submit)
submit_button.grid(row = 6,columnspan = 2)

win.mainloop()