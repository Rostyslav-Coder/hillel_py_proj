"""
    This is modul with 1 task  HW 12 Rostyslav Putnikov
"""

# Создать иерархию классов для описания академии.
# Примерный список классов: Person, Teacher, Student, Subject, Academy и тд.
# Продумать архитектуру: реализовать принципы ООП


class Person:
    """
    Class Person
    """

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        """
        Class function
        """
        return self.__name

    @name.setter
    def name(self, name):
        if name:
            self.__name = name

    def show_info(self):
        """
        Class function
        """
        print(f"Name: {self.__name}", end="  ")


# Создаем класс "Teacher", наследник класса "Person".
# От класса родителя получаем поле "name" и дополняем двумя новыми:
# "work_period" и "profession".
# Также от класса родителя получаем функцию "show_info" и дополняем ее.
class Teacher(Person):
    """
    Class Teacher child of Person
    """

    def __init__(self, name, work_period, profession):
        super().__init__(name)
        self._work_period = work_period
        self._profssn = profession

    @property
    def work_period(self):
        """
        Class function
        """
        return self._work_period

    @work_period.setter
    def work_period(self, work_period):
        if work_period:
            self._work_period = work_period

    @property
    def profession(self):
        """
        Class function
        """
        return self._profssn

    @profession.setter
    def profession(self, profession):
        if profession:
            self._profssn = profession

    def show_info(self):
        super().show_info()
        print(f"Work period: {self._work_period} Profession: {self._profssn}")


# Создаем класс "Student", наследник класса "Person".
# От класса родителя получаем поле "name" и дополняем двумя новыми:
# "house" и "patronus".
# Также от класса родителя получаем функцию "show_info" и дополняем ее.
class Student(Person):
    """
    Class Student child of Person
    """

    def __init__(self, name, house, patronus):
        super().__init__(name)
        self._house = house
        self._patronus = patronus

    @property
    def house(self):
        """
        Class function
        """
        return self._house

    @house.setter
    def house(self, house):
        if house:
            self._house = house

    @property
    def patronus(self):
        """
        Class function
        """
        return self._patronus

    @patronus.setter
    def patronus(self, patronus):
        if patronus:
            self._patronus = patronus

    def show_info(self):
        super().show_info()
        print(f"House: {self._house}  Patronus: {self._patronus}")


# Создаем класс "Subject", независимый от классов
# "Person", "Teacher" и "Student".
# Внутри класса создаем поля "subject_name" и "subject_hours",
# функцию "subject_show_info".
class Subject:
    """
    Class Subject
    """

    def __init__(self, subject_name, subject_hours):
        self._subject_name = subject_name
        self._subject_hours = subject_hours

    @property
    def subject_name(self):
        """
        Class function
        """
        return self._subject_name

    @subject_name.setter
    def subject_name(self, subject_name):
        if subject_name:
            self._subject_name = subject_name

    @property
    def subject_hours(self):
        """
        Class function
        """
        return self._subject_hours

    @subject_hours.setter
    def subject_hours(self, subject_hours):
        if subject_hours > 0:
            self._subject_hours = subject_hours

    def subject_show_info(self):
        """
        Function to print info
        """
        print(
            f"Subject name: {self._subject_name} end=' '"
            f"Subject hours: {self._subject_hours}"
        )


