"""
GP CALCULATOR
"""
grade = {
	'A':5, 'B':4, 'C':3, 'D': 2, 'E':1, 'F':0
}
num_courses = input('how many courses did you take?\n')

course = []
course_unit = []
grade_score = []
result = []
for idx in range(1, num_courses+1):
    course.append(raw_input('input course %d \n' % idx))
    course_unit.append(input('input unit for course %d \n' % idx))
    x =input('input your score for course %d \n' % idx)
    if 70 <= x <=100:
        grade_score.append(grade['A'])
    elif 60 <= x <70:
        grade_score.append(grade['B'])
    elif 50 <= x <60:
        grade_score.append(grade['C'])
    elif 45 <= x <50:
        grade_score.append(grade['D'])
    elif 40 <= x <45:
        grade_score.append(grade['E'])
    elif 0 <= x <40:
        grade_score.append(grade['F'])

for idx in range(num_courses):
    result.append(course_unit[idx] * grade_score[idx])

final_result = sum(result) / float(sum(course_unit))
print "your gp is ", final_result
