class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age 
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self,student):
        if self.max_students > len(self.students):
            self.students.append(student)
            print('Student Added Successfully',self.students)
            return True
        raise Exception('Maximun number of students reached.')
        
    
    def get_average_student(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value/len(self.students)


s1 = Student('Tim',19,95)
s2 = Student('Bill',19,70)
s3 = Student('Jessica',19,84)  

course = Course('English',2)

course.add_student(s1)
course.add_student(s2)


