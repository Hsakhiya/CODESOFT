import random
import string
from tkinter import *
from tkinter.ttk import *
root = Tk()
root.title("Random Password Generator")
# root.geometry("700x300")
root.resizable(width=False,height=False)

masterframe = Frame(root)
masterframe.pack(fill=BOTH, expand=True)

frame = Frame(masterframe,padding=10)
frame.pack(side=LEFT, fill=BOTH, expand=True)

optionframe = Frame(masterframe,padding=10)
# optionframe.pack(side=RIGHT, fill=Y, expand=False)

randompass = ''
character = string.ascii_letters + string.digits + '$&!@*'
option = ["All Characters", "Custom Selection"]

data = IntVar(value=5)
check_digit = IntVar()
check_lower = IntVar()
check_upper = IntVar()
check_special = IntVar()
get_option = IntVar()

def setchar():
    
    global character
    
    character = string.ascii_letters + string.digits + '$&!@*'
    if get_option.get() == 0:
        check_digit.set(0)
        check_lower.set(0)
        check_upper.set(0)
        check_special.set(0)

        
        optionframe.pack_forget()
    elif get_option.get() == 1:
        character=''
        optionframe.pack(side=RIGHT, fill=Y, expand=False)

def generate():
    global randompass
    length = data.get()
    randompass = ''

    if len(character) > 0:
        if length > 0:
            randompass = ''.join(random.choice(character) for i in range(length))
            password_lable.config(text=randompass,foreground='black')
        else:
            password_lable.config(text="Length cannot be Zero",foreground='red')
    else:
        password_lable.config(text="Select at least one character type",foreground='red')

def update_character_set():
    global character
    character = ''
    if check_digit.get():
        character += string.digits
    if check_lower.get():
        character += string.ascii_lowercase
    if check_upper.get():
        character += string.ascii_uppercase
    if check_special.get():
        character += '$&!@*'

length_lable = Label(frame, text="Password Length",font=(20))
length_lable.grid(row=0, column=0, sticky=W,pady=5)

length_entry = Entry(frame, textvariable=data, width=10,font=(15))
length_entry.grid(row=1, column=0, sticky=W,pady=10)

password_lable = Label(frame, text=randompass, width=30, relief=SUNKEN, anchor='w', font=('Arial',20))
password_lable.grid(row=2, column=0 )



btn = Button(frame, text="Generate Password", command=generate)
btn.grid(row=3, column=0,ipadx=50 )

for index in range(len(option)):
    Radiobutton(frame, text=option[index], variable=get_option, value=index, command=setchar).grid(row=4 + index, column=0, sticky=W, )

# Checkboxes for custom selection
Label(optionframe, text="Character Options", ).grid(row=0, column=0, columnspan=2, )

checkbutton_digit = Checkbutton(optionframe, text="Digits", variable=check_digit, command=update_character_set)
checkbutton_digit.grid(row=1, column=0, sticky=W, )

checkbutton_lower = Checkbutton(optionframe, text="Lowercase", variable=check_lower, command=update_character_set)
checkbutton_lower.grid(row=2, column=0, sticky=W, )

checkbutton_upper = Checkbutton(optionframe, text="Uppercase", variable=check_upper, command=update_character_set)
checkbutton_upper.grid(row=3, column=0, sticky=W, )

checkbutton_special = Checkbutton(optionframe, text="Special Characters", variable=check_special, command=update_character_set)
checkbutton_special.grid(row=4, column=0, sticky=W, )

root.mainloop()
