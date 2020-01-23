
#? we will make our all wizerd example label entry box on frame it's easy way for handaling our wizerd
#tutorial = 234
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Label Frame')

label_frame = ttk.LabelFrame(win,text = 'Enter your details below ')
label_frame.grid(row = 0,column = 0,padx =10,pady = 10)

#? create label on label frame
labels = ['Enter your name','Enter your age','gender','country','state','city']
for i in range(len(labels)):
    cur_label = 'lebel' + str(i)
    cur_label = ttk.Label(label_frame,text = labels[i])
    cur_label.grid(row = i,column = 0,sticky = tk.W)

#? create entry box on label frame

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
    cur_box = ttk.Entry(label_frame,width = 16,textvariable = user_info[i])
    cur_box.grid(row = counter,column = 1) # we can use paddin also here
    counter += 1

#? submit button
def submit():
    for i in user_info:
        info_var = (user_info[i].get())
        print(info_var)
        
submit_button =  ttk.Button(win,text = 'Submit',command = submit)
submit_button.grid(row = 1,columnspan = 2)

#? we have a methode under label frame wizerd class. for making padding between each labels and entry boxes
#? it's return all wizerd on label_frame. as a list
for child in label_frame.winfo_children(): #[all_labels,all_entrybox ]
    child.grid_configure(padx = 2,pady = 2) # first child =  all labels . -- 2nd child = all entry box --------
win.mainloop()