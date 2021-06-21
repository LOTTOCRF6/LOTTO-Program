from tkinter import *

from tkinter import messagebox
from playsound import playsound
from xdg.Locale import regex
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


master = Tk()
master.title("LOTTO Registration")
master.geometry("600x600")
master.config(bg="Black")


# My Class
class Register():
    def __init__(self, master):

        # start of name label and entry
        self.lab_name = Label(master, text="Enter your Name: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
        self.lab_name.place(x=60, y=20)
        self.entry_name = Entry(master, bg="lightblue", fg="black")
        self.entry_name.place(x=300, y=20, width=220, height=30)
        # end of name label and entry

        # start of address label and entry
        self.lab_address = Label(master, text="Enter your Address: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
        self.lab_address.place(x=60, y=70)
        self.entry_address = Entry(master, bg="lightblue", fg="black")
        self.entry_address.place(x=300, y=70, width=220, height=30)
        # end of id label and entry

        # start of Email label and entry
        self.lab_email = Label(master, text="Enter your Email: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
        self.lab_email.place(x=60, y=120)
        self.entry_email = Entry(master, bg="lightblue", fg="black")
        self.entry_email.place(x=300, y=120, width=220, height=30)
        # end of address label and entry

        # start of ID label and entry
        self.lab_id = Label(master, text="Enter your ID: ", bg="black", fg="lightblue", font=("Consolas 15 bold"))
        self.lab_id.place(x=60, y=170)
        self.entry_id = Entry(master, bg="lightblue", fg="black")
        self.entry_id.place(x=300, y=170, width=220, height=30)
        # end of email label and entry
        # Registration Button
        self.btn_register = Button(master, text="Register", borderwidth="10", command=self.register, font=("Consolas 13 bold"),
                                   bg="black", fg="lightblue")
        self.btn_register.place(x=80, y=210)
        # Validation Button
        self.btn_validate = Button(master, text="Validate(@)", borderwidth="10", command=self.check,
                                   font=("Consolas 13 bold"),
                                   bg="black", fg="lightblue")
        self.btn_validate.place(x=250, y=210)
        # Clear Button
        self.btn_clear = Button(master, text="Clear", borderwidth="10", command=self.clear,
                                font=("Consolas 13 bold"),
                                bg="black", fg="lightblue")
        self.btn_clear.place(x=420, y=210)

    # Start of Functions
    # Clear Function
    def clear(self):
        self.entry_name.delete(0, END)
        self.entry_address.delete(0, END)
        self.entry_email.delete(0, END)
        self.entry_id.delete(0, END)

    # start of registration function
    def check(self):

        name = self.entry_name.get()
        address = self.entry_address.get()
        email = str(self.entry_email.get())

        if "@" in self.entry_email.get():
            self.entry_id.config(state='normal')

        else:
            messagebox.showinfo(title='Alert!', message="Enter valid email address!")
            self.entry_id.config(state='readonly')
            self.entry_email.delete(0, END)

    # My registration function including sending email
    def register(self):
        senders_email = 'sithandathuzipho@gmail.com'
        receivers_email = self.entry_email.get()
        password = 'Crf6ZS@#'
        subject = "Registration Details "
        try:
            for i in range(len(self.entry_email.get())):
                if re.search(regex, self.entry_email.get()):
                    msg = MIMEMultipart()
                    msg["From"] = senders_email
                    msg["To"] = receivers_email
                    msg["Subject"] = subject

                    body = "Full Name: " + str(self.entry_name.get()) + "\n"
                    body = body + "Address: " + self.entry_address.get() + "\n"
                    body = body + "Email: " + str(self.entry_email.get()) + "\n"
                    body = body + "ID: " + str(self.entry_id.get())

                    msg.attach(MIMEText(body, 'plain'))
                    text = msg.as_string()
                    s = smtplib.SMTP("smtp.gmail.com", 587)

                    s.starttls()

                    s.login(senders_email, password)
                    s.sendmail(senders_email, receivers_email, text)
                    s.quit()
                    break
            Id = int(self.entry_id.get())
            id_ls = self.entry_id.get()
            year = self.entry_id.get()[1]
            year2 = self.entry_id.get()[0:2]
            reg = open('reg.txt', 'r+')
            reg.writelines("Username:" + " " + self.entry_name.get() + "\n")
            reg.writelines("User_address:" + " " + self.entry_address.get() + "\n")
            reg.writelines("User_email:" + " " + self.entry_email.get() + "\n")
            reg.writelines("User_ID:" + " " + self.entry_id.get())
            reg.close()
            if type(Id) == type(str()) or len(id_ls) != 13:
                raise ValueError
            elif int(year) <= 3:
                playsound("Welcome-tone6.com")
                messagebox.showinfo(title="Play!", message="Lets Play!")
                master.destroy()
                import LOTTO_Program_Play

            elif int(year2) > 3 and int(year2) > 21:
                messagebox.showinfo(title="Play!", message="Lets Play!")
                master.destroy()
                import LOTTO_Program_Play

            else:
                messagebox.showinfo(title="Under Age", message="Your are too young to play")

        except ValueError:
            messagebox.showerror(title="Invalid Id", message="Enter valid ID")
            self.entry_id.delete(0, END)
            if str(self.entry_email.get()) != "":
                messagebox.showerror("ID ERROR!!!", "Please Enter Email Address")
                self.entry_email.delete(0, END)


x = Register(master)
master.mainloop()