# Создаем класс "Academy", независимый от классов
# "Person", "Teacher", "Student" и "Subject".
# В классе "Academy" создаем методы для добавления и удаления
# объектов классов "Teacher", "Student" и "Subject".
class Academy:
    """
    Class Academy
    """

    def __init__(self, teachers, students, subjects):
        self.__teachers = teachers
        self.__students = students
        self.__subjects = subjects

    @property
    def teachers(self):
        """
        Class function
        """
        return self.__teachers

    @teachers.setter
    def teachers(self, teachers):
        self.__teachers = teachers

    def add_teachers(self, teachers):
        """
        Class function
        """
        self.__teachers.append(teachers)

    def remove_teachers(self, teachers):
        """
        Class function
        """
        self.__teachers.remove(teachers)

    @property
    def students(self):
        """
        Class function
        """
        return self.__students

    @students.setter
    def students(self, students):
        self.__students = students

    def add_students(self, students):
        """
        Class function
        """
        self.__students.append(students)

    def remove_students(self, students):
        """
        Class function
        """
        self.__students.remove(students)

    @property
    def subjects(self):
        """
        Class function
        """
        return self.__subjects

    @subjects.setter
    def subjects(self, subjects):
        self.__subjects = subjects

    def add_subjects(self, subjects):
        """
        Class function
        """
        self.__subjects.append(subjects)

    def remove_subjects(self, subjects):
        """
        Class function
        """
        self.__subjects.remove(subjects)

    def show_academy_info(self):
        """
        Function to print info
        """
        for teacher in self.__teachers:
            print(
                f"Taecher name: {teacher.name}"
                f"Teacher work period: {teacher.work_period}"
                f"Teacher subject: {teacher.profession}"
            )
        print()
        for student in self.__students:
            print(
                f"Student name: {student.name}"
                f"Student house: {student.house}"
                f"Student patronus: {student.patronus}"
            )
        print()
        for subject in self.__subjects:
            print(
                f"Subject name: {subject.subject_name}"
                f"Subject hours: {subject.subject_hours}"
            )


# Создаем объекты класса "Teacher" и присваиваем их в список "ac_teachers"
teacher_1 = Teacher(
    "prof. Albus Dumbledore",
    "1928 - 1997",
    ["Dark Arts Defense", "Transfiguration"],
)
teacher_2 = Teacher(
    "prof. Minerva McGonagall",
    "1956 - 1998",
    "Transfiguration",
)
teacher_3 = Teacher(
    "Roland Trick",
    "1966 - 2020",
    "Flying on broomsticks",
)
teacher_4 = Teacher(
    "Quirinus Quirrell",
    "1991 - 1992",
    "Dark Arts Defense",
)
teacher_5 = Teacher(
    "Rubeus Hagrid",
    "1960",
    "Caring for Magical Creatures",
)
ac_teachers = [teacher_1, teacher_2, teacher_3, teacher_4]
print("Create an object teacher_1:")
teacher_1.show_info()
print()

# Создаем объекты класса "Student" и присваиваем их в список "ac_students"
student_1 = Student("Harry Potter", "Gryffindor", "Stag")
student_2 = Student("Hermione Granger", "Gryffindor", "Otter")
student_3 = Student("Ron Weasley", "Gryffindor", "Jack Russell Terrier")
student_4 = Student("Draco Malfoy", "Slytherin", None)
student_5 = Student("Ginny Weasley", "Gryffindor", "Horse")
ac_students = [student_1, student_2, student_3, student_4]
print("Create an object student_1:")
student_1.show_info()
print()
print("Show all students in student list:")
for _ in ac_students:
    _.show_info()
print()

# Создаем объекты класса "Subject" и присваиваем их в список "ac_subjects"
subject_1 = Subject("Dark Arts Defense", 72)
subject_2 = Subject("Transfiguration", 68)
subject_3 = Subject("Flying on broomsticks", 52)
subject_4 = Subject("Caring for Magical Creatures", 42)
ac_subjects = [subject_1, subject_2, subject_3, subject_4]
print("Create an object subject_1:")
subject_1.subject_show_info()
print()

# Создаем объект класса "Academy" и присваеваем его полям
# списки объектов классов "Teacher", "Student" и "Subject"
hogwarts = Academy(ac_teachers, ac_students, ac_subjects)
print("Create an object Hogwarts:")
hogwarts.show_academy_info()
print()

# Проверяем метод "add_teachers" и метод "add_students"
print("Add new Teacher object and Student object in Hogwarts object:")
hogwarts.add_teachers(teacher_5)
hogwarts.add_students(student_5)
hogwarts.show_academy_info()
print()

# Проверяем метод "remove_teachers" и метод "remove_students"
print("Remove Teacher object and Student object in Hogwarts object:")
hogwarts.remove_teachers(teacher_4)
hogwarts.remove_students(student_4)
hogwarts.show_academy_info()
