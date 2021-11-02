#imported tkinter and message module for todolist 
from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        listbox.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Entry space is blank.", "Please add some task.")


#Initialising the window  
root = Tk()
#root.geometry(widthxheight+x-axis display position+y-axis display position of window)where x is defined in module
root.geometry('500x450+500+200')
root.title('Todolist')
#bg=background color configuring
root.config(bg='#FF0000')
#resizeable means min and max access for window assigning boolean value
root.resizable(width=True, height=True)


#we frame to align the listbox and scrollbar
frame =Frame(root)
#Added space around the frame
frame.pack(pady=10)


#We created listbox for task_list
listbox = Listbox(
    frame,
    width=30,
    height=10,
    font=('Helvetica', 18),
    bd=0,
    fg='#223441',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
listbox.pack(side=LEFT, fill=BOTH)

#we added list of tasks
task_list = [
    'go jogging',
    'drink water',
    'practice yoga',
    'write book',
    'practice programming',
    'take a bath',
    'Learn something new',
    'Love dogs'
    ]

for item in task_list:
    listbox.insert(END, item)


#added scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


#for entry in tasks
my_entry = Entry(
    root,
    font=('Helvetica', 18)
    )

my_entry.pack(padx=10,pady=18)

button_frame = Frame(root)
button_frame.pack(pady=18)


#added button for entry
addTask_btn = Button(
    button_frame,
    text='Enter Task',
    font=('Helvetica'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

root.mainloop()
