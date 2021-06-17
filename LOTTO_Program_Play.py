
from tkinter import *
import random
from tkinter import messagebox


def verify():
    pass


root = Tk()
root.title("Lotto Draw")
root.geometry("700x436")
root.config(background="Grey")
root.resizable(0, 0)

img = PhotoImage(file="crf.png")
canvas = Canvas(root, width=1200, height=800)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.pack()

play = Label(root, text="Are you ready 'Play' :", font=("bold", 12), bg="Grey", fg="white")
play.place(x=150, y=30)

num1 = IntVar()
num2 = IntVar()
num3 = IntVar()
num4 = IntVar()
num5 = IntVar()
num6 = IntVar()

txt1 = Spinbox(root, from_=1, to=49, textvariable=num1, width=2, font=("bold", 20), bg="black", fg="white")
txt1.place(x=50, y=90)
txt2 = Spinbox(root, from_=1, to=49, textvariable=num2, width=2, font=("bold", 20), bg="black", fg="white")
txt2.place(x=150, y=90)
txt3 = Spinbox(root, from_=1, to=49, textvariable=num3, width=2, font=("bold", 20), bg="black", fg="white")
txt3.place(x=250, y=90)
txt4 = Spinbox(root, from_=1, to=49, textvariable=num4, width=2, font=("bold", 20), bg="black", fg="white")
txt4.place(x=350, y=90)
txt5 = Spinbox(root, from_=1, to=49, textvariable=num5, width=2, font=("bold", 20), bg="black", fg="white")
txt5.place(x=450, y=90)
txt6 = Spinbox(root, from_=1, to=49, textvariable=num6, width=2, font=("bold", 20), bg="black", fg="white")
txt6.place(x=550, y=90)
result_answer = Label(root, width=50, height=8, bg="black", fg="white")
result_answer.place(x=130, y=150)


def exit_application():
    msgbox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if msgbox == 'yes':
        root.destroy()


def claim():
    messagebox.showinfo("Alert", "Thank you for playing")
    root.destroy()


def luck():
    x = num1.get()
    y = num2.get()
    z = num3.get()
    a = num4.get()
    b = num5.get()
    c = num6.get()

    my_list = [int(x), int(y), int(z), int(a), int(b), int(c)]
    my_list.sort()

    todaylotto = sorted(random.sample(range(1, 49), 6))

    if any(my_list) < 0 or any(my_list) > 49:
        messagebox.showinfo("NOOO", "Follow the rules")
        num1.delete(0, END)
        num2.delete(0, END)
        num3.delete(0, END)
        num4.delete(0, END)
        num5.delete(0, END)
        num6.delete(0, END)

    else:
        messagebox.showinfo("hurray", "Get ready")

        if len(todaylotto) == len(my_list):
            same = set(todaylotto).intersection(set(my_list))
            if len(same) == 6:
                result_answer.config(
                    text="Jackpot Hurray \n" + "You just got your self Price : R10, 000 000.00" + "\n Today Lotto Numbers are" + str(
                        todaylotto))
                claim_btn["state"] = "normal"
            elif len(same) == 5:
                result_answer.config(
                    text="Felicitations" + "You got 5 numbers correct" + "\n With this Outstanding Achievement" + "You won yourself R8, 584.00" + "\n Today Lotto Numbers are" + str(
                        todaylotto))
                claim_btn["state"] = "normal"
            elif len(same) == 4:
                result_answer.config(
                    text="Felicitations" + "You got 4 numbers correct" + "\n With this Meritorious Achievement" + "You won yourself R2, 384.00" + "\n Today Lotto Numbers are" + str(
                        todaylotto))
                claim_btn["state"] = "normal"
            elif len(same) == 3:
                result_answer.config(
                    text="Felicitations" + "You got 3 numbers correct" + "\n With this Substantial Achievement" + "You won yourself R100.50" + "\n Today Lotto Numbers are" + str(
                        todaylotto))
                claim_btn["state"] = "normal"
            elif len(same) == 2:
                result_answer.config(
                    text="Felicitations" + "You got 2 numbers correct" + "\n With this Adequate Achievement" + "You won yourself R20.00" + "\n Today Lotto Numbers are" + str(
                        todaylotto))
                claim_btn["state"] = "normal"
            elif len(same) == 1:
                messagebox.showinfo("RESULT",
                                    "We are sorry you only got one correct lotto numbers are: " + str(todaylotto))
            elif len(same) == 0:
                messagebox.showinfo("RESULT", "Try again Lotto numbers : " + str(todaylotto))



btn = Button(root, text="CHECK RESULTS", bg="black", fg="white", command=luck, borderwidth=5, width=15)
btn.place(x=80, y=350)
exit_btn = Button(root, text='Exit', bg='green', command=exit_application, borderwidth=5, width=10)
exit_btn.place(x=500, y=350)
claim_btn = Button(root, text='Claim Prize', bg='blue', command=claim, borderwidth=5, width=10)
claim_btn.place(x=300, y=350)
root.mainloop()

