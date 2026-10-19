from course import Course, InvalidMarksError,load_course

c = Course("Programming for AI")
c.add_student("Ali", 88)
c.add_student("Sara", 92)
c.add_student("Omar", 75)

try:
    c.add_student("Bilal", 120)
except InvalidMarksError as e:
    print("Error:", e)

print(c)

course = load_course("Programming for AI", "marks.txt")
print(course)
print("Top student:", course.top_student())

