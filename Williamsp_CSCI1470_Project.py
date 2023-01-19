import datetime
import time
from operator import index



#this puts a tiltle
def display_title():
    title = "** Clock-in System **"
    print("*" * len(title))
    print("*" * len(title))
    print(title)
    print("*" * len(title))
    print("*" * len(title))

#this makes 80 --- dashes
def display_separator():
    print("-" * 80)
    
def Add():
    Time_emp = input("Enter 'IN' For Clockin or Enter 'Out' for Clockout: ")
    display_separator()
    Time = Time_emp.upper()
    if Time == "OUT":
        Clock_out()
    elif Time == "IN":

        #Open the Timecard.txt file in append mode
        TimeCard_file = open('TimeCard.txt', 'a')
        # Add clock in time with current time.
        #input employees' name
        EmpName = input('Enter Your Name:')
        #this upper case employees' names
        Emp_Name = EmpName.upper()
        now = datetime.datetime.now()
        #the date looks like 0000-00-00
        Current = now.strftime("%Y-%m-%d")
        #the time looks like 00:00AM\PM
        Clock_in = now.strftime("%I:%M%p")

        #Append data to the file
        TimeCard_file.write(Emp_Name + " ")
        TimeCard_file.write(Current + " ")
        TimeCard_file.write(Clock_in)
        print("Your Current Date is:",Current)
        print("Your Clock in Time is :", Clock_in)
        TimeCard_file.write('\n')

        #Close the file
        TimeCard_file.close()

    #check if user want to conutine or quit program
    #Q is for quit
    #M is for main menu
    func = input("Enter Q to quit or Press M for main menu:")
    if func == "Q" or func =="q":
        quit()
    elif func == "M" or func =="m":
        return main()
    else:
        print("Incorrect input, Please Try Again \n")

#First Ask for employee name so can add clock out time for same person.
def Clock_out():
        found = False
        val = 'x'
        #input the employees' name you want to search for
        employee_name = input("Please Enter Your Name:")
        #uppercase
        employee = employee_name.upper()
        #open the time card file and search name
        TimeCard_file = open("TimeCard.txt", 'r')
        TimeCard = TimeCard_file.readline()

        #read the file if you have entered any name
        while TimeCard != '':
            found = TimeCard.startswith(employee)
            if found:
                val = TimeCard
            TimeCard = TimeCard_file.readline()
        TimeCard_file.close()


        if val != '':
                now = datetime.datetime.now()
               #current date
                Current  = now.strftime("%Y-%m-%d")
                #time right now
                Clock_out = now.strftime("%I:%M%p")
                search = val
                print(search.rstrip('\n') + ' ' + Clock_out)
                print("You are Clocked out successfully")
                display_separator()
              

     
           

#This function will display all working time for all employee
def TimeReport():
        #open time card
        TimeCard_file = open('TimeCard.txt','r')
        TimeCard = TimeCard_file.readline()
        #read the rest of the file
        while TimeCard != '':
            #Display all of the employee's data
            print('Employee Hours:', TimeCard)

            TimeCard = TimeCard_file.readline()
            
        #close the file
        TimeCard_file.close()

        #Added function to make decision if want to work or exit
        func = input("Enter Q to quit or Press M for main menu:")
        if func == "Q" or func =="q":
                quit()
        elif func == "M" or func =="m":
                return main()
        else:
                print("Incorrect input, Please Try Again \n")

def Edit():
        found =  False

        #input the name you want to search
        EmpName = input("Please Enter Employee Name:")
        employee = EmpName.upper()

        #open the time card file and search name
        TimeCard_file = open('TimeCard.txt','r')
        TimeCard = TimeCard_file.readline()


        #read the file if you have entered any name
        while TimeCard != '':
                found = TimeCard.startswith(employee)
                if found:
                        print(TimeCard)

                TimeCard = TimeCard_file.readline()
        
        TimeCard_file.close()
        Date = input("Enter the Date you want to edit:")
        search = (employee + " " + Date)

        #Open the file
        fn = "TimeCard.txt"
        f = open(fn)
        output = []
        #for loop i you find search record
        for line in f:
                if not line.startswith(search):
                    output.append(line)
        f.close()
        f = open(fn, 'w')
        f.writelines(output)
        f.close()

        #open the TimeCard.txt file in append mode
        TimeCard_file = open('TimeCard.txt', 'a')
        
        print("enter Clock in and Clock out for",employee)
        display_separator()
        Clock_in = input("Enter Clock In time:")
        Clock_out = input("Enter Clock Out time:")

        TimeCard_file.write(employee + " ")
        TimeCard_file.write(Date + " ")
        TimeCard_file.write(str(Clock_in) + " ")
        TimeCard_file.write(str(Clock_out) + " ")
        TimeCard_file.write('\n')

        #Close the file
        TimeCard_file.close()
    

        #check if user want to conutine or quit program
        #Q is for quit
        #M is for main menu
        func = input("Enter Q to quit or Press M for main menu:")
        if func == "Q" or func =="q":
                quit()
        elif func == "M" or func =="m":
                return main()
        else:
                print("Incorrect input, Please Try Again \n")





#Add date in time Card
def main():
    display_title()
    display_separator()
    #Select the option what you like to do in you time card
    print("What would you like to do in clock-in System?")
    print("A = Add :: E = Edit :: R = Report :: Q = Quit")
    func = input("Please select a function from the list above:")
    display_separator()

    #Use while loop
    #menu options
    while func == '' or func != 'A'  or func != 'a' or func != 'E' or func != 'e' or func != 'R' or func != 'r':
        if func == 'A' or func == 'a':
                Add()
       
        elif func == 'E' or func == 'e':
            print('Are you Manager?:')
            Mrg_emp = input("Y=Yes, Anything Else = No:")
            Mgr= Mrg_emp.upper()
            if (Mgr == 'YES' or Mgr == 'Y'):
                Edit()
            else:
                    print('\n')
                    main()
        elif func == 'R' or func == 'r':
            print('Are you Manager?:')
            Mrg_emp = input("Y=Yes, Anything Else = No:")
            Mgr= Mrg_emp.upper()
            if (Mgr == 'YES' or Mgr == 'Y'):
                TimeReport()
            else:
                    print('\n')
                    main()
        elif func == "Q" or func == "q":
                quit()
        #if you press any random key it will bring you here
        else:
            print("Incorrect input please try again \n")
            func = input("enter A for Add, E for Edit, R for Report:")

main()
