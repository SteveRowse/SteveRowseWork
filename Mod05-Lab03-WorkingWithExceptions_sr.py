# ------------------------------------------------------------------------------------------ #
# Title: lab 03 Working With Exceptions
# Desc: Shows how work with Exceptions
# Change Log: (Who, When, What)
#   <Steve ROwse>,<20/23/2026>,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data
import json
FILE_NAME: str = 'MyLabData.json'
RED = '\033[31m'
RESET = '\033[0m' # Resets the color to default

# Define the program's data
MENU: str = '''
---- Student GPAs ------------------------------
  Select from the following menu:  
    1. Show current student data. 
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
-------------------------------------------------- 
'''



student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
student_gpa: float = 0.0  # Holds the GPA of a student entered by the user.
message: str = ''  # Holds a custom message string
menu_choice: str = ''   # Hold the choice made by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Not using type hint helps PyCharm, so we won't use it going forward


# When the program starts, read the file data into a list of dictionary rows (table)
# Extract the data from the file
    # Transform the data from the file
    # Load it into the collection collection is "students"

FILE_NAME: str = '_MyLabData.json'

try:

    file = open(FILE_NAME, "r")
    students = json.load(file)

except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file is not None and file.closed == False:
        file.close()


file = open(FILE_NAME, "w")
json.dump(students, file)
file.close()

''' 
for row in file.readlines(): #creates a veriable "row"
    # Transform the data from the file
    student_data = row.split(',')   #creates a variable "student_data" which is taking the previous variable "row" and
                                    #spliting it into indicies seperated by commas. So "FirstName" "lastName" and "GPA"
                                    #variable is the result of splitting the data
    student_data = {"FirstName": student_data[0],"LastName": student_data[1],"GPA": float(student_data[2].strip())}
    # add (append) it into our collection (list of lists)
    students.append(student_data)
file.close()
'''

print(students) #check point


    # Repeat the follow tasks
    # display the table's current data
while True:
    print(MENU)
    menu_choice: str = input('enter you menu choice: ')

    if menu_choice == "1":
    # Process the data to create and display a custom message
        for student in students:
            if student["GPA"] >= 4.0: #if there is an instance of a number > then 4 then print -
                                        #THEN print the data from the indexed strings
                message = " {} {} earned an A with a {:.2f} GPA"
            elif student["GPA"] >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif student["GPA"] >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif student["GPA"] >= 1.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA was not a passing grade"

            print(message.format(student["FirstName"], student["LastName"], student["GPA"]))
        print("-"*50)
        continue

    elif menu_choice == "2":
        try:
            # Input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError(RED + "The first name should not contain numbers." + RESET)


            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            try:  # using a nested try block to capture when an input cannot be changed to a float
                student_gpa = float(input("What is the student's GPA? "))
            except ValueError:
                raise ValueError("GPA must be a numeric value.")

            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "GPA": float(student_gpa)}
            students.append(student_data)
        except ValueError as e:
            print(e)  # Prints the custom message
            print(RED + "-- Technical Error Message -- " + RESET)
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')


        continue
    elif menu_choice == "3":
        '''
        #  Save the data to the file
        file = open(FILE_NAME, "w")
        for student in students:
            file.write(f'{student["FirstName"]},{student["LastName"]},{student["GPA"]}\n')
        file.close()
        print("Data Saved!")
        '''
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
        except TypeError as e:
            RED
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file is not None and file.closed == False:
                RESET
                file.close()

        print(students)  # check point
        continue

    elif menu_choice == "4":
        print("Goodbye!")
        break
# Add data to the table
    # Save the data to the file
    # Exit the program



