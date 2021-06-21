from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import ttk
import requests
from xdg.Locale import regex

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
# Currency
result = StringVar()

response = requests.get('https://v6.exchangerate-api.com/v6/6698980fefc5cd611ec51be2/latest/USD')
results = response.json()

conversion_rates = results['conversion_rates']

currency = []
for i in conversion_rates.keys():
    currency.append(i)

currency_cb = ttk.Combobox(root)
currency_cb['values'] = currency
currency_cb['state'] = 'readonly'
currency_cb.set('Select Currency')
currency_cb.place(x=760, y=350)

currency2 = []
for i in conversion_rates.keys():
    currency.append(i)

currency_cb2 = ttk.Combobox(root)
currency_cb2['values'] = currency
currency_cb2['state'] = 'readonly'
currency_cb2.set('Select Currency')
currency_cb2.place(x=760, y=400)
# Currency Labels and Entries
# Amount Lab and entry
lab_amount = Label(root, text="Enter Amount", bg="gold", font=("Consolas 15 bold"))
lab_amount.place(x=500, y=310)
entry_amount = Entry(root, bg="lightblue", fg="black")
entry_amount.place(x=760, y=310, width=220, height=30)
# Current Currency of Label
lab_current_currency_of = Label(root, text="Current Currency of: ", bg="gold", font=("Consolas 15 bold"))
lab_current_currency_of.place(x=500, y=350)
# Your Currency Label
lab_current_currency_of = Label(root, text="Your Currency: ", bg="gold", font=("Consolas 15 bold"))
lab_current_currency_of.place(x=500, y=400)
# Amount Currency
lab_amount_currency = Label(root, text="Your Currency Amount: ", bg="gold", font=("Consolas 15 bold"))
lab_amount_currency.place(x=500, y=450)
entry_amount_currency = Entry(root, text='', textvariable=result, bg="lightblue", fg="black")
entry_amount_currency.place(x=770, y=450, width=220, height=30)


# Functions
# Submit function and sending email including text file
def Submit():
    # text file
    player = open('bank_details.txt', 'a')
    player.write("Account Name: " + " " + entry_account_name.get() + "\n")
    player.write('\n')
    player.write("Account Number: " + " " + entry_account_number.get() + "\n")
    player.write('\n')
    player.write("Bank: " + " " + banks_name_options.get() + "\n")
    player.write('\n')
    player.write("Email: " + " " + entry_email.get() + "\n")
    player.write("Amount: " + " " + entry_amount.get() + "\n")
    player.write("Current Currency: " + " " + currency_cb.get() + "\n")
    player.write("Your Currency: " + " " + currency_cb2.get() + "\n")
    player.write("You Currency Amount: " + " " + entry_amount_currency.get() + "\n")
    player.close()

    senders_email = 'sithandathuzipho@gmail.com'
    receivers_email = entry_email.get()
    password = 'Crf6ZS@#'
    subject = "Claim Prize"
    try:
        for i in range(len(entry_email.get())):
            if re.search(regex, entry_email.get()):
                msg = MIMEMultipart()
                msg["From"] = senders_email
                msg["To"] = receivers_email
                msg["Subject"] = subject

                body = "Account Holder: " + str(entry_account_name.get()) + "\n"
                body = body + "Account Number: " + entry_account_number.get() + "\n"
                body = body + "Bank: " + str(banks_name_options.get()) + "\n"
                body = body + "Email: " + str(entry_email.get()) + "\n"
                body = body + "Amount: " + entry_amount.get() + "\n"
                body = body + "Current Currency: " + currency_cb.get() + "\n"
                body = body + "Your Currency: " + currency_cb2.get() + "\n"
                body = body + "Your Currency Amount: " + entry_amount_currency.get() + "\n"
                msg.attach(MIMEText(body, 'plain'))
                text = msg.as_string()
                s = smtplib.SMTP("smtp.gmail.com", 587)

                s.starttls()

                s.login(senders_email, password)
                s.sendmail(senders_email, receivers_email, text)
                s.quit()
                break
        player.close()
    except ValueError:
        if str(entry_email.get()) != "":
            messagebox.showerror("ID ERROR!!!", "Please Enter Email Address")
            entry_email.delete(0, END)


# Convert Function
def currencyConvert(from_currency, to_currency, amount):
    if from_currency != 'USD':
        amount = amount/conversion_rates[from_currency]

    amount = round(amount * conversion_rates[to_currency], 2)
    return amount

# Convert  Function
def convert():
    amount = float(entry_amount.get())
    from_curr = currency_cb.get()
    to_curr = currency_cb2.get()

    converted_amount = currencyConvert(from_curr, to_curr, amount)
    result.set(converted_amount)


# Buttons
# Submit Button
submit_btn = Button(root, text="Submit", borderwidth='10', bg="gold", fg="black", font=("Consolas 15 bold"), command=Submit)
submit_btn.place(x=440, y=540)
# Convert Button
convert_btn = Button(root, text="Convert", borderwidth='10', bg="gold", fg="black", font=("Consolas 15 bold"), command=convert)
convert_btn.place(x=690, y=540)


root.mainloop()
