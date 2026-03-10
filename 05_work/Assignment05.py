# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Steve Rwose>,<02/25/2025>, <Asignment start>
# ------------------------------------------------------------------------------------------ #

# TODO: Import the json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 

'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
RED = '\033[31m'                # sets color to red
RESET = '\033[0m'               # Resets the color to default

# When the program starts, read the .json
import json
import sys                      # needed for color change

# Define the Data Variables
student_first_name: str = ''    # Holds the first name of a student entered by the user.
student_last_name: str = ''     # Holds the last name of a student entered by the user.
course_name: str = ''           # Holds the name of a course entered by the user.
file = None                     # Holds a reference to an opened file.
menu_choice: str                # Hold the choice made by the user.
student_data: dict = {}         # Hold the dictionary
students: list = []             # Hold the list



# Extract the data from the file with error handling
try:
    file = open(FILE_NAME, "r")     # opens the .json file
    students = json.load(file)      # set the imported data to a variable "students"
except FileNotFoundError as e:      # creates an error if there is not .json file
    print("Text file must exist before running this script!\n")
    print(RED +"-- Technical Error Message -- " + RESET)
    print(e, e.__doc__, type(e), sep='\n')
    print("program ended")          # since there is no file end program
    sys.exit(1)
except Exception as e:
    print("There was a non-specific error!\n")
    print(RED +"-- Technical Error Message -- "+ RESET)
    print(e, e.__doc__, type(e), sep='\n')

finally: # Check if a file object exists and is still open
    if file is not None and file.closed == False:
        file.close()


# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do? ")

# Input user data
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():    # error if user enters a number
                raise ValueError(RED + "The first name should not contain numbers." + RESET)
            student_last_name = input("Enter the student's last name: ")
            if not student_first_name.isalpha():    # error if user enters a number
                raise ValueError(RED + "The first name should not contain numbers." + RESET)
            course_name = input("Please enter the name of the course: ")

            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            if not student_first_name.isalpha():     # error if user enters a number
                raise ValueError(RED + "The first name should not contain numbers." + RESET)
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print(RED + "-- Technical Error Message -- " + RESET)
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print(RED + "-- Technical Error Message -- " + RESET)
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        for each_row in students:
            #print(each_row)
            print(each_row["FirstName"], each_row["LastName"], "is registered for", each_row["CourseName"])
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            print("----Data Saved----")
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file is not None and file.closed == False:
                file.close()
        continue # Stop the loop


    elif menu_choice == "4":
        break  # out of the loop
    else:
        print(RED + "Please only choose option 1, 2, 3, or 4"+ RESET)

print("Program Ended")
