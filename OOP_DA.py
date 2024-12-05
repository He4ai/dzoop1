class Student:
    def __init__(self, name, last_name, gender):
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def add_finished_courses(self, course):
        self.finished_courses.append(course)
        if course in self.courses_in_progress:
            self.courses_in_progress.remove(course)
            
    def rate_lector(self, lector, course, grade: int):
        if isinstance(lector, Lector) and (course in self.finished_courses or course in self.courses_in_progress) and course in lector.courses_attached and grade >=1 and grade <= 10:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка!'
        
class Mentor:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.courses_attached = []
        
class Lector(Mentor):

    def __init__(self, name, last_name):
        super().__init__(name, last_name)
        self.grades = {}
    
class Reviewer(Mentor):
    def __init__(self):
        pass  
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    

##dlya proverki moego koda
"""
lector = Lector('Vitya', 'Barashkin')
lector.courses_attached.append('Python')
print(lector.grades)
student = Student('Masha', 'Class', 'Ne masha...')
student.courses_in_progress.append('Python')
student.courses_in_progress.append('Pyn')
student.rate_lector(lector, 'Python', 10)
student.rate_lector(lector, 'Python', 10)
student.rate_lector(lector, 'Python', 10)
print(lector.grades)

"""

