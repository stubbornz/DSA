# importing libraries
from tkinter import *
from math import sqrt, factorial

# initializing tkinter
root = Tk()

# fixing color and fonts
BACKGROUNDCOLOR = "red"
FONTS = "Times 33 overstrike"


# size of the tkinter window
root.geometry("348x390")
root.minsize(348, 390)
root.maxsize(348, 390)
root.title("Calculator")
# background color of tkinter window
root.configure(bg=BACKGROUNDCOLOR)

# Creating frames
frame = Frame(root, relief=SUNKEN, borderwidth=6, bg=BACKGROUNDCOLOR)
frame.pack(pady=1)
frame1 = Frame(root, relief=SUNKEN, borderwidth=6, bg=BACKGROUNDCOLOR)
frame1.pack(pady=1)
frame2 = Frame(root, relief=SUNKEN, borderwidth=6, bg=BACKGROUNDCOLOR)
frame2.pack(pady=1)
frame3 = Frame(root, relief=SUNKEN, borderwidth=6, bg=BACKGROUNDCOLOR)
frame3.pack(pady=1)
frame4 = Frame(root, relief=SUNKEN, borderwidth=6, bg=BACKGROUNDCOLOR)
frame4.pack(pady=1)
frame5 = Frame(root, relief=SUNKEN, borderwidth=6, bg=BACKGROUNDCOLOR)
frame5.pack(pady=1)

# Creating entry widgets
entry = Entry(frame, relief=SUNKEN, borderwidth=4, bg=BACKGROUNDCOLOR, font=FONTS, fg="white")
entry.pack()

# Creating function for updating values from entry widgets
def button_click(char):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(char))


def button_clear():
    entry.delete(0, END)

def delete():
    current = entry.get()
    entry.delete(0, END)
    length = len(current)
    string = current[0: length-1]
    entry.insert(0, string)

# it can oerforms one calculation at a time
def equals():
    string = entry.get()
    k = 0

    availableCharacters = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!',
        '+', 'X', '-', '^', '÷', '%', '√'
                            ]
    loop = 1
    oneCharacter = ['!', '+', 'X', '-', '^', '÷', '%', '√']
    for i in string:
        if i in oneCharacter:
            loop -= 1

    for i in string:
        if i in availableCharacters:
            loop += 1

    if loop == len(string):
        for i in string:
            k += 1
            if i == '+':
                start = string[0: k - 1]
                end = string[k: len(string)]
                entry.delete(0, END)
                entry.insert(0, str(int(start) + int(end)))
            elif i == '-':
                start = string[0: k - 1]
                end = string[k: len(string)]
                entry.delete(0, END)
                entry.insert(0, str(int(start) - int(end)))
            elif i == 'X':
                start = string[0: k - 1]
                end = string[k: len(string)]
                entry.delete(0, END)
                entry.insert(0, str(int(start) * int(end)))
            elif i == '÷':
                start = string[0: k - 1]
                end = string[k: len(string)]
                entry.delete(0, END)
                entry.insert(0, str(int(start) / int(end)))
            elif i == '%':
                start = string[0: k - 1]
                end = string[k: len(string)]
                entry.delete(0, END)
                entry.insert(0, str(int(start) % int(end)))
            elif i == '^':
                start = string[0: k - 1]
                end = string[k: len(string)]
                entry.delete(0, END)
                entry.insert(0, str(pow(int(start), int(end))))
            elif i == '√':
                end = string[1: len(string)]
                entry.delete(0, END)
                entry.insert(0, str(sqrt(int(end))))
            elif i == '!':
                start = string[0: k - 1]
                entry.delete(0, END)
                entry.insert(0, str(factorial(int(start))))
    else:
        entry.delete(0, END)
        entry.insert(0, "ERROR")

