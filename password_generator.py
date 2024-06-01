
from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip



def generator():
    small_albhabet=string.ascii_lowercase
    capital_albhabet=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation
    all=small_albhabet+capital_albhabet+numbers+special_characters

    password_length=int(length_box.get())
    if choice.get()==1:
        entryclass.insert(0, random.sample(small_albhabet+capital_albhabet, password_length))
    if choice.get()==2:
        entryclass.insert(0, random.sample(small_albhabet+capital_albhabet+numbers, password_length))
    if choice.get()==3:
        entryclass.insert(0, random.sample(all, password_length))
    if choice.get()!=1 and choice.get()!=2 and choice.get()!=3:
        messagebox.showerror("Error", "Please Select the Difficulty level")



def copy():
    random_password=entryclass.get()
    pyperclip.copy(random_password)


root = Tk()
root.title("Password Generator")
root.geometry("850x500+300+300")
choice = IntVar()
root.withdraw
Font =('Arial', 13, 'bold')
root.config(bg='gray20')


passwordlabel = Label(root, text='Password Generator', font=('Arial', 20, 'bold'), fg='white', bg='gray20')
passwordlabel.pack(pady='10')

weakradiobutton =Radiobutton(root, text='Weak', value=1, variable=choice, font=Font)
weakradiobutton.pack(pady=5)

Mediumradiobutton=Radiobutton(root, text='Medium', value=2, variable=choice, font=Font)
Mediumradiobutton.pack(pady=5)

strongradiobutton=Radiobutton(root, text='Strong', value=3, variable=choice, font=Font)
strongradiobutton.pack(pady=5)

passlabel=Label(root, text='Password Length', font=Font, bg='gray20', fg='white')
passlabel.pack(pady=5)

length_box= Spinbox(root, from_=5, to_=18, font=Font, width='15')
length_box.pack(pady='5')

generateButton = Button(root, text='Generate', font=Font, command=generator)
generateButton.pack(pady=5)

entryclass =Entry(root, width='25', bd='2', font=Font)
entryclass.pack(pady=5)

CopyButton = Button(root, text='Copy', font=Font,command=copy)
CopyButton.pack(pady=10)



root.mainloop()
