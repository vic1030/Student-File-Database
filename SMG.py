
class StudentManagerController:
    """
    StudentManagerController: Manages student records and operations.
    Methods:
           __init__: Initialize the student manager.
        add_student: Add a new student to the manager.
        generate_id: Generate a unique student ID.
        remove_student: Remove a student based on ID.
        update_student: Update student information.
        order_by_score: Sort students by score in descending order.
        student_average_score: Calculate the average score of all students.
    
    """

    __init_id = 100  # Initialize the student manager.

    def __init__(self):
        self.stu_list = []

    def stu_list(self):
        """
        student_list
        return: The list stored student list
        """
        return self.stu_list

    def add_student(self, stu_info):
        """
        add one new student
        param stu_info: student information without list
        """
        stu_info.id = self.generate_id()

        self.stu_list.append(stu_info)

    def generate_id(self):
        """
        Generate a unique student ID.
        """
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self, id):
        """
        remove student base on id
        param id: student id
        return:
        """
        for i in self.stu_list:
            if i.id == id:
                self.stu_list.remove(i)
                return True  # remove successed
        return False  # failed to remove

    def update_student(self, stu_info):
        """
        update other information base on stu_info.id
        param stu_info: student
        return: wether update successed
        """
        for i in self.stu_list:
            if i.id == stu_info.id:
                i.name = stu_info.name
                i.age = stu_info.age
                i.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        """
        Descending self.__stu_list based on score
        """
        for r in range(len(self.stu_list) - 1):
            for c in range(r + 1, len(self.stu_list)):
                if self.stu_list[r].score < self.stu_list[c].score:
                    self.stu_list[r], self.stu_list[c] = self.stu_list[c], self.stu_list[r]

    def student_average_score(self):
        total_score = sum(student.score for student in self.stu_list)
        num_students = len(self.stu_list)
        if num_students > 0:
            return total_score / num_students
        else:
            return 0

        
class StudentModel:
    """

    StudentModel: Represents a student's data structure.
        Methods:
            __init__: Initialize a student instance.

    """

    def __init__(self, name="", age=0, score=0, id=0):
        """
        create student
        param name: (str)
        param age: (int)
        param score: (float)
        param id:(student id to identify indiviual information)
        """
        self.name = name
        self.age = age
        self.score = score
        self.id = id