
from tkinter import *
from random import randint
import random
import datetime
from tkinter import messagebox

import self

root = Tk()
root.title("Let`s Play")
root.geometry("600x600")
root.config(bg="grey")


class Numbers():

    def __init__(self,master):


        self.result = Entry(master, borderwidth=5, relief=SUNKEN)
        self.result.grid(row=0, column=0, columnspan=6, pady=5)
        self.result.config(font=("Arial", 18))
        self.result.focus_set()  # Sets focus on the input text area
        # Entry 2
        self.lotto_numbers = Label(master, text="Lotto No.", bg='Light green')
        self.lotto_numbers.grid(row=8, column=0)
        self.lotto_num = Entry(master, borderwidth=5, relief=SUNKEN)
        self.lotto_num.grid(row=8, column=-0, columnspan=6, pady=5)
        self.lotto_num.config(font=("Arial", 18))
        self.result_lab = Label(master, text="Lotto Result", bg='light green')
        self.result_lab.grid(row=9, column=0)
        self.lotto_result = Entry(master, borderwidth=5, relief=SUNKEN)
        self.lotto_result.grid(row=9, column=0, columnspan=6, pady=5)
        self.lotto_result.config(font=("Arial", 18))

        # Buttons
        self.button1 = Button(root, text="0", width=3, command=lambda: self.ins('0, '), relief=RAISED, bg='light green')
        self.button1.grid(row=1, column=0, padx=3, pady=3)
        self.button1.config(font=("Arial", 18))

        self.button2 = Button(master, text="1", width=3, command=lambda: self.ins('1, '), relief=RAISED, bg='light green')
        self.button2.grid(row=1, column=1, padx=3, pady=3)
        self.button2.config(font=("Arial", 18))

        self.button3 = Button(master, text="2", width=3, command=lambda:self.ins('2, '),relief=RAISED,bg='light green')
        self.button3.grid(row=1, column=2, padx=3, pady=3)
        self.button3.config(font=("Arial", 18))

        self.button4 = Button(master, text="3", width=3, command=lambda:self.ins('3, '),relief=RAISED,bg='light green')
        self.button4.grid(row=1, column=3, padx=3, pady=3)
        self.button4.config(font=("Arial", 18))

        self.button5 = Button(master, text="4", width=3, command=lambda:self.ins('4, '),relief=RAISED,bg='light green')
        self.button5.grid(row=1, column=4, padx=3, pady=3)
        self.button5.config(font=("Arial", 18))

        self.button6 = Button(master, text="5", width=3, command=lambda:self.ins('5, '),relief=RAISED,bg='light green')
        self.button6.grid(row=1, column=5, padx=3, pady=3)
        self.button6.config(font=("Arial", 18))

        self.button7 = Button(master, text="6", width=3, command=lambda:self.ins('6, '),relief=RAISED,bg='light green')
        self.button7.grid(row=1, column=6, padx=3, pady=3)
        self.button7.config(font=("Arial", 18))

        self.button8 = Button(master, text="7", width=3, command=lambda:self.ins('7, '),relief=RAISED,bg='light green')
        self.button8.grid(row=1, column=7, padx=3, pady=3)
        self.button8.config(font=("Arial", 18))

        self.button9 = Button(master, text="8", width=3, command=lambda:self.ins('8, '),relief=RAISED,bg='light green')
        self.button9.grid(row=2, column=0, padx=3, pady=3)
        self.button9.config(font=("Arial", 18))

        self.button0 = Button(master, text="9", width=3, command=lambda: self.ins('9, '),relief=RAISED,bg='light green')
        self.button0.grid(row=2, column=1, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button0 = Button(master, text="10", width=3, command=lambda: self.ins('10, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=2, column=2, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button0 = Button(master, text="11", width=3, command=lambda: self.ins('11, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=2, column=3, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button0 = Button(master, text="12", width=3, command=lambda: self.ins('12, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=2, column=4, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button0 = Button(master, text="13", width=3, command=lambda: self.ins('13, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=2, column=5, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button0 = Button(master, text="14", width=3, command=lambda: self.ins('14, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=2, column=6, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button0 = Button(master, text="15", width=3, command=lambda: self.ins('15, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=2, column=7, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button0 = Button(master,text="16", width=3, command=lambda: self.ins('16, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=3, column=0, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="17", width=3, command=lambda: self.ins('17, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=3, column=1, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="18", width=3, command=lambda: self.ins('18, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=3, column=2, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="19", width=3, command=lambda: self.ins('19, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=3, column=3, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="20", width=3, command=lambda: self.ins('20, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=3, column=4, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="21", width=3, command=lambda: self.ins('21, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=3, column=5, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="22", width=3, command=lambda: self.ins('22, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=3, column=6, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="23", width=3, command=lambda: self.ins('23, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=3, column=7, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="24", width=3, command=lambda: self.ins('24, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=4, column=0, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="25", width=3, command=lambda: self.ins('25, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=4, column=1, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="26", width=3, command=lambda: self.ins('26, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=4, column=2, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="27", width=3, command=lambda: self.ins('27, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=4, column=3, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="28", width=3, command=lambda: self.ins('28, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=4, column=4, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="29", width=3, command=lambda: self.ins('29, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=4, column=5, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="30", width=3, command=lambda: self.ins('30, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=4, column=6, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="31", width=3, command=lambda: self.ins('31, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=4, column=7, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="32", width=3, command=lambda: self.ins('32, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=5, column=0, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="33", width=3, command=lambda: self.ins('33, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=5, column=1, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="34", width=3, command=lambda: self.ins('34, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=5, column=2, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="35", width=3, command=lambda: self.ins('35, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=5, column=3, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="36", width=3, command=lambda: self.ins('36, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=5, column=4, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="37", width=3, command=lambda: self.ins('37, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=5, column=5, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="38", width=3, command=lambda: self.ins('38, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=5, column=6, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="39", width=3, command=lambda: self.ins('39, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=5, column=7, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="40", width=3, command=lambda: self.ins('40, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=6, column=0, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="41", width=3, command=lambda: self.ins('41, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=6, column=1, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="42", width=3, command=lambda: self.ins('42, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=6, column=2, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="43", width=3, command=lambda: self.ins('43, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=6, column=3, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="44", width=3, command=lambda: self.ins('44, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=6, column=4, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="45", width=3, command=lambda: self.ins('45, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=6, column=5, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="46", width=3, command=lambda: self.ins('46, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=6, column=6, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="47", width=3, command=lambda: self.ins('47, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=6, column=7, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="48", width=3, command=lambda: self.ins('48, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=7, column=0, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(master, text="49", width=3, command=lambda: self.ins('49, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=7, column=1, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        # Operations Buttons
        self.button0 = Button(master, text="Play", width=3, command=self.play, relief=RAISED,
                              bg='light green')
        self.button0.grid(row=0, column=5, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.empty = []
        self.num = self.result.get()
        self.ran_numbers = random.sample(range(0,49), 6)

    def ins(self, val):
        self.result.insert(END, val)

    def cancel(self):
        self.result.delete(0, 'end')

    def delete_all(self):
        x = self.result.get()
        self.result.delete(0, 'end')
        y = x[:-1]
        self.result.insert(0, y)

    def play(self):

        for i in self.ran_numbers:
            if i in str(self.result.get()):
                self.empty.append(i)
        self.lotto_num.insert(0, self.ran_numbers)


y = Numbers(root)
root.mainloop()

