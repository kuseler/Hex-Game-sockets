from tkinter import *

root = Tk()
root.title('Game')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
bg = PhotoImage(file = "camouflage.png") 
label1 = Label( root, image = bg) 
label1.place(x = 0, y = 0) 
  


# Feld
feld = Label(master=root, text='', bg='gray', font=('Arial', 36))
feld.place(x=40, y=40, width=800, height=600)

# Geldanzeige
text = Label(master=root, text='Geld:', bg='#008800', font=('Arial', 30))
text.place(x=1150, y=75, width=230, height=60)
geldAnzeige = Label(master=root, text='', bg='#008800', font=('Arial', 36))
geldAnzeige.place(x=1150, y=125, width=230, height=60)

# Button
buttonRundeBeenden = Button(master=root, text='Runde beenden', bg='#008800', font=('Arial', 20), command='')
buttonRundeBeenden.place(x=1150, y=575, width=230, height=60)
buttonZugBeenden = Button(master=root, text='Zug beenden', bg='#008800', font=('Arial', 20), command='')
buttonZugBeenden.place(x=1150, y=475, width=230, height=60)



root.mainloop()
