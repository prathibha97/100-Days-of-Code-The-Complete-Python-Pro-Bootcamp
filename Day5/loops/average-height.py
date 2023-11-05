# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

# total_height = sum(student_heights)
# num_of_students = len(student_heights)
# avg_height = round(total_height / num_of_students)
# print(avg_height)

total_height = 0
num_of_students = 0

for height in student_heights:
  total_height += height
print(f"total height = {total_height}")
  
for student in student_heights:
  num_of_students += 1
print(f"number of students = {num_of_students}")
  
avg_height = round(total_height / num_of_students)
print(f"average height = {avg_height}")
