from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.title('Game')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
bg = PhotoImage(file = "camouflage.png") 
label1 = Label( root, image = bg) 
label1.place(x = 0, y = 0) 
  
role=False
role = messagebox.askyesno('Yes|No', 'Do you want to proceed as Host?')
print(role)
if role == True:
    role = "Server"
    print(role)
else:
    role = "Client"
    print(role)

# Feld
frame = Frame(master=root, bg='gray')
frame.place(x=40, y=40, width=800, height=600)
label = Label(master=root, bg='gray')
label.place(x=985, y=200, width=550, height=250)

def getMouse(event):
    x = frame.winfo_pointerx()-40
    y = frame.winfo_pointery()-60
    print(x,y)
    frame.unbind("<Button-1>")
    return x,y

def eventHandler():
    frame.bind("<Button-1>",getMouse)

def placeUnit():
    unit = PhotoImage(file = "unit1_friendly")
    newUnit = Label(frame, image = unit)
    
    

# Geldanzeige
text = Label(master=root, text='Geld:', bg='#008800', font=('Arial', 30))
text.place(x=1150, y=75, width=230, height=60)
geldAnzeige = Label(master=root, text='', bg='#008800', font=('Arial', 36))
geldAnzeige.place(x=1150, y=125, width=230, height=60)

# Button
buttonRundeBeenden = Button(master=root, text='Runde beenden', bg='#008800', font=('Arial', 20), command=eventHandler)
buttonRundeBeenden.place(x=1150, y=575, width=230, height=60)
buttonZugBeenden = Button(master=root, text='Zug beenden', bg='#008800', font=('Arial', 20),command=eventHandler)
buttonZugBeenden.place(x=1150, y=475, width=230, height=60)

buttonAttack = Button(master=root, text='Attack', bg='#008800', font=('Arial', 20), command='')
buttonAttack.place(x=995, y=210, width=200, height=100)
buttonMove = Button(master=root, text='Move', bg='#008800', font=('Arial', 20), command='')
buttonMove.place(x=1325, y=210, width=200, height=100)

if role=="Server":
    unit1 = PhotoImage(file = 'unit1_friendly.png')
    unit2 = PhotoImage(file = 'unit2_friendly.png')
    unit3 = PhotoImage(file = 'unit3_friendly.png')

else:
    unit1 = PhotoImage(file = 'unit1_hostile.png')
    unit2 = PhotoImage(file = 'unit2_hostile.png')
    unit3 = PhotoImage(file = 'unit3_hostile.png')

buttonUnit1 = Button(master=root, image=unit1, command=placeUnit)
buttonUnit1.place(x=995, y=340, width=140, height=100)
buttonUnit2 = Button(master=root, image=unit2, command='')
buttonUnit2.place(x=1190, y=340, width=140, height=100)
buttonUnit3 = Button(master=root, image=unit3, command='')
buttonUnit3.place(x=1385, y=340, width=140, height=100)



root.mainloop()
