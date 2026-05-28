class Student:
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка'
        if course not in self.courses_in_progress:
            return 'Ошибка'
        if course not in lecturer.courses_attached:
            return 'Ошибка'
        if not 1 <= grade <= 10:
            return 'Ошибка'

        lecturer.grades.setdefault(course, []).append(grade)

    def get_average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)

        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        average_grade = round(self.get_average_grade(), 1)

        return (
            f'Имя: {self.first_name}\n'
            f'Фамилия: {self.last_name}\n'
            f'Средняя оценка за домашние задания: {average_grade}\n'
            f'Курсы в процессе изучения: {courses_in_progress}\n'
            f'Завершенные курсы: {finished_courses}'
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() <= other.get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() >= other.get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() == other.get_average_grade()


class Mentor:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.grades = {}

    def get_average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)

        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        average_grade = round(self.get_average_grade(), 1)
        return (
            f'Имя: {self.first_name}\n'
            f'Фамилия: {self.last_name}\n'
            f'Средняя оценка за лекции: {average_grade}'
        )

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() <= other.get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() >= other.get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() == other.get_average_grade()


class Reviewer(Mentor):
    def rate_homework(self, student, course, grade):
        if not isinstance(student, Student):
            return 'Ошибка'
        if course not in self.courses_attached:
            return 'Ошибка'
        if course not in student.courses_in_progress:
            return 'Ошибка'
        if not 1 <= grade <= 10:
            return 'Ошибка'

        student.grades.setdefault(course, []).append(grade)

    def __str__(self):
        return f'Имя: {self.first_name}\nФамилия: {self.last_name}'


def get_students_average_grade(students, course):
    course_grades = []
    for student in students:
        course_grades.extend(student.grades.get(course, []))

    if not course_grades:
        return 0
    return sum(course_grades) / len(course_grades)


def get_lecturers_average_grade(lecturers, course):
    course_grades = []
    for lecturer in lecturers:
        course_grades.extend(lecturer.grades.get(course, []))

    if not course_grades:
        return 0
    return sum(course_grades) / len(course_grades)


if __name__ == '__main__':
    lecturer_1 = Lecturer('Иван', 'Иванов')
    lecturer_2 = Lecturer('Анна', 'Смирнова')

    reviewer_1 = Reviewer('Пётр', 'Петров')
    reviewer_2 = Reviewer('Мария', 'Соколова')

    student_1 = Student('Ольга', 'Алёхина', 'Ж')
    student_2 = Student('Алексей', 'Морозов', 'М')

    student_1.courses_in_progress += ['Python', 'Java']
    student_1.finished_courses += ['Введение в программирование']
    student_2.courses_in_progress += ['Python', 'Git']
    student_2.finished_courses += ['Основы HTML']

    lecturer_1.courses_attached += ['Python', 'C++']
    lecturer_2.courses_attached += ['Python', 'Git']

    reviewer_1.courses_attached += ['Python', 'C++']
    reviewer_2.courses_attached += ['Python', 'Git', 'Java']

    print(isinstance(lecturer_1, Mentor))
    print(isinstance(reviewer_1, Mentor))
    print(lecturer_1.courses_attached)
    print(reviewer_1.courses_attached)
    print()

    print(student_1.rate_lecture(lecturer_1, 'Python', 7))
    print(student_1.rate_lecture(lecturer_1, 'Java', 8))
    print(student_1.rate_lecture(lecturer_1, 'C++', 8))
    print(student_1.rate_lecture(reviewer_1, 'Python', 6))
    print(lecturer_1.grades)
    print()

    reviewer_1.rate_homework(student_1, 'Python', 8)
    reviewer_1.rate_homework(student_1, 'Python', 9)
    reviewer_2.rate_homework(student_1, 'Java', 10)
    reviewer_1.rate_homework(student_2, 'Python', 7)
    reviewer_2.rate_homework(student_2, 'Git', 9)

    student_2.rate_lecture(lecturer_1, 'Python', 9)
    student_1.rate_lecture(lecturer_2, 'Python', 10)
    student_2.rate_lecture(lecturer_2, 'Git', 8)

    print(reviewer_1)
    print()
    print(lecturer_1)
    print()
    print(student_1)
    print()

    print(f'Лектор 1 лучше лектора 2: {lecturer_1 > lecturer_2}')
    print(f'Студент 1 лучше студента 2: {student_1 > student_2}')
    print()

    students = [student_1, student_2]
    lecturers = [lecturer_1, lecturer_2]

    print(
        'Средняя оценка студентов по Python: '
        f'{round(get_students_average_grade(students, "Python"), 1)}'
    )
    print(
        'Средняя оценка лекторов по Python: '
        f'{round(get_lecturers_average_grade(lecturers, "Python"), 1)}'
    )
