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
        
    @classmethod
    def average_rate_for_course(cls, course, students):
        av_rate = 0
        count = 0
        for student in students:
            if course in student.courses_in_progress and len(student.grades.values()) != 0:
                av_rate += round(sum(student.grades.get(course)) / len(student.grades.get(course)), 1)
                count += 1
        return round((av_rate / count), 1)
    
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
        
    @classmethod
    def average_rate_for_course(cls, course, lectors):
        av_rate = 0
        count = 0
        for lector in lectors:
            if course in lector.courses_attached and len(lector.grades.values()) != 0:
                av_rate += round(sum(lector.grades.get(course)) / len(lector.grades.get(course)), 1)
                count += 1
        return round((av_rate / count), 1)

class Reviewer(Mentor):
    def __init__(self, name, last_name):
        super().__init__(name, last_name)  
    
    def rate_student(self, student, course, grade):
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

student1 = Student('Маша', 'Миронова', 'Ж')
student2 = Student('Петя', 'Гринев', 'М')
student1.add_finished_courses('Python')
student1.add_finished_courses('Java')
student1.courses_in_progress.append('C++')
student1.courses_in_progress.append('Full-stack Python')
student2.add_finished_courses('Java')
student2.add_finished_courses('C++')
student2.courses_in_progress.append('Full-stack Python')

lector1 = Lector('Андрей', 'Соколов')
lector2 = Lector('Ирина', 'Соколова')
lector1.courses_attached.append('Python')
lector1.courses_attached.append('Java')
lector1.courses_attached.append('C++')
lector2.courses_attached.append('Full-stack Python')
lector2.courses_attached.append('Java')
lector2.courses_attached.append('C++')
student1.rate_lector(lector1, 'Python', 7)
student1.rate_lector(lector1, 'Python', 10)
student1.rate_lector(lector1, 'Python', 1)
student1.rate_lector(lector1, 'Java', 7)
student1.rate_lector(lector1, 'Java' , 2)
student1.rate_lector(lector1, 'Java' , 10)
student1.rate_lector(lector1, 'C++' , 7)
student1.rate_lector(lector1, 'C++' , 5)
student1.rate_lector(lector1, 'C++' , 10)
student1.rate_lector(lector2, 'C++' , 7)
student1.rate_lector(lector2, 'C++' , 7)
student1.rate_lector(lector2, 'C++' , 7)
student1.rate_lector(lector2, 'Java' , 10)
student1.rate_lector(lector2, 'Java' , 10)
student1.rate_lector(lector2, 'Java' , 10)
student1.rate_lector(lector2, 'Full-stack Python' , 10)
student1.rate_lector(lector2, 'Full-stack Python' , 10)
student1.rate_lector(lector2, 'Full-stack Python' , 10)

revie1 = Reviewer('Кэтрин', 'Эрншо')
revie2 = Reviewer('Эдгар', 'Линтон')
revie1.courses_attached.append('Python')
revie1.courses_attached.append('Java')
revie1.courses_attached.append('C++')
revie1.courses_attached.append('Full-stack Python')
revie1.rate_student(student1, 'Full-stack Python', 10)
revie1.rate_student(student1, 'Full-stack Python', 10)
revie1.rate_student(student1, 'Full-stack Python', 3)
revie1.rate_student(student1, 'C++', 10)
revie1.rate_student(student1, 'C++', 10)
revie1.rate_student(student1, 'C++', 6)
revie1.rate_student(student2, 'Full-stack Python', 10)
revie1.rate_student(student2, 'Full-stack Python', 10)
revie1.rate_student(student2, 'Full-stack Python', 10)

print('ДЕЙСТВИЯ СО СТУДЕНТАМИ:\n')
print(student1, '\n')
print(student2, '\n')
print('Средняя оценка студентов на курсе Full-stack Python: ', Student.average_rate_for_course('Full-stack Python', [student1, student2]))
print('Средняя оценка студентов на курсе C++: ', Student.average_rate_for_course('C++', [student1, student2]))


print('\nДЕЙСТВИЯ С ЛЕКТОРАМИ:\n')
print(lector1,'\n')
print(lector2,'\n')
print(f'Сравнение средней оценки лекторов:\n{lector1.name, lector1.average_rate()} < {lector2.name, lector2.average_rate()}', lector1.average_rate() < lector2.average_rate())
print(f'{lector1.name, lector1.average_rate()} > {lector2.name, lector2.average_rate()}', lector1.average_rate() > lector2.average_rate())
print(f'{lector1.name, lector1.average_rate()} = {lector2.name, lector2.average_rate()}', lector1.average_rate() == lector2.average_rate())
print('Средняя оценка лекторов на курсе C++: ', Lector.average_rate_for_course('C++', [lector1, lector2]))
print('Средняя оценка лекторов на курсе Python: ', Lector.average_rate_for_course('Python', [lector1, lector2]))

print('\nДЕЙСТВИЯ С ПРОВЕРЯЮЩИМИ:\n')
print(revie1, '\n')
print(revie2, '\n')