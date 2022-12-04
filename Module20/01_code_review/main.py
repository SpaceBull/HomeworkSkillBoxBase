students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def writes_out_interests(roster_students):
    new_roster_interests = []
    surnames = ''
    for student_id in roster_students:
        surnames += roster_students[student_id]['surname']
        new_roster_interests += (roster_students[student_id]['interests'])
    count_letter = len(surnames)
    new_roster_interests = set(new_roster_interests)
    return count_letter, new_roster_interests


pairs = []
for id_student in students:
    pairs.append((id_student, students[id_student]['age']))

the_number_of_letters_in_the_surname = writes_out_interests(students)[0]
new_roster = writes_out_interests(students)[1]

print(f'Список пар "ID студента — возраст": {pairs}')
print(f'Полный список интересов всех студентов: {new_roster}')
print(f'Общая длина всех фамилий студентов: {the_number_of_letters_in_the_surname}')
