from tkinter import *

import pygame
import pyttsx3
from PIL import Image, ImageTk

pygame.init()
engine = pyttsx3.init()
root = Tk()
root.title('Alphabet Application')
root.geometry('1352x652+0+0')
root.config(background='white')

str1 = StringVar()
str1.set('Welcome to Kidzee Academy')
ABC = Frame(root, bg='white')
ABC.grid()

# define frame1
frame1 = Frame(ABC, bg='white')
frame1.grid()

Disp = Canvas(frame1, width=160, height=120, bg='white')
Disp.grid(row=1, column=3)
img = PhotoImage(file='Icon.png')
image = Disp.create_image(85, 62, image=img)

imgClear = PhotoImage(file='Icon.png')
def Clear():
    str1.set('Welcome to Kidzee Academy')
    Disp.create_image(85, 62, image=imgClear)
    engine.say('Welcome to Kidzee Academy')
    engine.runAndWait()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def Alphabet(alphabet):
    # alphabet to fruit mapping
    fruit_dict = {
        'A': 'Apple',
        'B': 'Banana',
        'C': 'Cocoa',
        'D': 'Damson',
        'E': 'Elderberry',
        'F': 'Fig',
        'G': 'Guava',
        'H': 'Huckleberry',
        'I': 'Ita Palm',
        'J': 'Jujube',
        'K': 'Kumquat',
        'L': 'Lime',
        'M': 'Mango',
        'N': 'Nance',
        'O': 'Orange',
        'P': 'Papaya',
        'Q': 'Quince',
        'R': 'Raspberry',
        'S': 'Strawberry',
        'T': 'Tamarind',
        'U': 'Ugli',
        'V': 'Vanilla',
        'W': 'Watermelon',
        'X': 'Xigua',
        'Y': 'Yuzu',
        'Z': 'Zucchini',
    }
    fruit_name = fruit_dict.get(alphabet, 'Unknown Fruit')
    str1.set(f'{alphabet} is for {fruit_name}')

    # load corresponding image based on the alphabet
    image_path = f'{fruit_name}.png'
    image = Image.open(image_path)
    alphabet_image = ImageTk.PhotoImage(image)

    Disp.delete('all')
    Disp.create_image(85, 62, image=alphabet_image)
    Disp.image = alphabet_image  # Store a reference to prevent garbage collection

    # Speak the text
    speak_text(f'{alphabet} is for {fruit_name}')

# main screen
Display = Entry(frame1, textvariable=str1, font=('arial', 44, 'bold'), bg='blue', fg='white', bd=34, width=39,
                justify=CENTER)
Display.grid(row=0, column=0, columnspan=7, pady=1)

# row 1
btnA = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('A'), width=10, height=3,
              text='A', bg='orange', fg='white')
btnA.grid(row=1, column=0)

btnB = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('B'), width=10, height=3,
              text='B', bg='blue', fg='white')
btnB.grid(row=1, column=1)

btnC = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('C'), width=10, height=3,
              text='C', bg='blue', fg='white')
btnC.grid(row=1, column=2)

btnD = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('D'), width=10, height=3,
              text='D', bg='blue', fg='white')
btnD.grid(row=1, column=4)

btnE = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('E'), width=10, height=3,
              text='E', bg='blue', fg='white')
btnE.grid(row=1, column=5)

btnF = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('F'), width=10, height=3,
              text='F', bg='orange', fg='white')
btnF.grid(row=1, column=6)

#  row 2
btnG = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('G'), width=10, height=3,
              text='G', bg='orange', fg='white')
btnG.grid(row=2, column=0)

btnH = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('H'), width=10, height=3,
              text='H', bg='blue', fg='white')
btnH.grid(row=2, column=1)

btnI = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('I'), width=10, height=3,
              text='I', bg='blue', fg='white')
btnI.grid(row=2, column=2)

btnJ = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('J'), width=10, height=3,
              text='J', bg='blue', fg='white')
btnJ.grid(row=2, column=3)

btnK = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('K'), width=10, height=3,
              text='K', bg='blue', fg='white')
btnK.grid(row=2, column=4)

btnL = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('L'), width=10, height=3,
              text='L', bg='blue', fg='white')
btnL.grid(row=2, column=5)

btnM = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('M'), width=10, height=3,
              text='M', bg='orange', fg='white')
btnM.grid(row=2, column=6)


# row 3
btnN = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('N'), width=10, height=3,
              text='N', bg='orange', fg='white')
btnN.grid(row=3, column=0)

btnO = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('O'), width=10, height=3,
              text='O', bg='blue', fg='white')
btnO.grid(row=3, column=1)

btnP = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('P'), width=10, height=3,
              text='P', bg='blue', fg='white')
btnP.grid(row=3, column=2)

btnQ = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('Q'), width=10, height=3,
              text='Q', bg='blue', fg='white')
btnQ.grid(row=3, column=3)

btnR = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('R'), width=10, height=3,
              text='R', bg='blue', fg='white')
btnR.grid(row=3, column=4)

btnS = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('S'), width=10, height=3,
              text='S', bg='blue', fg='white')
btnS.grid(row=3, column=5)

btnT = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('T'), width=10, height=3,
              text='T', bg='orange', fg='white')
btnT.grid(row=3, column=6)

# row 4

btnU = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('U'), width=10, height=3,
              text='U', bg='orange', fg='white')
btnU.grid(row=4, column=0)
btnV = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('V'), width=10, height=3,
              text='V', bg='orange', fg='white')
btnV.grid(row=4, column=1)
btnW = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('W'), width=10, height=3,
              text='W', bg='orange', fg='white')
btnW.grid(row=4, column=2)
btnX = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('X'), width=10, height=3,
              text='X', bg='orange', fg='white')
btnX.grid(row=4, column=3)
btnY = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('Y'), width=10, height=3,
              text='Y', bg='orange', fg='white')
btnY.grid(row=4, column=4)
btnZ = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=lambda: Alphabet('Z'), width=10, height=3,
              text='Z', bg='orange', fg='white')
btnZ.grid(row=4, column=5)
btnClear = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), command=Clear, width=10, height=3, text='Clear', bg='white',
                  fg='Black')
btnClear.grid(row=4, column=6)

root.mainloop()
