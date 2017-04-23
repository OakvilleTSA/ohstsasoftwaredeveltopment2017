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
allowing the student to take tests, look at grades, look at homework, and
more.

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
test = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5' , '6', '7', '8', '9']
users = [{'username': '', 'grades': {'English': 100, 'Math': 100, 'Social Studies': 100, 'Science': 100}, 'password': '', 'code': [], 'first': 'ad', 'last': 'min', 'role': 'teacher'}]



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
                    j -= len(alphabet)
 		encrypted += alphabet[j]
    return encrypted, key

    
def decrypt(phrase, code):
    decrypted = ''
    for i in range(len(phrase)):
        for j in range(len(alphabet)):
            if phrase[i] == alphabet[j]:
                j -= code[i]
                if j < 0:
                    j += len(alphabet)
                decrypted += alphabet[j]
    return decrypted

def loginAttempt():
    userid = str(usernameB.get())
    match = False
    for account in users:
        if userid == account['username']:
            match = True
            if decrypt(account['password'], account['code']) == passwordB.get().lower():
                #open next screen
                sim(account)
            else:
                Tkinter.Label(rootLogin, text="Incorrect Password").grid()
    else:
        if match == False:
            newUser(userid)
        
def newUser(userid):
    rootNew = Tkinter.Tk()
    rootNew.title("SIM - New User")
    rootNew.overrideredirect(False)
    rootNew.minsize(400, 250)
    Label(rootNew, text="New User Detected", font=("Arial", 20)).grid(row=0, column=0)
    Label(rootNew, text="Please indicate if you are a student or teacher", font=("Arial", 15)).grid(row=1, column=0)
    role = StringVar() 
    role.set("student")
    def teacher():
        role.set("teacher")
    def student():
        role.set("student")
    Radiobutton(rootNew, text="Teacher", variable=role, value="teacher", command=teacher).grid(row=2, column=0)
    Radiobutton(rootNew, text="Student", variable=role, value="student", command=student).grid(row=3, column=0)
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
                'role': role.get(),
                'code': key,
                'grades': { 'English': 0,
                            'Math': 0,
                            'Social Studies': 0,
                            'Science': 0 } }
        users.append(user)
        rootNew.destroy()
                

    ###
    
    create = Tkinter.Button(rootNew, text="Create", command=create)
    create.grid(row=8, column=0)

####################################
#CANVAS, WIDGETS, AND DRAWINGS HERE#
####################################
def init():
    global usernameB
    global passwordB
    global rootLogin
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

    rootLogin.mainloop()



#####################
#MORE FUNCTIONS HERE#
#####################
'''For functions that need to be AFTER the initlization of the canvas'''

def sim(account):
    rootLogin.destroy()
    if account['role'] == 'student':
        student(account)
    elif account['role'] == 'teacher':
        teacher(account)

