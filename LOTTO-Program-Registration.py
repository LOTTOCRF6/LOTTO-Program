from tkinter import *

from tkinter import messagebox


root = Tk()
root.title("Registration")
root.geometry("600x600")
root.config(bg="Black")

# start of name label and entry
lab_name = Label(root, text="Enter your Name: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_name.place(x=60, y=20)
entry_name = Entry(root, bg="lightblue", fg="black")
entry_name.place(x=300, y=20, width=220, height=30)
# end of name label and entry

# start of ID label and entry
lab_id = Label(root, text="Enter your ID: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_id.place(x=60, y=70)
entry_id = Entry(root, bg="lightblue", fg="black")
entry_id.place(x=300, y=70, width=220, height=30)
# end of id label and entry

# start of Address label and entry
lab_address = Label(root, text="Enter your Address: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_address.place(x=60, y=120)
entry_address = Entry(root, bg="lightblue", fg="black")
entry_address.place(x=300, y=120, width=220, height=30)
# end of address label and entry

# start of Email label and entry
lab_email = Label(root, text="Enter your Email: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
lab_email.place(x=60, y=170)
entry_email = Entry(root, bg="lightblue", fg="black")
entry_email.place(x=300, y=170, width=220, height=30)
# end of email label and entry

# start of functions


# start of registration function
def register():
        id = int(entry_id.get())
        if id >= 18:
            import LOTTO_Program_Play
            LOTTO_Program_Play()
            root.withdraw

        else:
            messagebox.showinfo('Underage', 'Come back when you are 18 or older')
            entry_id.delete(0, END)
            entry_id.focus

# Button
btn_register = Button(root, text="Register", borderwidth="10", command=register, font=("Consolas 13 bold"), bg="black", fg="lightblue")
btn_register.place(x=80, y=210)


root.mainloop()