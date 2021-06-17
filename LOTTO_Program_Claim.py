from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Lotto Price Claim")
root.geometry("800x800")
root.config(background="Grey")
root.resizable(0, 0)

img = PhotoImage(file="imgonline-com-ua-BrightContr-1jeVAauFh8h.png")
canvas = Canvas(root, width=2400, height=1600)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.pack()

# labels and entries


root.mainloop()