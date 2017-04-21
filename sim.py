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


#VARIABLES, LISTS, ETC. ALL INITIALIZE HERE
key = ['']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(phrase):
    encrypted = ''
    for i in range(len(phrase)):
        key.append(rand.int(0,9))
        for j in range(len(alphabet)):
           if phrase[i] == alphabet[j]:
                j += key[i]
 		encrypted += alphabet[j]
    return encrypted
    
def decrypt(phrase):
    decrypted = ''
    for i in range(len(phrase)):
        for j in range(len(alphabet)):
            if phrase[i] == alphabet[j]:
                j -= key[i]
                decrypted += alphabet[j]
    return decrypted


