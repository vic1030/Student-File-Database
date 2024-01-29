"""
Student File Database

This program implements a student information management system using Python. 
It allows users to interactively perform operations related to student records, 
including adding, displaying, modifying,and deleting student information. 
The student data is stored in a JSON file named 'StudentInfo.txt'.

The program is organized using a class-based architecture, 
comprising several classes that work together to manage student information effectively. 
It includes features such as input validation, file I/O, and error handling to enhance usability and reliability.

Dependencies:

SMG module: Contains the 'StudentManagerController' class responsible for managing student records.
StudentModel class: Represents the structure of a student's data.

Usage:
    Run this script to start the Student File Database program. 
    Follow the on-screen menu prompts to perform various operations on student records.

"""
from SMG import *
import os
import json
import re
Space = '\t\t'

class StudentManagerView:
    """ 
    StudentManagerView: Handles user interaction and menu display.
        
    Methods:
           display_menu: Display the main menu options.
            main: Main loop to manage user interactions and options.
            input_number: Safely input and validate numeric values.
            validate_name: Validate student name using a regular expression.
            input_student: Gather user input for adding a new student.
            output_students: Save student data to the 'StudentInfo.txt' file.
            load_file: Load student data from the 'StudentInfo.txt' file.
            delete_student: Prompt user for student ID and delete the student if found.
            modify_student: Allow user to modify student details.
            output_student_by_score: Display student records in descending order of scores 
                                     and calculate average score.
    
    """

    def __init__(self):
        self.manager = StudentManagerController()

    def display_menu(self):

        print(Space + '-' * 115)
        print(Space + '-\t\t\t\t\t\t- Student File Database -\t\t\t\t\t-')
        print(Space + '-' * 115)
        print(Space + '-\t\t1.Adding Student Information\t\t\t\t2.Display Student Information\t\t-')
        print(Space + '-' * 115)
        print(Space + '-\t\t3.Delete Student Information\t\t\t\t4.Query and Modify Student Information\t-')
        print(Space + '-' * 115)
        print(Space + '-\t\t5.Students Grade(Descending Order)+ Average\t\t6.Exit the Systerm\t\t\t-')
        print(Space + '-' * 115)


    def main(self):
        """
        Main loop to manage user interactions and options.
        """
    
        while True:
            self.display_menu()
            option = input("Please enter the corresponding number for your choice: ")
            if option == "1":
                self.input_student()
            elif option == "2":
                self.output_students(self.manager.stu_list)
            elif option == "3":
                self.delete_student()
            elif option == "4":
                self.modify_student()
            elif option == "5":
                self.output_student_by_score()
            elif option == "6":
                print('Exiting the systerm...')
                break
            else:
                print('\n' + Space + 'INVALID ANSWER, PLEASE ENTER AGAIN.')


    def input_number(self,message):
        """
        Safely input and validate numeric values.
        """
        while True:
            try:
                number = int(input(message))
                return number
            except:
                print("INVALID INPUT!")

    def validate_name(self, name):
        """
        Validate student name using a regular expression.
        """
        pattern = r'^[A-Za-z\s]+$'  # Only alphabetic characters and spaces
        return re.match(pattern, name) is not None

    
    def input_student(self):
        """
        Gather user input for adding a new student.
        """
        name = input("Please Enter the Student Name: ")
        while not self.validate_name(name):
            print("Invalid name format. Please enter a valid student name.")
            name = input("Please Enter the Student Name: ")
        age = self.input_number("Please Enter the Age: ")
        score = self.input_number("Please Enter the Final Grade: ")
        student = StudentModel(name, age, score)
        self.manager.add_student(student)

    def output_students(self, list_output):
        """
        Save student data to the 'StudentInfo.txt' file(dic).
        """
        student_data = []

        for i in list_output:
            student_data.append(
                {'Student-ID': i.id, 'Student-Name': i.name, 'Student-Age': i.age, 'Student-Score': i.score}
                )

        with open('StudentInfo.txt', 'w', encoding='utf-8') as f:
            json.dump(student_data, f, indent=4)

        print('\n' + 'Student information successfully added and saved!')

    def load_file(self):
        """
        Load student data from the 'StudentInfo.txt' file.
        """
        if os.path.exists('StudentInfo.txt'):
            with open('StudentInfo.txt', 'r', encoding='utf-8') as f:
                student_data = json.load(f)
                for data in student_data:
                    student = StudentModel(data['name'], data['age'], data['score'])
                    self.manager.add_student(student)
    
    def delete_student(self):
        """
        Prompt user for student ID and delete the student if found.
        """
        id = self.input_number("Please Enter the Student ID: ")

        if self.manager.remove_student(id):
            print(" Successfully Deleted ")
        else:
            print(" Failed to Delete ")

    def modify_student(self):
        """
        Allow user to modify student details.
        """
        student = StudentModel()
        student.id = self.input_number("Please Enter the Student's ID You Want to Change: ")
        student.name = input("Please Enter the Revised Name: ")
        student.age = self.input_number("Please Enter the Revised Age:: ")
        student.score = self.input_number("Please Enter the Revised Score: ")

        if self.manager.update_student(student):
            print("Successful Modification")
        else:
            print("Failed to Modify")

    def output_student_by_score(self):
        """
        Display student records in descending order of scores and calculate average score.
        """
        self.manager.student_average_score()
        average_score = self.manager.student_average_score()
        print(f'Average score of all students: {average_score}')
        self.manager.order_by_score()
        self.output_students(self.manager.stu_list)



if __name__ =="__main__":
    try:
        view = StudentManagerView()
        view.main()
        
    except:
        print("System Error Occurred")