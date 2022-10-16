"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""


class Student:

    def __init__(self, name, age, id, stream, university):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()
        self.stream = stream
        self.university = university

    def add_subject(self, subject, grade):
        self.subjects[subject] = grade
        return self.subjects

    def remove_subject(self, subject):
        self.subjects.pop(subject)
        return self.subjects

    def show_all_subjects(self):
        for subject in self.subjects:
            print(subject)

    def overall_mark(self):
        sum_of_grades = sum(self.subjects[subject] for subject in self.subjects)
        avg_grade = round(sum_of_grades / len(self.subjects), 2)
        return avg_grade




# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

class CFGStudent(Student):

    def __init__(self, name, age, id):
        super().__init__(name=name, age=age, id=id, stream='software', university="CFG")



first_student = CFGStudent(name='Sarah', age=20, id='1234')

#Add subject
first_student.add_subject('Python foundation', 60)
first_student.add_subject('Theory foundation', 75)
first_student.add_subject('Algorithms', 84)
first_student.add_subject('Databases', 65)
first_student.show_all_subjects()

#Remove subject
first_student.remove_subject('Python foundation')
first_student.show_all_subjects()

#Overall mark
print(first_student.overall_mark())








