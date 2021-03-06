# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Dustin Holland,05/12/2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
objFile = open('ToDoList.txt', 'a')
dicRow = {'Task': 'Homework', 'Priority': 'High'}
objFile.write(dicRow['Task'] + ',' + dicRow['Priority'] + '\n')
lstTable = [dicRow]
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print('You have selected option', strChoice)  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here #code added
        print('Here is what is currently stored')
        for i in lstTable:
            print(i)
        continue
    # Step 4 - Add a new item the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here

        # Must gather user input.
        NewTask = input('Please enter your Task')
        NewPriority = input('Please enter your priority (Low, Med, High)')
        dicRow = {'Task': NewTask, 'Priority': NewPriority.strip()}
        lstTable.append(dicRow)

        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        lstTable.remove(lstTable[1])
        print('You have successfully removed your last added item')

        continue


    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
            # TODO: Add Code
        objFile=open('ToDoList.txt', 'a')
        objFile.write(dicRow['Task'] + ',' + dicRow['Priority'] + '\n')
        objFile.close()
        print('You have successfully saved your file!')
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print('You are now exiting the program')
        break  # and Exit the program
