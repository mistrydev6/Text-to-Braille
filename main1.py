brailleDict={
    "A"	:	"⠁",
    "B"	:	"⠃",
    "C"	:	"⠉",
    "D"	:	"⠙",
    "E"	:	"⠑",
    "F"	:	"⠋",
    "G"	:	"⠛",
    "H"	:	"⠓",
    "I"	:	"⠊",
    "J"	:	"⠚",
    "K"	:	"⠅",
    "L"	:	"⠇",
    "M"	:	"⠍",
    "N"	:	"⠝",
    "O"	:	"⠕",
    "P"	:	"⠏",
    "Q"	:	"⠟",
    "R"	:	"⠗",
    "S"	:	"⠎",
    "T"	:	"⠞",
    "U"	:	"⠥",
    "V"	:	"⠧",
    "W"	:	"⠺",
    "X"	:	"⠭",
    "Y"	:	"⠽",
    "Z"	:	"⠵",
    "1"	:	"⠼⠁",
    "2"	:	"⠼⠃",
    "3"	:	"⠼⠉",
    "4"	:	"⠼⠙",
    "5"	:	"⠼⠑",
    "6"	:	"⠼⠋",
    "7"	:	"⠼⠛",
    "8"	:	"⠼⠓",
    "9"	:	"⠼⠊",
    "0"	:	"⠼⠚",
    " " :   " ",
    ","	:	"⠂",
    ";"	:	"⠆",
    ":"	:	"⠒",
    "."	:	"⠲",
    "?"	:	"⠦",
    "!"	:	"⠖",
    "\'"	:	"⠄",
    "“"	:	"⠄⠶",
    "“"	:	"⠘⠦",
    "”"	:	"⠘⠴",
    "\'"	:	"⠄⠦",
    "\'"	:	"⠄⠴",
    "("	:	"⠐⠣",
    ")"	:	"⠐⠜",
    "/"	:	"⠸⠌",
    "\ "	:	"⠸⠡",
}

import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Text To Braille Converter")
root.geometry("500x500")
root.configure(bg="white")

label = tk.Label(root, text="Text To Braille Converter", font=("Arial", 20), bg="white", fg="black")
label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 20), bg="white", fg="black")
entry.pack(pady=20)



def convert():
    a = entry.get()
    a = a.upper()
    for x in a:

        if x[0] in brailleDict:
            #print(brailleDict[x[0]], end="")
            textOut.insert(END, brailleDict[x[0]])
        elif x[0] == " ":
            #print(" ", end="")
            textOut.insert(END, " ")

def clear_text():
    entry.delete(0, END)
    textOut.delete(1.0, END)


button = tk.Button(root, text="Convert", font=("Arial", 20), bg="white", fg="black", command=convert)
button.pack(pady=20)

textOut = tk.Text(root,font=("Arial", 20), bg="white", fg="black", height=5, width=25)
textOut.pack(pady=10)

button2 = tk.Button(root, text="Clear", font=("Arial", 20), bg="white", fg="black", command=clear_text)
button2.pack(pady=15)

root.mainloop()





