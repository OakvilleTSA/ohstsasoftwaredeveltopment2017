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
users = [{'username': '', 'grades': {'English': 100, 'Math': 100, 'Social Studies': 100, 'Science': 100}, 'password': '', 'code': [], 'first': 'ad', 'last': 'min', 'role': 'student'}]



################
#FUNCTIONS HERE#
################
'''For functions that need to be BEFORE the initlization of the canvas'''

#Encrypt and Decrypt passwords
def encrypt(phrase):
    phrase = phrase.lower()
    encrypted = ''
    key = []
    for i in range(len(phrase)):
        key.append(random.randint(1,9))
        for j in range(len(alphabet)):
           if phrase[i] == alphabet[j]:
                j += key[i]
                if j > 26:
                    j -= 26
 		encrypted += alphabet[j]
    return encrypted, key

    
def decrypt(phrase, code):
    decrypted = ''
    for i in range(len(phrase)):
        for j in range(len(alphabet)):
            if phrase[i] == alphabet[j]:
                j -= code[i]
                if j < 0:
                    j += 26
                decrypted += alphabet[j]
    return decrypted

def loginAttempt():
    userid = str(usernameB.get())
    match = False
    for account in users:
        if userid == account['username']:
            if decrypt(account['password'], account['code']) == passwordB.get().lower():
                #open next screen
                print 'In the system'
                match = True
                sim(account)
    else:
        if match == False:
            newUser(userid)
        
def newUser(userid):
    rootLogin.destroy()
    rootNew = Tkinter.Tk()
    rootNew.title("SIM - New User")
    rootNew.overrideredirect(False)
    rootNew.minsize(400, 250)
    Label(rootNew, text="New User Detected", font=("Arial", 20)).grid(row=0, column=0)
    Label(rootNew, text="Please indicate if you are a student or teacher", font=("Arial", 15)).grid(row=1, column=0)
    role = '' #####THESE ARE THE LINES NOT WORKING - ROLE WON'T CHANGE#####
    Radiobutton(rootNew, text="Teacher", value="teacher", variable=role).grid(row=2, column=0)#####
    Radiobutton(rootNew, text="Student", value="student", variable=role).grid(row=3, column=0)#####
    Tkinter.Label(rootNew, text="First Name:").grid(row=4, column=0)
    ent1 = Tkinter.Entry(rootNew)
    ent1.grid(row=5, column=0)
    Tkinter.Label(rootNew, text="Last Name:").grid(row=6, column=0)
    ent2 = Tkinter.Entry(rootNew)
    ent2.grid(row=7, column=0)
    
    ###Odd placement but this is where it has to be
    def create():
        password, key = encrypt(passwordB.get())
        user = {'username': userid,
                'password': password,
                'first': ent1.get(),
                'last': ent2.get(),
                'role': role.get(),#####
                'code': key,
                'grades': { 'English': 0,
                            'Math': 0,
                            'Social Studies': 0,
                            'Science': 0 } }
        users.append(user)
        print user ##For testing purposes##
        rootNew.destroy()
    ###
    
    create = Tkinter.Button(rootNew, text="Create", command=create)
    create.grid(row=8, column=0)

####################################
#CANVAS, WIDGETS, AND DRAWINGS HERE#
####################################
#Basic initlization
rootLogin = Tkinter.Tk()
rootLogin.title("SIM - Student Information Manager")
rootLogin.minsize(200,300)
title = Tkinter.Label(rootLogin, text="Student \nInformation \nManager", font=("Arial", 30))
title.grid(row=0,column=0)

#Username and Password Entry Boxes (WIP)
usernameL = Tkinter.Label(rootLogin, text="Username:")
usernameB = Tkinter.Entry(rootLogin)
passwordL = Tkinter.Label(rootLogin, text="Password:")
passwordB = Tkinter.Entry(rootLogin)
submit = Tkinter.Button(rootLogin, text="Submit", command=loginAttempt)

#Place widgets on grid
usernameL.grid(row=1,column=0)
usernameB.grid(row=2,column=0)
passwordL.grid(row=3,column=0)
passwordB.grid(row=4,column=0)
submit.grid(row=5,column=0)




#####################
#MORE FUNCTIONS HERE#
#####################
'''For functions that need to be AFTER the initlization of the canvas'''

def sim(account):
    def viewGrades():
        rootGrades = Tkinter.Tk()
        rootGrades.title("SIM - Student Information Manager")
        rootGrades.minsize(400,400)
        grades = account['grades']
        Tkinter.Label(rootGrades, text="Student Information Manager", font=("Arial", 30)).grid(row=0, column=0, columnspan=3)
        Tkinter.Label(rootGrades, text=account['first'] + " " + account['last'], font=("Arial", 20)).grid(row=1, column=0, columnspan=3)
        Tkinter.Label(rootGrades, text='GRADES:', font=("Arial", 15)).grid(row=2, column=1)
        Tkinter.Label(rootGrades, text='English: ' + str(grades['English']), font=("Arial", 15)).grid(row=3, column=1)
        Tkinter.Label(rootGrades, text='Math: ' + str(grades['Math']), font=("Arial", 15)).grid(row=4, column=1)
        Tkinter.Label(rootGrades, text='Social Studies: ' + str(grades['Social Studies']), font=("Arial", 15)).grid(row=5, column=1)
        Tkinter.Label(rootGrades, text='Science: ' + str(grades['Science']), font=("Arial", 15)).grid(row=6, column=1)

    def takeTest():
        print 'Test taken'
    def vAssignments():
        print 'Assignments viewed'
    def cAssignments():
        print 'Assignments completed'    
    rootLogin.destroy()
    rootSim = Tkinter.Tk()
    rootSim.title("SIM - Student Information Manager")
    rootSim.minsize(400,400)
    if account['role'] == 'student':
        Tkinter.Label(rootSim, text="Student Information Manager", font=("Arial", 30)).grid(row=0, column=0, columnspan=2)
        Tkinter.Label(rootSim, text=account['first'] + " " + account['last'], font=("Arial", 20)).grid(row=1, column=0, columnspan=2)
        grades = Tkinter.Button(rootSim, text="View \nGrades", command=viewGrades, width=15, height=5, bg="light gray", font=("Arial", 20)).grid(row=2, column=0)
        test = Tkinter.Button(rootSim, text="Take A \nTest", command=takeTest, width=15, height=5, bg="light gray", font=("Arial", 20)).grid(row=2, column=1)
        Tkinter.Label(rootSim).grid(row=3)
        viewAssignments = Tkinter.Button(rootSim, text="View \nAssignments", command=vAssignments, width=15, height=5, bg="light gray", font=("Arial", 20)).grid(row=4, column=0)
        createAssignments = Tkinter.Button(rootSim, text="Complete an \nAssignment", command=cAssignments, width=15, height=5, bg="light gray", font=("Arial", 20)).grid(row=4, column=1)

    

###############################
#MUST BE THE LAST LINE OF CODE#
############################### 
def start():
    rootLogin.mainloop()