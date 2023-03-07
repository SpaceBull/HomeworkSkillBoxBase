import random
from operator import itemgetter


class Student:
    all_students = []

    def __init__(self, data_name='Долматов Иван', number_of_group=3, grade=None):
        self.data_name = data_name
        self.number_of_group = number_of_group
        self.grade = grade
        self.all_students = list()

    def adds_students(self):
        Student.all_students.append([self.data_name, self.number_of_group, sorted(self.grade)])

    def print_info(self):
        roster = sorted(Student.all_students, key=itemgetter(2), reverse=True)
        for i_elem in roster:
            self.data_name = i_elem[0]
            self.number_of_group = i_elem[1]
            self.grade = i_elem[2]
            print(f'Ученик {self.data_name} учится в группе {self.number_of_group} c оценками {self.grade}')


for _ in range(10):
    names = ['-', 'Коля', 'Александр', 'Дима', 'Николай', 'Иван']
    surname = ['Брин', 'Долматов', 'Дондуков', 'Быков', 'Иванов', 'Петров', 'Печкин']
    grade_student = [random.randint(2, 5) for _ in range(5)]
    number_random = random.randint(1, 5)
    number_surname = random.randint(0, 6)
    the_name = ''.join(surname[number_surname] + ' ' + names[number_random])
    new_student = Student(the_name, number_random, grade_student)
    new_student.adds_students()


result = Student()
result.print_info()


