#!/usr/bin/env python
'''
 ____ _____ _   _ ____  _____ _   _ _____
/ ___|_   _| | | |  _ \| ____| \ | |_   _|
\___ \ | | | | | | | | |  _| |  \| | | |
 ___) || | | |_| | |_| | |___| |\  | | |
|____/ |_|  \___/|____/|_____|_| \_| |_|

 ___ _   _ _____ ___  ____  __  __    _  _____ ___ ___  _   _
|_ _| \ | |  ___/ _ \|  _ \|  \/  |  / \|_   _|_ _/ _ \| \ | |
 | ||  \| | |_ | | | | |_) | |\/| | / _ \ | |  | | | | |  \| |
 | || |\  |  _|| |_| |  _ <| |  | |/ ___ \| |  | | |_| | |\  |
|___|_| \_|_|   \___/|_| \_\_|  |_/_/   \_\_| |___\___/|_| \_|

 __  __    _    _   _    _    ____ _____ ____
|  \/  |  / \  | \ | |  / \  / ___| ____|  _ \
| |\/| | / _ \ |  \| | / _ \| |  _|  _| | |_) |
| |  | |/ ___ \| |\  |/ ___ \ |_| | |___|  _ <
|_|  |_/_/   \_\_| \_/_/   \_\____|_____|_| \_\

OAKVILLE TSA PROJECT 2017

Student Information Manager (SIM)
Manages student information from a teacher/administrative perspective while also
allowing the student to take tests, look at grades, look at homework, email,and
more. Parents also can see their kids progress in school.

Credits:
Garrett Summerfield - i <3 linux
Thomas Gleiforst - Best Programmer here
Hannah Jokuti - Thomas's partner in crime
Alisa Lazareva - LASANGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

'''

#IMPORTS
import Tkinter
import tkFont
import math
import random
from Tkinter import *

############################################
#VARIABLES, LISTS, ETC. ALL INITIALIZE HERE#
############################################
key = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
users = []

################
#FUNCTIONS HERE#
################

#Encrypt and Decrypt passwords
def encrypt(phrase):
    encrypted = ''
    key = []
    for i in range(len(phrase)):
        key.append(random.randint(1,9))
        for j in range(len(alphabet)):
           if phrase[i] == alphabet[j]:
                j += key[i]
 		encrypted += alphabet[j]
    return encrypted

    
def decrypt(phrase, code):
    decrypted = ''
    for i in range(len(phrase)):
        for j in range(len(alphabet)):
            if phrase[i] == alphabet[j]:
                j -= code[i]
                decrypted += alphabet[j]
    return decrypted

def loginAttempt():
    if usernameB.get() in users:
        
    else:
        users.append(usernameB.get()

####################################
#CANVAS, WIDGETS, AND DRAWINGS HERE#
####################################
#Basic initlization
rootMain = Tkinter.Tk()
rootMain.title("SIM - Student Information Manager")
rootMain.minsize(600,600)
canvas = Tkinter.Canvas(rootMain, width=900, height=600, background='#FFFFFF')
canvas.grid(row=0, rowspan=50, column=4)

#Username and Password Entry Boxes (WIP)
usernameL = Tkinter.Label(rootMain, text="Username:")
usernameB = Tkinter.Entry(rootMain)
passwordL = Tkinter.Label(rootMain, text="Password:")
passwordB = Tkinter.Entry(rootMain)
submit = Tkinter.Button(rootMain, text="Submit", command=loginAttempt)

#Place widgets on grid
usernameL.grid(row=0,column=0)
usernameB.grid(row=1,column=0)
passwordL.grid(row=2,column=0)
passwordB.grid(row=3,column=0)
submit.grid(row=4,column=0)

###############################
#MUST BE THE LAST LINE OF CODE#
############################### 
rootMain.mainloop()