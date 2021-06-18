from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


root = Tk()
root.title("Lotto Price Claim")
root.geometry("1000x600")
root.config(background="gold")
root.resizable(0, 0)

img = PhotoImage(file="resize-lottowinner.png")
canvas = Canvas(root, width=1200, height=600)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.pack()

# labels and entries
lab_account_name = Label(root, text="Account Name", bg="gold", font=("Consolas 15 bold"))
lab_account_name.place(x=60, y=310)
entry_account_name = Entry(root, bg="lightblue", fg="black")
entry_account_name.place(x=215, y=310, width=220, height=30)

# account number label and entry
lab_account_number = Label(root, text="Account No.", bg="gold", font=("Consolas 15 bold"))
lab_account_number.place(x=60, y=350)
entry_account_number = Entry(root, bg="lightblue", fg="black")
entry_account_number.place(x=215, y=350, width=220, height=30)

# Bank name label and entry
lab_bank_name = Label(root, text="Bank Name", bg="gold", font=("Consolas 15 bold"))
lab_bank_name.place(x=60, y=390)
banks_name_options = Combobox(root, value=["Capitec Bank", "Ned Bank", "First National Bank", "Standard Bank"])
banks_name_options.place(x=215, y=390, width=220, height=30)

# Email label and entry
lab_email = Label(root, text="Enter Email", bg="gold", font=("Consolas 15 bold"))
lab_email.place(x=60, y=500)
entry_email = Entry(root, bg="lightblue", fg="black")
entry_email.place(x=215, y=500, width=220, height=30)
# Buttons
submit_btn = Button(root, text="Submit", borderwidth='10', bg="gold", fg="black", font=("Consolas 15 bold"), )
submit_btn.place(x=440, y=540)

# Functions
# Submit Button









root.mainloop()
