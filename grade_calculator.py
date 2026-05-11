# grade_calculator.py

subjects = {}
num = int(input("How many subjects? "))

for i in range(num):
    name = input(f"Subject {i+1} name: ")
    marks = float(input(f"Marks out of 100: "))
    subjects[name] = marks
total = sum(subjects.values())
percentage = total / num

print(f"\n--- Result ---")
for sub, mark in subjects.items():
    print(f"{sub}: {mark}")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 75:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 45:
    print("Grade: C")
else:
    print("Grade: Fail")