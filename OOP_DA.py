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
            
    def average_rate(self):
        if len(self.grades.values()) != 0:
            return round(sum(map(sum, self.grades.values())) / sum(map(len, self.grades.values())), 1)
        else:
            return 0
            
    def rate_lector(self, lector, course, grade: int):
        if isinstance(lector, Lector) and (course in self.finished_courses or course in self.courses_in_progress) and course in lector.courses_attached and grade >=1 and grade <= 10:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка!'
            

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.last_name} \nСредняя оценка за курс: {self.average_rate()} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курс: {self.finished_courses}'
        
class Mentor:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.courses_attached = []
        
class Lector(Mentor):
    def __init__(self, name, last_name):
        super().__init__(name, last_name)
        self.grades = {}
        
    def average_rate(self):
        if len(self.grades.values()) != 0:
            return round(sum(map(sum, self.grades.values())) / sum(map(len, self.grades.values())), 1)
        else:
            return 0
                
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.last_name} \nСредняя оценка за лекцию: {self.average_rate()}'
 
    def __lt__(self, other):
        if not isinstance(other, Lector):
            print('Сравнение некорректно!')
        else:
            return self.average_rate() < other.average_rate()
        
    def __eq__(self, other):
        if not isinstance(other, Lector):
            print('Сравнение некорректно!')
        else:
            return self.average_rate() == other.average_rate()
    
    def __gt__(self, other):
        if not isinstance(other, Lector):
            print('Сравнение некорректно!')
        else:
            return self.average_rate() > other.average_rate()

class Reviewer(Mentor):
    def __init__(self, name, last_name):
        super().__init__(name, last_name)  
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.last_name}'
    

##dlya proverki moego koda
"""    
lector = Lector('Vitya', 'Barashkin')
lector2 = Lector('Katya', 'Barashkina')
revie = Reviewer('Andrey', 'Sokolov')
lector.courses_attached.append('Python')
lector.courses_attached.append('Java')
print(lector.grades)
student = Student('Masha', 'Class', 'Ne masha...')
student.courses_in_progress.append('Python')
student.courses_in_progress.append('Java')
student.rate_lector(lector, 'Python', 10)
student.rate_lector(lector, 'Python', 5)
student.rate_lector(lector, 'Java', 10)
student.rate_lector(lector2, 'Python', 10)
student.rate_lector(lector2, 'Python', 10)
student.rate_lector(lector2, 'Java', 10)
revie.courses_attached.append('Python')
revie.rate_hw(student, 'Python', 5)
revie.rate_hw(student, 'Python', 5)
revie.rate_hw(student, 'Python', 4)
print(lector)
print(lector2)
print(student)
print(revie)
print(lector == lector2)
print(lector < lector2)
print(lector > lector2)
"""