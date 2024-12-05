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
        
class Mentor:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Lector(Mentor):
    def __init__(self):
        pass
    
class Reviewer(Mentor):
    def __init__(self):
        pass    
    
        
lector = Lector('Vitya', 'Barashkin')
print(lector.__dict__)