def student(account):
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
        rootTestTaker = Tkinter.Tk()
        rootTestTaker.title("SIM - Student Information Manager")
        rootTestTaker.minsize(400,400)
        Tkinter.Label(rootTestTaker, text="Student Information Manager", font=("Arial", 30)).grid(row=0, column=0, columnspan=4)
        Tkinter.Label(rootTestTaker, text=account['first'] + " " + account['last'], font=("Arial", 20)).grid(row=1, column=0, columnspan=4)
        i = 0
        def quiz():
            for i in test:
                rootTestTaker = Tkinter.Tk()
                rootTestTaker.title("SIM - Student Information Manager")
                rootTestTaker.minsize(400,400)
                Tkinter.Label(rootTestTaker, text="Student Information Manager", font=("Arial", 30)).grid(row=0, column=0, columnspan=4)
                Tkinter.Label(rootTestTaker, text=account['first'] + " " + account['last'], font=("Arial", 20)).grid(row=1, column=0, columnspan=4)
    
                Tkinter.Label(rootTestTaker, text="Question:").grid(row=3, column=0)
                q = Tkinter.Text(rootTestTaker, height=3)
                q.grid(row=3, column = 1, rowspan=2, columnspan=3)
                
                answer = IntVar(rootTestTaker)
                answer.set(0)
    
                answer1 = Tkinter.Radiobutton(rootTestTaker, text="A. "+i[0], variable=answer, value=1)
                answer1.grid(row=5, column=1, columnspan=3)
    
                
                answer2 = Tkinter.Radiobutton(rootTestTaker, text="B. "+i[1], variable=answer, value=2)
                answer2.grid(row=6, column=1, columnspan=3)
    
                
                answer3 = Tkinter.Radiobutton(rootTestTaker, text="C. "+i[2], variable=answer, value=3)
                answer3.grid(row=7, column=1, columnspan=3)
    
                
                answer4 = Tkinter.Radiobutton(rootTestTaker, text="D. "+i[3], variable=answer, value=4)
                answer4.grid(row=8, column=1, columnspan=3)
    
            
                Tkinter.Button(rootTestTaker, text="Next Question", command=add).grid(row=9, column=1)
                Tkinter.Button(rootTestTaker, text="New Question", command=new).grid(row=9, column=2)
                Tkinter.Button(rootTestTaker, text="Finish Test", command=finish).grid(row=9, column=3)
        question()

    def vAssignments():
        print 'Assignments viewed'
    def cAssignments():
        print 'Assignments completed'    
    rootSim = Tkinter.Tk()
    rootSim.title("SIM - Student Information Manager")
    rootSim.minsize(400,400)
    Tkinter.Label(rootSim, text="Student Information Manager", font=("Arial", 30)).grid(row=0, column=0, columnspan=2)
    Tkinter.Label(rootSim, text=account['first'] + " " + account['last'], font=("Arial", 20)).grid(row=1, column=0, columnspan=2)
    grades = Tkinter.Button(rootSim, text="View \nGrades", command=viewGrades, width=15, height=5, bg="light gray", font=("Arial", 20)).grid(row=2, column=0)
    test = Tkinter.Button(rootSim, text="Take A \nTest", command=takeTest, width=15, height=5, bg="light gray", font=("Arial", 20)).grid(row=2, column=1)
    Tkinter.Label(rootSim).grid(row=3)
    viewAssignments = Tkinter.Button(rootSim, text="View \nAssignments", command=vAssignments, width=15, height=5, bg="light gray", font=("Arial", 20)).grid(row=4, column=0)
    createAssignments = Tkinter.Button(rootSim, text="Complete an \nAssignment", command=cAssignments, width=15, height=5, bg="light gray", font=("Arial", 20)).grid(row=4, column=1)
    Tkinter.Label(rootSim).grid(row=5)
    def restartFromSim():
        rootSim.destroy()
        init()
    back = Tkinter.Button(rootSim, text="Go Back", command=restartFromSim, width=32, height=2, bg="light gray", font=("Arial", 20)).grid(row=6, column=0, columnspan=2)