# Creating Button widgets
# row-1
b1 = Button(frame1, text="1", fg=BACKGROUNDCOLOR, font=FONTS, padx=22, pady=5, command=lambda: button_click(1))
b1.pack(side=LEFT)
b2 = Button(frame1, text="2", fg=BACKGROUNDCOLOR, font=FONTS, padx=22, pady=5, command=lambda: button_click(2))
b2.pack(side=LEFT)
b3 = Button(frame1, text="3", fg=BACKGROUNDCOLOR, font=FONTS, padx=22, pady=5, command=lambda: button_click(3))
b3.pack(side=LEFT)
b4 = Button(frame1, text="4", fg=BACKGROUNDCOLOR, font=FONTS, padx=22, pady=5, command=lambda: button_click(4))
b4.pack(side=LEFT)
badd = Button(frame1, text="+", fg=BACKGROUNDCOLOR, font=FONTS, padx=22, pady=5, command=lambda: button_click('+'))
badd.pack(side=LEFT)

# row-2
b5 = Button(frame2, text="5", fg=BACKGROUNDCOLOR, font=FONTS, padx=23, pady=5, command=lambda: button_click(5))
b5.pack(side=LEFT)
b6 = Button(frame2, text="6", fg=BACKGROUNDCOLOR, font=FONTS, padx=23, pady=5, command=lambda: button_click(6))
b6.pack(side=LEFT)
b7 = Button(frame2, text="7", fg=BACKGROUNDCOLOR, font=FONTS, padx=23, pady=5, command=lambda: button_click(7))
b7.pack(side=LEFT)
b8 = Button(frame2, text="8", fg=BACKGROUNDCOLOR, font=FONTS, padx=23, pady=5, command=lambda: button_click(8))
b8.pack(side=LEFT)
bsub = Button(frame2, text="-", fg=BACKGROUNDCOLOR, font=FONTS, padx=23, pady=5, command=lambda: button_click('-'))
bsub.pack(side=LEFT)

# row-3
b9 = Button(frame3, text="9", fg=BACKGROUNDCOLOR, font=FONTS, padx=21, pady=5, command=lambda: button_click(9))
b9.pack(side=LEFT)
b0 = Button(frame3, text="0", fg=BACKGROUNDCOLOR, font=FONTS, padx=21, pady=5, command=lambda: button_click(0))
b0.pack(side=LEFT)
bclear = Button(frame3, text="C", fg=BACKGROUNDCOLOR, font=FONTS, padx=21, pady=5, command=button_clear)
bclear.pack(side=LEFT)
bmul = Button(frame3, text="X", fg=BACKGROUNDCOLOR, font=FONTS, padx=21, pady=5, command=lambda: button_click('X'))
bmul.pack(side=LEFT)
bdiv = Button(frame3, text="÷", fg=BACKGROUNDCOLOR, font=FONTS, padx=21, pady=5, command=lambda: button_click('÷'))
bdiv.pack(side=LEFT)

# row-4
brem = Button(frame4, text="rem", fg=BACKGROUNDCOLOR, font=FONTS, padx=13, pady=5, command=lambda: button_click('%'))
brem.pack(side=LEFT)
bpower = Button(frame4, text="pow", fg=BACKGROUNDCOLOR, font=FONTS, padx=13, pady=5, command=lambda: button_click('^'))
bpower.pack(side=LEFT)
bsqrt = Button(frame4, text="sqrt", fg=BACKGROUNDCOLOR, font=FONTS, padx=13, pady=5, command=lambda: button_click('√'))
bsqrt.pack(side=LEFT)
bfact = Button(frame4, text="fact", fg=BACKGROUNDCOLOR, font=FONTS, padx=13, pady=5, command=lambda: button_click('!'))
bfact.pack(side=LEFT)

# row-5
beq = Button(frame5, text="=", fg=BACKGROUNDCOLOR, font=FONTS, padx=100, pady=5, command=equals)
beq.pack(side=LEFT)
bdel = Button(frame5, text="del", fg=BACKGROUNDCOLOR, font=FONTS, padx=80, pady=5, command=delete)
bdel.pack(side=LEFT)

# repeating tkinter loop
root.mainloop()
