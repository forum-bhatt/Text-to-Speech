from tkinter import *
import pygame
import pyttsx3

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
image = Disp.create_image(85, 62, image = img)

# main screen
Display = Entry(frame1, textvariable=str1, font=('arial', 44, 'bold'), bg='blue', fg='white', bd=34, width=39, justify=CENTER)
Display.grid(row=0, column=0, columnspan=7, pady=1)

# row 1
btnA = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='A', bg='orange', fg='white')\
    .grid(row=1, column=0)
btnB = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='B', bg='orange', fg='white')\
    .grid(row=1, column=1)
btnC = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='C', bg='orange', fg='white')\
    .grid(row=1, column=2)
btnD = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='D', bg='orange', fg='white')\
    .grid(row=1, column=4)
btnE = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='E', bg='orange', fg='white')\
    .grid(row=1, column=5)
btnF = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='F', bg='orange', fg='white')\
    .grid(row=1, column=6)

#  row 2
btnG = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='G', bg='orange', fg='white')\
    .grid(row=2, column=0)
btnH = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='H', bg='blue', fg='white')\
    .grid(row=2, column=1)
btnI = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='I', bg='blue', fg='white')\
    .grid(row=2, column=2)
btnJ = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='J', bg='blue', fg='white')\
    .grid(row=2, column=3)
btnK = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='K', bg='blue', fg='white')\
    .grid(row=2, column=4)
btnL = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='L', bg='blue', fg='white')\
    .grid(row=2, column=5)
btnM = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='M', bg='orange', fg='white')\
    .grid(row=2, column=6)

# row 3
btnN = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='N', bg='orange', fg='white')\
    .grid(row=3, column=0)
btnO = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='O', bg='orange', fg='white')\
    .grid(row=3, column=1)
btnP = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='P', bg='orange', fg='white')\
    .grid(row=3, column=2)
btnQ = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='Q', bg='orange', fg='white')\
    .grid(row=3, column=3)
btnR = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='R', bg='orange', fg='white')\
    .grid(row=3, column=4)
btnS = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='S', bg='orange', fg='white')\
    .grid(row=3, column=5)
btnT = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='T', bg='orange', fg='white')\
    .grid(row=3, column=6)

# row 4

btnU = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='U', bg='orange', fg='white')\
    .grid(row=4, column=0)
btnV = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='V', bg='orange', fg='white')\
    .grid(row=4, column=1)
btnW = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='W', bg='orange', fg='white')\
    .grid(row=4, column=2)
btnX = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='X', bg='orange', fg='white')\
    .grid(row=4, column=3)
btnY = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='Y', bg='orange', fg='white')\
    .grid(row=4, column=4)
btnZ = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='Z', bg='orange', fg='white')\
    .grid(row=4, column=5)
btnClear = Button(frame1, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text='Clear', bg='white', fg='Black')\
    .grid(row=4, column=6)





root.mainloop()

