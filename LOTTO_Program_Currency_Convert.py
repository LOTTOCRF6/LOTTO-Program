
from tkinter import *
from tkinter import ttk
import requests

root = Tk()
root. title("Currency Convertor Challenge")
root.geometry("400x400")

my_pic = PhotoImage(file="resize-currency.png")
background = Label(root, image=my_pic).place(x=0, y=0)

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
currency_cb.place(x=200, y=80)

currency2 = []
for i in conversion_rates.keys():
    currency.append(i)

currency_cb2 = ttk.Combobox(root)
currency_cb2['values'] = currency
currency_cb2['state'] = 'readonly'
currency_cb2.set('Select Currency')
currency_cb2.place(x=200, y=120)


# SUB-header
header_lab = Label(root, text="Welcome To Currency Convertor", bg="cyan1")
header_lab.place(x=130, y=5)

# Amount to Convert
amount_lab = Label(root, text="Enter Amount:", bg="cyan1")
amount_lab.place(x=5, y=50)
amount_entry = Entry(root)
amount_entry.place(x=200, y=50)

# From Currency Covert
fromcurr_lab = Label(root, text="Convert Currency Of:", bg="cyan1")
fromcurr_lab.place(x=5, y=80)

tocurr_lab = Label(root, text="To Currency Of:", bg="cyan1")
tocurr_lab.place(x=5, y=120)


new_curr_amountlab = Label(root, text="New Currency Amount is:", bg="cyan1")
new_curr_amountlab.place(x=5, y=230)
new_curr_amountEntry = Entry(root, text='', textvariable=result)
new_curr_amountEntry.place(x=200, y=230)


def currencyConvert(from_currency, to_currency, amount):
    if from_currency != 'USD':
        amount = amount/conversion_rates[from_currency]

    amount = round(amount * conversion_rates[to_currency], 2)
    return amount


def convertSwitch():
    amount = float(amountentry.get())
    from_curr = currency_cb.get()
    to_curr = currency_cb2.get()

    converted_amount = currencyConvert(from_curr, to_curr, amount)
    result.set(converted_amount)


def clean():
    amountentry.delete(0, END)
    new_curr_amountEntry.delete(0, END)
    currency_cb.set("Select Currency")
    currency_cb2.set("Select Currency")


btn1 = Button(root, text="Convert", command=convertSwitch, bg="cyan1")
btn1.place(x=200, y=180)
btn2 = Button(root, text="Clear", command=clean, bg="cyan1")
btn2.place(x=200, y=260)


root.mainloop()