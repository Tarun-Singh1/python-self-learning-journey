students = [
    ("Tarun", 3.73, 45),
    ("Arjun", 2.91, 30),
    ("Priya", 3.95, 60),
    ("Sam", 3.50, 28),
    ("Neha", 2.45, 55),
    ("Riya", 3.81, 40),
]

honors = []
support = []

for name, gpa, credits in students:
    if gpa >= 3.7 and credits >= 35:
        honors.append((gpa, name))
    elif gpa < 3.0:
        support.append((gpa, name))

honors.sort(reverse=True)
support.sort()

print("Eligible for honors:")
for gpa, name in honors:
    print(f"- {name:<9} GPA: {gpa}")

print("\nNeeds academic support:")
for gpa, name in support:
    print(f"- {name:<9} GPA: {gpa}")