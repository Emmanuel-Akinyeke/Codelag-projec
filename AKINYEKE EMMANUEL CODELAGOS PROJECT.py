#-*-coding:utf8;-*-
#qpy:3
#qpy:console
################   AUTHOR: Akinyeke Emmanuel #################
################# CREDITS: Tutorials point #### w3schools, #### ipython #### python docs #####
################ CREATED:  11/09/2018 ####################
############### ATTENDANCE REGISTER   ############# ###
############# PROGRAM VERSION:   0.9 #####################
############ Welcome The world of programming where ideas can be coded ###
import time
import sys

#file_attendance = open('Attendance Log.txt', 'w')
#defines the menu system of the attendance
#Defines the main menu items for the program 
def menu_items():
    print('1.  Register a student') 
    print('2.  Remove a student') 
    print('3.  Search for a student') 
    print('4.  print registered student list') 
    print('5.  Mark Attendance')
    print('6.  Get a student attendance Log') 
    print('7.  Print all Attendance log')
    print('8.  Quit')
    
def reg_student():
    global reg_students
    global attendance_log
    print('Welcome to the CODE LAGOS attendace Registration page\nTyping (back) takes you to the main menu') 
    decision = True      #initilize the while statement to run at all times
    reg_students = {}
    attendance_log = {} 
    while decision == True:
        stud_name = input('STUDENT NAME:  ')
        time.sleep(1)
        stud_phone = input('STUDENT PHONE NUMBER:  ')
        time.sleep(1)
        stud_sex = input('SEX (Male or Female):  ')
        others = [stud_phone, stud_sex]
        reg_students[stud_name] = others   #makes the student name the key and others as the value for the dictionary 
        attendance_log[stud_name] = ' '  #register the user name on the attendance list
        user_decision = input('Add another student? (y/n)\nTyping (n) takes you to main main menu:   ') 
        if user_decision.lower() == 'n':
            decision = False
        else:
            decision = True
                
def remove_student():
    time.sleep(1) 
    global reg_students, attendance_log    #declaring reg_students and attendance_log as a variable
    remove =  True      ##initilize the while statement for execution 
    while remove:
        del_name = input('Enter the student name to Remove: \nType (exit) for Main menu \n ')
        if del_name  in reg_students:
            del reg_students[del_name]     #delete the name inserted by the user on the registration list
            del attendance_log[del_name]     #delete the name inserted by the user on the attendance list
            print(del_name, 'Removed')
            continue
        if del_name.lower() == 'exit':
               remove = False
        else:
            print('The student name was not found')
def search_student():
    time.sleep(1) 
    global reg_students, attendance_log
    search_name = input('Enter the name of the student:  ')
    if search_name in reg_students:
        print(search_name)
        print(reg_students[search_name])   #print the name inserted if it is found
    else:
        print(search_name, 'was not found')
        
def get_regstudents():
    time.sleep(1) 
    global reg_students, attendance_log
    for s, t in sorted(enumerate(reg_students.items())): #it sorts and itemize all the keys and values found
        print(s, t)
        decision = input('Type (back) for main menu\n') 

def mark_attendance():
    time.sleep(2) 
    global reg_students, attendance_log
    log = True 
    while log:
        print('Type (exit) to quit the logger') 
        print('Entering your name simply mark you present on the attendance list\n') 
        log_check = input()
        if log_check in attendance_log:       #test for membership 
            time_log = time.asctime(time.localtime())    ##assign the formatted asctime to the variable 
            time_fun = str(time_log)          #converts the time into a printable str.
            attendance_log[log_check] = time_fun  #it add the time to the attendance log 
            print(time_fun, 'recorded for', log_check)   #Tels the user what happened
        elif log_check.lower() == 'exit':
            log = False
        else:
            print(log_check, 'not found please register the name: ') 
def get_studentlog():
    time.sleep(1) 
    global reg_students, attendance_log
    while True:
        student_name = input('Enter the student name:  ')
        if student_name in attendance_log:
            print(attendance_log[student_name])
            decision = input('Enter for main menu:\n') 
            break
        else:
            print(student_name, 'was not found')
            
def studentlogs():
    time.sleep(1) 
    global reg_students, attendance_log
    print(attendance_log)
    decision = input('\n Type (back) for main menu:\n')
    
def savedata():
    global reg_students, attendance_log
    file_attendance = open('Attendance Log.txt', 'w') 
    file_attendance.write(reg_students)
    file_attendance.close()
    

def exit():
    print('Thank you for using this program')
    sys.exit()        #exit the program

#function as main  
def main():
    print('WELCOME TO CODE LAGOS ATTENDANCE PROGRAM') 
    time.sleep(2)
    choice = 0            #initilize the menu executor
    reg_students = {}     #create an empty list for Registered users
    attendance_log = {}    #create an empty list for attendance
    
    while choice !=9:
        menu_items() 
        time.sleep(2)         #delays the program for Few seconds
        choice = int(input()) #ask for user choice of item
        if choice == 1:  
            reg_student()
        if choice == 2:
            remove_student() 
        if choice == 3:
            search_student()
        if choice == 4:
            get_regstudents()
        if choice == 5:
            mark_attendance()
        if choice == 6:
            get_studentlog()
        if choice == 7:
            studentlogs()
        if choice == 8:
        #   savedata()     #Needs reviewing
            exit() 


main()           
 






'''
NOTE: 

This scripts can be improved for efficiency and more features can be included

Suggestions: 
(1) A database system can be implemented
(2) Student details can be automated on on excel document
(3) A GUI can be implemented
(4) The Student could use a code to mark the attendance
 upgrade is limitless. 
'''