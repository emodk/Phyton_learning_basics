students_dict = {}
info = input()
while ":" in info:
    details = info.split(":")
    name, i_d, course = details[0], details[1], details[2]
    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][name] = i_d
    info = input()
students_by_course = students_dict[info]
# print(students_by_course)
for key, value in students_by_course.items():
    print(f"{key} - {value}")
