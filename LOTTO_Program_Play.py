
import random
from tkinter import *
from tkinter import messagebox


def verify():
    pass


root = Tk()
root.title("National Lotto Draw")
root.geometry("700x436")
root.config(background="Gold")
root.resizable(0, 0)

play = Label(root, text="Are you ready 'Play'", font=("bold", 15), bg="black", fg="white")
play.place(x=220, y=10)

num1 = IntVar()
num2 = IntVar()
num3 = IntVar()
num4 = IntVar()
num5 = IntVar()
num6 = IntVar()

lab_range1 = Label(root, text="1-49", bg="black", fg="white")
lab_range1.place(x=60, y=65)
txt1 = Spinbox(root, from_=0, to=49, textvariable=num1, width=2, font=("Consolas 20 bold"), bg="black", fg="white")
txt1.place(x=50, y=90)
lab_range2 = Label(root, text="1-49", bg="black", fg="white")
lab_range2.place(x=160, y=65)
txt2 = Spinbox(root, from_=0, to=49, textvariable=num2, width=2, font=("Consolas 20 bold"), bg="black", fg="white")
txt2.place(x=150, y=90)
lab_range3 = Label(root, text="1-49", bg="black", fg="white")
lab_range3.place(x=260, y=65)
txt3 = Spinbox(root, from_=0, to=49, textvariable=num3, width=2, font=("Consolas 20 bold"), bg="black", fg="white")
txt3.place(x=250, y=90)
lab_range4 = Label(root, text="1-49", bg="black", fg="white")
lab_range4.place(x=360, y=65)
txt4 = Spinbox(root, from_=0, to=49, textvariable=num4, width=2, font=("Consolas 20 bold"), bg="black", fg="white")
txt4.place(x=350, y=90)
lab_range5 = Label(root, text="1-49", bg="black", fg="white")
lab_range5.place(x=460, y=65)
txt5 = Spinbox(root, from_=0, to=49, textvariable=num5, width=2, font=("Consolas 20 bold"), bg="black", fg="white")
txt5.place(x=450, y=90)
lab_range6 = Label(root, text="1-49", bg="black", fg="white")
lab_range6.place(x=560, y=65)
txt6 = Spinbox(root, from_=0, to=49, textvariable=num6, width=2, font=("Consolas 20 bold"), bg="black", fg="white")
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
    import LOTTO_Program_Claim


def luck():
    x = num1.get()
    y = num2.get()
    z = num3.get()
    a = num4.get()
    b = num5.get()
    c = num6.get()

    play = open('play.txt', 'r+')
    play.writelines("No1:" + " " + txt1.get() + "\n")
    play.writelines("No2:" + " " + txt2.get() + "\n")
    play.writelines("No3:" + " " + txt3.get() + "\n")
    play.writelines("N4:" + " " + txt4.get() + "\n")
    play.writelines("N5:" + " " + txt5.get() + "\n")
    play.writelines("N6:" + " " + txt6.get() + "\n")

    play.close()

    my_list = [int(x), int(y), int(z), int(a), int(b), int(c)]
    my_list.sort()

    todaylotto = sorted(random.sample(range(1, 49), 6))

    if any(my_list) < 0 or any(my_list) > 49:
        messagebox.showinfo("NOOO", "Follow the rules")
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt3.delete(0, END)
        txt4.delete(0, END)
        txt5.delete(0, END)
        txt6.delete(0, END)

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
                txt1.delete(0, END)
                txt2.delete(0, END)
                txt3.delete(0, END)
                txt4.delete(0, END)
                txt5.delete(0, END)
                txt6.delete(0, END)
            elif len(same) == 0:
                messagebox.showinfo("RESULT", "Try again Lotto numbers : " + str(todaylotto))
                txt1.delete(0, END)
                txt2.delete(0, END)
                txt3.delete(0, END)
                txt4.delete(0, END)
                txt5.delete(0, END)
                txt6.delete(0, END)


btn = Button(root, text="CHECK RESULTS", bg="black", fg="white", command=luck, borderwidth=5, width=15)
btn.place(x=80, y=350)
exit_btn = Button(root, text='Exit', bg='black', fg='white', command=exit_application, borderwidth=5, width=10)
exit_btn.place(x=500, y=350)
claim_btn = Button(root, text='Claim Prize', bg='black', fg="white", command=claim, borderwidth=5, width=10)
claim_btn.place(x=300, y=350)
root.mainloop()

