
from tkinter import *


class numbers():

    def __init__(self):
        self.root = Tk()
        self.root.title("Let`s Play")
        self.root.geometry("600x600")
        self.root.config(bg="grey")

        self.result = Entry(self.root, borderwidth=5, relief=SUNKEN)
        self.result.grid(row=0, column=0, columnspan=6, pady=5)
        self.result.config(font=("Arial", 18))
        self.result.focus_set()  # Sets focus on the input text area

        # Buttons
        self.button1 = Button(self.root, text="0", width=3, command=lambda: self.ins('0, '),relief=RAISED,bg='light green')
        self.button1.grid(row=1, column=0, padx=3, pady=3)
        self.button1.config(font=("Arial", 18))

        self.button2 = Button(self.root, text="1", width=3, command=lambda: self.ins('1, '), relief=RAISED, bg='light green')
        self.button2.grid(row=1, column=1, padx=3, pady=3)
        self.button2.config(font=("Arial", 18))

        self.button3 = Button(self.root, text="2", width=3, command=lambda:self.ins('2, '),relief=RAISED,bg='light green')
        self.button3.grid(row=1, column=2, padx=3, pady=3)
        self.button3.config(font=("Arial", 18))

        self.button4 = Button(self.root, text="3", width=3, command=lambda:self.ins('3, '),relief=RAISED,bg='light green')
        self.button4.grid(row=1, column=3, padx=3, pady=3)
        self.button4.config(font=("Arial", 18))

        self.button5 = Button(self.root, text="4", width=3, command=lambda:self.ins('4, '),relief=RAISED,bg='light green')
        self.button5.grid(row=1, column=4, padx=3, pady=3)
        self.button5.config(font=("Arial", 18))

        self.button6 = Button(self.root, text="5", width=3, command=lambda:self.ins('5, '),relief=RAISED,bg='light green')
        self.button6.grid(row=1, column=5, padx=3, pady=3)
        self.button6.config(font=("Arial", 18))

        self.button7 = Button(self.root, text="6", width=3, command=lambda:self.ins('6, '),relief=RAISED,bg='light green')
        self.button7.grid(row=1, column=6, padx=3, pady=3)
        self.button7.config(font=("Arial", 18))

        self.button8 = Button(self.root, text="7", width=3, command=lambda:self.ins('7, '),relief=RAISED,bg='light green')
        self.button8.grid(row=1, column=7, padx=3, pady=3)
        self.button8.config(font=("Arial", 18))

        self.button9 = Button(self.root, text="8", width=3, command=lambda:self.ins('8, '),relief=RAISED,bg='light green')
        self.button9.grid(row=2, column=0, padx=3, pady=3)
        self.button9.config(font=("Arial", 18))

        self.button0 = Button(self.root, text="9", width=3, command=lambda: self.ins('9, '),relief=RAISED,bg='light green')
        self.button0.grid(row=2, column=1, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button0 = Button(self.root, text="10", width=3, command=lambda: self.ins('10, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=2, column=2, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button0 = Button(self.root, text="11", width=3, command=lambda: self.ins('11, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=2, column=3, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button0 = Button(self.root, text="12", width=3, command=lambda: self.ins('12, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=2, column=4, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button0 = Button(self.root, text="13", width=3, command=lambda: self.ins('13, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=2, column=5, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button0 = Button(self.root, text="14", width=3, command=lambda: self.ins('14, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=2, column=6, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button0 = Button(self.root, text="15", width=3, command=lambda: self.ins('15, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=2, column=7, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button0 = Button(self.root, text="16", width=3, command=lambda: self.ins('16, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=3, column=0, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="17", width=3, command=lambda: self.ins('17, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=3, column=1, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="18", width=3, command=lambda: self.ins('18, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=3, column=2, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="19", width=3, command=lambda: self.ins('19, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=3, column=3, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="20", width=3, command=lambda: self.ins('20, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=3, column=4, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="21", width=3, command=lambda: self.ins('21, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=3, column=5, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="22", width=3, command=lambda: self.ins('22, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=3, column=6, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="23", width=3, command=lambda: self.ins('23, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=3, column=7, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="24", width=3, command=lambda: self.ins('24, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=4, column=0, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="25", width=3, command=lambda: self.ins('25, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=4, column=1, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="26", width=3, command=lambda: self.ins('26, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=4, column=2, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="27", width=3, command=lambda: self.ins('27, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=4, column=3, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="28", width=3, command=lambda: self.ins('28, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=4, column=4, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="29", width=3, command=lambda: self.ins('29, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=4, column=5, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="30", width=3, command=lambda: self.ins('30, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=4, column=6, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="31", width=3, command=lambda: self.ins('31, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=4, column=7, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="32", width=3, command=lambda: self.ins('32, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=5, column=0, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="33", width=3, command=lambda: self.ins('33, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=5, column=1, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="34", width=3, command=lambda: self.ins('34, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=5, column=2, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="35", width=3, command=lambda: self.ins('35, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=5, column=3, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="36", width=3, command=lambda: self.ins('36, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=5, column=4, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="37", width=3, command=lambda: self.ins('37, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=5, column=5, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="38", width=3, command=lambda: self.ins('38, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=5, column=6, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="39", width=3, command=lambda: self.ins('39, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=5, column=7, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="40", width=3, command=lambda: self.ins('40, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=6, column=0, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="41", width=3, command=lambda: self.ins('41, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=6, column=1, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="42", width=3, command=lambda: self.ins('42, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=6, column=2, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="43", width=3, command=lambda: self.ins('43, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=6, column=3, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="44", width=3, command=lambda: self.ins('44, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=6, column=4, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="45", width=3, command=lambda: self.ins('45, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=6, column=5, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="46", width=3, command=lambda: self.ins('46, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=6, column=6, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="47", width=3, command=lambda: self.ins('47, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=6, column=7, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="48", width=3, command=lambda: self.ins('48, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=7, column=0, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))
        self.button0 = Button(self.root, text="49", width=3, command=lambda: self.ins('49, '), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=7, column=1, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        # Operations Buttons
        self.button0 = Button(self.root, text="Submit", width=3, command=lambda: self.Submit(), relief=RAISED,
                              bg='light green')
        self.button0.grid(row=0, column=5, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.root.mainloop()

    def ins(self, val):
        self.result.insert(END, val)

    def cancel(self):
        self.result.delete(0, 'end')

    def delete_all(self):
        x = self.result.get()
        self.result.delete(0, 'end')
        y = x[:-1]
        self.result.insert(0, y)

    def calculate(self):
        x = self.result.get()
        answer = eval(x)
        self.result.delete(0, 'end')
        self.result.insert(0, answer)


if __name__ == "__main__":
    numbers()