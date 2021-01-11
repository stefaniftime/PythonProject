from tkinter import *
import random
import time
import subprocess
import pygame.mixer
import simpleaudio as sa

random.seed()
pygame.mixer.init()
root = Tk()
root.geometry("%dx%d%+d%+d"%(root.winfo_screenwidth(),root.winfo_screenheight(), 0, 20))
root.title("WAR!")
numbers = ['2','3','4','5','6','7','8','9','T','A','J','Q','K']
suits = ["clubs","hearts","spades","diamonds"]
buttons = {}
deck1 = []
deck2 = []
center = {"d1":[],"d2":[]}
label1 = Label(root, width = 50, height = 3)
label2 = Label(root, width = 50, height = 3)
label1.place_configure(x=0, y=0)
label2.place_configure(x=0, y=350)
label1.pack()
label2.pack()
x = 0
y = 50
x2 = 0
y2 = 50

def get_posscards():
    global posscards
    posscards = []
    for i in numbers:
        for j in suits:
            posscards.append(i+"_of_"+j+".gif")

def create_random_card(xpos, ypos, col = False):
    img = PhotoImage(file = random.choice(numbers)+"_of_"+random.choice(suits)+".gif")
    button = Label(root, image=img)
    button.img = img
    if col:
        button.grid(row = xpos, column = ypos)
    else:
        button.place_configure(x = xpos, y = ypos)
    buttons.append(button)
def create_card(name, undername, xpos, ypos, typ, col=False):
    img = PhotoImage(file="resources/"+name)
    button = Button(root, image = img)
    button.config(command = lambda undername = undername: flip(button, undername))
    button.img = img
    button.subimg = undername
    button.typ = typ
    button.name = name
    buttons[undername] = button
    if col:
        button.grid(row = xpos, column = ypos)
    else:
        button.place_configure(x = xpos,y = ypos)




