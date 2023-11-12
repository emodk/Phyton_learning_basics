class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if self.__students_count != 0:
            self.students.append(name)
            self.grades.append(grade)
            self.__students_count -= 1

    def get_average_grade(self):
        return float(f'{(sum(self.grades)) / len(self.grades):.2f}')

    def __repr__(self):
        students = ", ".join(self.students)
        a = self.get_average_grade()
        return f'The students in {self.name}: {students}. Average grade: {a}'


# Test code
a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)