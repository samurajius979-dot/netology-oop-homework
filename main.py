# -*- coding: utf-8 -*-
"""Решение домашнего задания по ООП для учебной группы."""

ERROR_MESSAGE = 'Ошибка'


def is_valid_grade(grade):
    """Проверяет, что оценка является числом от 1 до 10."""
    if isinstance(grade, bool):
        return False

    return isinstance(grade, (int, float)) and 1 <= grade <= 10


def calculate_average(grades):
    """Возвращает среднюю оценку по словарю с оценками за курсы."""
    all_grades = []
    for course_grades in grades.values():
        all_grades.extend(course_grades)

    if not all_grades:
        return 0

    return sum(all_grades) / len(all_grades)


def calculate_course_average(people, course):
    """Возвращает среднюю оценку всех объектов по конкретному курсу."""
    course_grades = []
    for person in people:
        course_grades.extend(person.grades.get(course, []))

    if not course_grades:
        return 0

    return sum(course_grades) / len(course_grades)


def format_courses(courses):
    """Форматирует список курсов для вывода на экран."""
    if not courses:
        return 'Нет'

    return ', '.join(courses)


class Student:
    """Студент учебной группы."""

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return ERROR_MESSAGE
        if course not in self.courses_in_progress:
            return ERROR_MESSAGE
        if course not in lecturer.courses_attached:
            return ERROR_MESSAGE
        if not is_valid_grade(grade):
            return ERROR_MESSAGE

        lecturer.grades.setdefault(course, []).append(grade)

    def get_average_grade(self):
        return calculate_average(self.grades)

    def __str__(self):
        average_grade = round(self.get_average_grade(), 1)

        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {average_grade}\n'
            'Курсы в процессе изучения: '
            f'{format_courses(self.courses_in_progress)}\n'
            f'Завершенные курсы: {format_courses(self.finished_courses)}'
        )

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented

        return self.get_average_grade() == other.get_average_grade()

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


class Mentor:
    """Базовый класс для наставников."""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    """Лектор, который получает оценки от студентов."""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        return calculate_average(self.grades)

    def __str__(self):
        average_grade = round(self.get_average_grade(), 1)

        return (
            f'{super().__str__()}\n'
            f'Средняя оценка за лекции: {average_grade}'
        )

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented

        return self.get_average_grade() == other.get_average_grade()

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


class Reviewer(Mentor):
    """Проверяющий, который выставляет оценки студентам."""

    def rate_homework(self, student, course, grade):
        if not isinstance(student, Student):
            return ERROR_MESSAGE
        if course not in self.courses_attached:
            return ERROR_MESSAGE
        if course not in student.courses_in_progress:
            return ERROR_MESSAGE
        if not is_valid_grade(grade):
            return ERROR_MESSAGE

        student.grades.setdefault(course, []).append(grade)

    def __str__(self):
        return super().__str__()


def get_students_average_grade(students, course):
    """Возвращает среднюю оценку студентов за курс."""
    return calculate_course_average(students, course)


def get_lecturers_average_grade(lecturers, course):
    """Возвращает среднюю оценку лекторов за курс."""
    return calculate_course_average(lecturers, course)


def run_demo():
    """Показывает работу всех классов, методов и функций."""
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

    print('Демонстрация отказов при выставлении оценок:')

    # Отказ по роли: студент не может оценить другого студента.
    role_error = student_1.rate_lecture(student_2, 'Python', 10)
    print(f'ОТКАЗ ПО РОЛИ: {role_error}')

    # Отказ по курсу: студент не изучает C++, поэтому не может оценить лектора.
    course_error = student_1.rate_lecture(lecturer_1, 'C++', 8)
    print(f'ОТКАЗ ПО КУРСУ: {course_error}')

    # Дополнительные отказы для метода проверки домашних заданий.
    homework_role_error = reviewer_1.rate_homework(lecturer_1, 'Python', 8)
    homework_course_error = reviewer_1.rate_homework(student_1, 'Java', 8)
    print(f'ОТКАЗ ПО РОЛИ ДЛЯ ДЗ: {homework_role_error}')
    print(f'ОТКАЗ ПО КУРСУ ДЛЯ ДЗ: {homework_course_error}')
    print()

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

    assert isinstance(lecturer_1, Mentor)
    assert isinstance(reviewer_1, Mentor)
    assert role_error == ERROR_MESSAGE
    assert course_error == ERROR_MESSAGE
    assert homework_role_error == ERROR_MESSAGE
    assert homework_course_error == ERROR_MESSAGE
    assert lecturer_1.grades == {'Python': [7, 9]}
    assert student_1.grades == {'Python': [8, 9], 'Java': [10]}
    assert student_1 > student_2
    assert lecturer_2 > lecturer_1
    assert get_students_average_grade([student_1, student_2], 'Python') == 8
    assert round(get_lecturers_average_grade(
        [lecturer_1, lecturer_2], 'Python'
    ), 1) == 8.7

    print(reviewer_1)
    print()
    print(lecturer_1)
    print()
    print(student_1)
    print()

    print(f'Лектор 2 лучше лектора 1: {lecturer_2 > lecturer_1}')
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


if __name__ == '__main__':
    run_demo()
