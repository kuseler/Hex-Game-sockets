from tkinter import *

root = Tk()
root.title('Game')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


# Feld
feld = Label(master=root, text='', bg='gray', font=('Arial', 36))
feld.place(x=40, y=40, width=800, height=600)

# Button
button = Button(master=root, text='Runde beenden', bg='#008800', font=('Arial', 20), command='')
button.place(x=1150, y=575, width=230, height=60)


root.mainloop()
