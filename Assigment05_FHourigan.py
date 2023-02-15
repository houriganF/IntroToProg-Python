# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# FHourigan,02/13/2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    objFile = open("ToDoList.txt", "r")  # Read Data from File if it exists
    for row in objFile:
        lstRow = row.split(",")
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}  #Create a dictionary {key:value}
        lstTable.append(dicRow)
        print(dicRow)
        print(dicRow["Task"] + "," + dicRow["Priority"])
    objFile.close()
except:
    print("""File Not Found, Create a file file 
    called ToDoList.txt first.""")


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
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        if len(lstTable) == 0:
            print(" ---- No Data in File ---- ")
        else:
            for dicRow in lstTable:
                print(dicRow["Task"] + "," + dicRow["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        dicRow = {"Task": input(" Please Enter a Task: "), "Priority": input(" Please Enter the Priority: ")}
        lstTable.append(dicRow)
        print(" Your data was added to ToDoList.txt, select choice 1 to see the current data in the file...")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strData = (input("Row of Task and corresponding Priority to remove: "))
        for row in lstTable:
            if dicRow["Task"].lower() == strData.lower():
                lstTable.remove(dicRow)
                print(" -- Row Removed -- ")
            else:
                print(" Row Not Found ")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + ',' + dicRow["Priority"] + '\n')
        objFile.close()
        print("-- Data Recorded to Text File -- \n")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print(" -- Good Bye -- ")  # Exit the program
        break  # and Exit the program