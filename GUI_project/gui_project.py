#tutorial --- 232
import tkinter as tk #tkinter is a libery. ja pythone dewa ase
from tkinter import ttk # its a sub module of tkinter
from csv import DictWriter
import os
win = tk.Tk()
win.title('GUI')

#! create label
# for creating level we can use two module 1) pack 2)grid -- grid is batter
name_label = ttk.Label(win, text = 'Enter your name: ')
name_label.grid(row = 0, column = 0,sticky = tk.W)

email_label = ttk.Label(win,text = 'Enter your email: ')
email_label.grid(row = 1, column = 0,sticky = tk.W)

age_label = ttk.Label(win,text = 'Enter your age: ')
age_label.grid(row = 2, column = 0,sticky = tk.W)

gender_label = ttk.Label(win,text = 'Select your gender: ')
gender_label.grid(row = 3, column = 0,sticky = tk.W)

#! create entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win,width = 16,textvariable = name_var)
name_entrybox.grid(row = 0,column = 1)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win,width = 16,textvariable = email_var)
email_entrybox.grid(row = 1,column = 1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win,width = 16,textvariable = age_var)
age_entrybox.grid(row = 2,column = 1)

#! create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win,width = 14,textvariable = gender_var,state = 'readonly')
gender_combobox['values'] = ('Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row = 3,column = 1)

#! radio button
user_type = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win,text = 'Student',value = 'Student',variable = user_type)
radiobtn1.grid(row = 4,column = 0)

radiobtn2 = ttk.Radiobutton(win,text = 'Teacher',value = 'Teacher',variable = user_type)
radiobtn2.grid(row = 4,column = 1)

#! check button
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win,text = 'check if you want to subscribe to out newslatter',variable = checkbtn_var)
checkbtn.grid(row = 5,columnspan = 3)

#! create button
def action():
    user_name = name_var.get()
    user_age = age_var.get()
    user_email = email_var.get()
    user_gender = gender_var.get()
    user_types = user_type.get()
    if checkbtn_var == 0:
        subscribed = 'No'
    else:
        subscribed = 'Yes'
    print(f"{user_name} is {user_age} years old {user_email} {user_gender} {user_types} {subscribed}")

    #! write as a normal text file
    # with open('file.txt','a') as wf:
    #     wf.write(f"{user_name} {user_age} {user_email} {user_gender} {user_types} {subscribed}\n")

    #! write data into csv file
    with open('file.csv','a',newline='') as wf:
        dict_writer = DictWriter(wf,fieldnames = ['user_name','user_email','user_age','user_gender','user_type','subscribed'])
        if os.stat('file.csv').st_size == 0:
            dict_writer.writeheader()
    
        dict_writer.writerow({
            'user_name' : user_name,
            'user_email' : user_email,
            'user_age' : user_age,
            'user_gender' : user_gender,
            'user_type' : user_types,
            'subscribed' : subscribed
        })

    #? it will delete previus data when i click submit button
    name_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)

    #? it will changed color when i click submit button
    name_label.configure(foreground = "Blue")
    email_label.configure(foreground = "Blue")
    age_label.configure(foreground = "Blue")

    #? it will changed button color
    submit_button.configure(foreground = 'Blue')

submit_button = tk.Button(win,text = 'Submit',command = action)
submit_button.grid(row = 6,column = 0)


win.mainloop()