def teacher(account):
    #get list of all students
    students = []
    for user in users:
        if user['role'] == 'student':
            name = user['last'] + ", " + user['first']
            students.append(name)

    def viewGrades():
        rootGrades = Tkinter.Tk()
        rootGrades.title("SIM - Student Information Manager")
        rootGrades.minsize(400,400)
        Tkinter.Label(rootGrades, text="Student Information Manager", font=("Arial", 30)).grid(row=0, column=0, columnspan=3)
        Tkinter.Label(rootGrades, text=account['first'] + " " + account['last'], font=("Arial", 20)).grid(row=1, column=0, columnspan=3)
        def english():
            i = 0
            for user in users:
                if user['role'] == 'student':
                    Tkinter.Label(rootGrades, text=user['last'] + ", " + user['first'], font=("Arial", 15)).grid(row=i+6, column=0)  
                    Tkinter.Label(rootGrades, text=user['grades']['English'], font=("Arial", 15)).grid(row=i+6, column=2) 
                i += 1                   
                  
        def math():
            i = 0
            for user in users:
                if user['role'] == 'student':
                    Tkinter.Label(rootGrades, text=user['last'] + ", " + user['first'], font=("Arial", 15)).grid(row=i+6, column=0)  
                    Tkinter.Label(rootGrades, text=user['grades']['Math'], font=("Arial", 15)).grid(row=i+6, column=2)                    
                i += 1

        def socialStudies():
            i = 0
            for user in users:
                if user['role'] == 'student':
                    Tkinter.Label(rootGrades, text=user['last'] + ", " + user['first'], font=("Arial", 15)).grid(row=i+6, column=0)  
                    Tkinter.Label(rootGrades, text=user['grades']['Social Studies'], font=("Arial", 15)).grid(row=i+6, column=2)                    
                i += 1
                
        def science():
            i = 0
            for user in users:
                if user['role'] == 'student':
                    Tkinter.Label(rootGrades, text=user['last'] + ", " + user['first'], font=("Arial", 15)).grid(row=i+6, column=0)  
                    Tkinter.Label(rootGrades, text=user['grades']['Science'], font=("Arial", 15)).grid(row=i+6, column=2)                    
                i += 1  
        
        English = Tkinter.Button(rootGrades, text="English", command=english, width=20, height=2, bg="light gray", font=("Arial", 10)).grid(row=3, column=0)
        Math = Tkinter.Button(rootGrades, text="Math", command=math, width=20, height=2, bg="light gray", font=("Arial", 10)).grid(row=3, column=2)
        SocialStudies = Tkinter.Button(rootGrades, text="Social Studies", command=socialStudies, width=20, height=2, bg="light gray", font=("Arial", 10)).grid(row=4, column=0)
        Science = Tkinter.Button(rootGrades, text="Science", command=science, width=20, height=2, bg="light gray", font=("Arial", 10)).grid(row=4, column=2)

    def makeTest():
        def question():   
            rootTestMaker = Tkinter.Tk()
            rootTestMaker.title("SIM - Student Information Manager")
            rootTestMaker.minsize(400,400)
            Tkinter.Label(rootTestMaker, text="Student Information Manager", font=("Arial", 30)).grid(row=0, column=0, columnspan=4)
            Tkinter.Label(rootTestMaker, text=account['first'] + " " + account['last'], font=("Arial", 20)).grid(row=1, column=0, columnspan=4)

            Tkinter.Label(rootTestMaker, text="Question:").grid(row=3, column=0)
            q = Tkinter.Text(rootTestMaker, height=3)
            q.grid(row=3, column = 1, rowspan=2, columnspan=3)
            
            answer = IntVar(rootTestMaker)
            answer.set(0)

            Tkinter.Label(rootTestMaker, text="A.").grid(row=5, column=1)
            answer1 = Tkinter.Radiobutton(rootTestMaker, variable=answer, value=1)
            answer1.grid(row=5, column=2)
            option1 = Tkinter.Entry(rootTestMaker)
            option1.grid(row=5, column=3)
            
            Tkinter.Label(rootTestMaker, text="B.").grid(row=6, column=1)
            answer2 = Tkinter.Radiobutton(rootTestMaker, variable=answer, value=2)
            answer2.grid(row=6, column=2)
            option2 = Tkinter.Entry(rootTestMaker)
            option2.grid(row=6, column=3)
            
            Tkinter.Label(rootTestMaker, text="C.").grid(row=7, column=1)
            answer3 = Tkinter.Radiobutton(rootTestMaker, variable=answer, value=3)
            answer3.grid(row=7, column=2)
            option3 = Tkinter.Entry(rootTestMaker)
            option3.grid(row=7, column=3)
            
            Tkinter.Label(rootTestMaker, text="D.").grid(row=8, column=1)
            answer4 = Tkinter.Radiobutton(rootTestMaker, variable=answer, value=4)
            answer4.grid(row=8, column=2)
            option4 = Tkinter.Entry(rootTestMaker)
            option4.grid(row=8, column=3)
        
            def add():
                question = []
                question.append(option1.get())
                question.append(option2.get())
                question.append(option3.get())
                question.append(option4.get())
                question.append(answer.get())

                test.append(question)
            def new():
                rootTestMaker.destroy()
                question()
            def finish():
                rootTestMaker.destroy()
            Tkinter.Button(rootTestMaker, text="Save Question", command=add).grid(row=9, column=1)
            Tkinter.Button(rootTestMaker, text="New Question", command=new).grid(row=9, column=2)
            Tkinter.Button(rootTestMaker, text="Finish Test", command=finish).grid(row=9, column=3)
        question()

    def gradeAssignments():
        print 'Assignments graded'

    def createAssignments():
        print 'Assignments created' 
  
    def viewStudents():
        rootStudents = Tkinter.Tk()
        rootStudents.title("SIM - Student Information Manager")
        rootStudents.minsize(400,400)
        Tkinter.Label(rootStudents, text="Student Information Manager", font=("Arial", 30)).grid(row=0, column=0, columnspan=3)
        Tkinter.Label(rootStudents, text=account['first'] + " " + account['last'], font=("Arial", 20)).grid(row=1, column=0, columnspan=3)
        Tkinter.Label(rootStudents, text='Students:', font=("Arial", 15)).grid(row=2, column=1)
        for i in range(len(students)):
            Tkinter.Label(rootStudents, text=students[i], font=("Arial", 15)).grid(row=i+3, column=1)    

    def changeGrades():
        rootChange = Tkinter.Tk()
        rootChange.title("SIM - Student Information Manager")
        rootChange.minsize(400,400)
        Tkinter.Label(rootChange, text="Student Information Manager", font=("Arial", 30)).grid(row=0, column=0, columnspan=3)
        Tkinter.Label(rootChange, text=account['first'] + " " + account['last'], font=("Arial", 20)).grid(row=1, column=0, columnspan=3)
        def english():
            student = StringVar(rootChange)
            student.set(students[0])
           
            def changed(kid):
                Tkinter.Label(rootChange, text=kid, font=("Arial", 10)).grid(row=7, column=0)
                for i in range(len(students)):
                    if kid == students[i]:
                        x = -1
                        for j in users:
                            if j['role'] == 'student':
                                x += 1
                            if i == x:
                                STUDENT = j
                currentGrade = Tkinter.Label(rootChange, text=STUDENT['grades']['English'], font=("Arial", 10)).grid(row=7, column=1)
                futureGrade = Tkinter.Entry(rootChange)
                futureGrade.grid(row=7, column=2) ##dont actually remember what I was gonna do with this
                def go():
                    STUDENT['grades']['English'] = futureGrade.get()
                    changed(kid)
                submit = Tkinter.Button(rootChange, text='Submit Change', command=go).grid(row=8, column=1)
            option = OptionMenu(rootChange, student, *students, command=changed).grid(row=6, column=0)
            changed(student.get())


        def math():
            student = StringVar(rootChange)
            student.set(students[0])
           
            def changed(kid):
                Tkinter.Label(rootChange, text=kid, font=("Arial", 10)).grid(row=7, column=0)
                for i in range(len(students)):
                    if kid == students[i]:
                        x = -1
                        for j in users:
                            if j['role'] == 'student':
                                x += 1
                            if i == x:
                                STUDENT = j
                currentGrade = Tkinter.Label(rootChange, text=STUDENT['grades']['Math'], font=("Arial", 10)).grid(row=7, column=1)
                futureGrade = Tkinter.Entry(rootChange)
                futureGrade.grid(row=7, column=2) ##dont actually remember what I was gonna do with this
                def go():
                    STUDENT['grades']['Math'] = futureGrade.get()
                    changed(kid)
                submit = Tkinter.Button(rootChange, text='Submit Change', command=go).grid(row=8, column=1)
            option = OptionMenu(rootChange, student, *students, command=changed).grid(row=6, column=0)
            changed(student.get())

        def socialStudies():
            student = StringVar(rootChange)
            student.set(students[0])
           
            def changed(kid):
                Tkinter.Label(rootChange, text=kid, font=("Arial", 10)).grid(row=7, column=0)
                for i in range(len(students)):
                    if kid == students[i]:
                        x = -1
                        for j in users:
                            if j['role'] == 'student':
                                x += 1
                            if i == x:
                                STUDENT = j
                currentGrade = Tkinter.Label(rootChange, text=STUDENT['grades']['Social Studies'], font=("Arial", 10)).grid(row=7, column=1)
                futureGrade = Tkinter.Entry(rootChange)
                futureGrade.grid(row=7, column=2) ##dont actually remember what I was gonna do with this
                def go():
                    STUDENT['grades']['Social Studies'] = futureGrade.get()
                    changed(kid)
                submit = Tkinter.Button(rootChange, text='Submit Change', command=go).grid(row=8, column=1)
            option = OptionMenu(rootChange, student, *students, command=changed).grid(row=6, column=0)
            changed(student.get())
                
        def science():
            student = StringVar(rootChange)
            student.set(students[0])
           
            def changed(kid):
                Tkinter.Label(rootChange, text=kid, font=("Arial", 10)).grid(row=7, column=0)
                for i in range(len(students)):
                    if kid == students[i]:
                        x = -1
                        for j in users:
                            if j['role'] == 'student':
                                x += 1
                            if i == x:
                                STUDENT = j
                currentGrade = Tkinter.Label(rootChange, text=STUDENT['grades']['Science'], font=("Arial", 10)).grid(row=7, column=1)
                futureGrade = Tkinter.Entry(rootChange)
                futureGrade.grid(row=7, column=2) ##dont actually remember what I was gonna do with this
                def go():
                    STUDENT['grades']['Science'] = futureGrade.get()
                    changed(kid)
                submit = Tkinter.Button(rootChange, text='Submit Change', command=go).grid(row=8, column=1)
            option = OptionMenu(rootChange, student, *students, command=changed).grid(row=6, column=0)
            changed(student.get()) 
        
        English = Tkinter.Button(rootChange, text="English", command=english, width=20, height=2, bg="light gray", font=("Arial", 10)).grid(row=3, column=0)
        Math = Tkinter.Button(rootChange, text="Math", command=math, width=20, height=2, bg="light gray", font=("Arial", 10)).grid(row=3, column=2)
        SocialStudies = Tkinter.Button(rootChange, text="Social Studies", command=socialStudies, width=20, height=2, bg="light gray", font=("Arial", 10)).grid(row=4, column=0)
        Science = Tkinter.Button(rootChange, text="Science", command=science, width=20, height=2, bg="light gray", font=("Arial", 10)).grid(row=4, column=2)

    rootSim = Tkinter.Tk()
    rootSim.title("SIM - Student Information Manager")
    rootSim.minsize(400,400)
    Tkinter.Label(rootSim, text="Student Information Manager", font=("Arial", 30)).grid(row=0, column=0, columnspan=3)
    Tkinter.Label(rootSim, text=account['first'] + " " + account['last'], font=("Arial", 20)).grid(row=1, column=0, columnspan=3)
    vgrades = Tkinter.Button(rootSim, text="View \nGrades", command=viewGrades, width=15, height=5, bg="light gray", font=("Arial", 20)).grid(row=2, column=0)
    cgrades = Tkinter.Button(rootSim, text="Change \nGrades", command=changeGrades, width=15, height=5, bg="light gray", font=("Arial", 20)).grid(row=2, column=1)
    makeTest = Tkinter.Button(rootSim, text="Make A \nTest", command=makeTest, width=15, height=5, bg="light gray", font=("Arial", 20)).grid(row=2, column=2)
    Tkinter.Label(rootSim).grid(row=3)
    gradeAssignments = Tkinter.Button(rootSim, text="Grade \nAssignments", command=gradeAssignments, width=15, height=5, bg="light gray", font=("Arial", 20)).grid(row=4, column=0)
    createAssignments = Tkinter.Button(rootSim, text="Create an \nAssignment", command=createAssignments, width=15, height=5, bg="light gray", font=("Arial", 20)).grid(row=4, column=1)
    vstudents = Tkinter.Button(rootSim, text="View \nStudents", command=viewStudents, width=15, height=5, bg="light gray", font=("Arial", 20)).grid(row=4, column=2)
    Tkinter.Label(rootSim).grid(row=5)
    def restartFromSim():
        rootSim.destroy()
        init()
    back = Tkinter.Button(rootSim, text="Go Back", command=restartFromSim, width=48, height=2, bg="light gray", font=("Arial", 20)).grid(row=6, column=0, columnspan=3)



user = {'username': '1',
                'password': '2',
                'first': '3',
                'last': '4',
                'role': 'student',
                'code': [6],
                'grades': { 'English': 10,
                            'Math': 10,
                            'Social Studies': 10,
                            'Science': 10 } }
users.append(user)

user = {'username': '2',
                'password': '3',
                'first': '4',
                'last': '5',
                'role': 'student',
                'code': [7],
                'grades': { 'English': 20,
                            'Math': 20,
                            'Social Studies': 20,
                            'Science': 20 } }
users.append(user)


###############################
#MUST BE THE LAST LINE OF CODE#
############################### 
def start():
    init()
