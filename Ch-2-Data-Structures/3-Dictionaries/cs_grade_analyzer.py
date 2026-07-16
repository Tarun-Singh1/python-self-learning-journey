from collections import defaultdict

enrollments = [
    ("Tarun", "CS1337", 88), ("Tarun", "CS2305", 76), ("Tarun", "CS3345", 91),
    ("Priya", "CS1337", 95), ("Priya", "CS2305", 89), ("Priya", "CS3345", 97),
    ("Arjun", "CS1337", 62), ("Arjun", "CS2305", 70), ("Arjun", "CS3345", 55),
    ("Sam", "CS1337", 73), ("Sam", "CS3345", 68),
    ("Neha", "CS2305", 91), ("Neha", "CS3345", 88),
    ("Riya", "CS1337", 79), ("Riya", "CS2305", 83),
]
student_data = defaultdict(list)
course_data = defaultdict(list)

for name, course, score in enrollments:
    student_data[name].append(score)
    course_data[course].append((name, score))

print("=== STUDENT REPORT CARDS ===")
student_summaries = {}

for name, scores in student_data.items():
    avg = sum(scores) / len(scores)

    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    else:
        grade = 'F'

    student_summaries[name] = {"avg": avg, "min_score": min(scores)}
    print(f"{name:<8} | Avg: {avg:.2f} | Grade: {grade}")

print("\n=== COURSE DIFFICULTY (hardest first) ===")
course_averages = {}
top_students = {}

for course, records in course_data.items():
    scores = [score for name, score in records]
    course_averages[course] = sum(scores) / len(scores)
    best_student_record = max(records, key=lambda x: x[1])
    top_students[course] = best_student_record

sorted_courses = sorted(course_averages.items(), key=lambda item: item[1])
for course, avg in sorted_courses:
    print(f"{course:<8} | Avg: {avg:.2f}")

print("\n=== TOP STUDENT PER COURSE ===")
for course, (name, score) in top_students.items():
    print(f"{course:<8} | {name} ({score})")

print("\n=== AT-RISK STUDENTS ===")
for name, stats in student_summaries.items():
    if stats["min_score"] < 65 and stats["avg"] < 75:
        print(name)

print("\n=== DEPARTMENT STATS ===")
all_scores = [score for name, course, score in enrollments]
dept_avg = sum(all_scores) / len(all_scores)

highest_record = max(enrollments, key=lambda x: x[2])
lowest_record = min(enrollments, key=lambda x: x[2])

print(f"Department average: {dept_avg:.2f}")
print(f"Highest score: {highest_record[0]} in {highest_record[1]} ({highest_record[2]})")
print(f"Lowest score: {lowest_record[0]} in {lowest_record[1]} ({lowest_record[2]})")