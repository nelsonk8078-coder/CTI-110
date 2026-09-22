#p2hw2 set up

grade1 = float(input("enter grade #1: "))
grade2= float(input("enter grade #2: "))
grade3= float(input("enter grade #3: "))

grade_list = [grade1, grade2, grade3]

min_grade = min(grade_list)
max_grade = max(grade_list)
sum_grade = min(grade_list)
total_grade = sum(grade_list)
count_grade = len(grade_list)
average = total_grade / count_grade

print(f"Grades: {grade_list}")
print(f"lowest: {min_grade:.2f}")
print(f"Highest: {max_grade:.2f}")
print(f"Sum: {sum_grade:.2f}")
print(f"average: {average:.2f}")

