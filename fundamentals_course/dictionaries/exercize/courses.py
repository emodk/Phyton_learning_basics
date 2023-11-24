courses = {}
course_info = input()
while course_info != "end":
    course_details = course_info.split(":")
    course_name = course_details[0]
    student_name = course_details[1]
    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name].append(student_name)
    course_info = input()
for key in courses:
    key_1 = key[:-1] + ":"
    print(f'{key_1} {len(courses[key])}')
    for i in range(len(courses[key])):
        print(f"--{courses[key][i]}")
