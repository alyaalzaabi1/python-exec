students = {}
n = int(input("How many students? "))

for _ in range(n):
    name = input("Enter student name: ")
    grade = float(input(f"Enter grade for {name}: "))
    students[name] = grade

average = sum(students.values()) / len(students)
print("Class average:", average)
