name = input("What is your name: ")
age = int(input("How old are you: "))
gpa = float(input("What is your GPA: "))
credits_completed = int(input("Number of credits completed by you: "))
any_academic_violations = input("Any academic violations? y or n: ")

has_violation = any_academic_violations == "y"


eligible_for_scholarship = (
    gpa >= 3.5
    and credits_completed >= 30
    and (17 <= age <= 25 or False)
    and not has_violation
)

SCHOLARSHIP_RATE = 150
award_amount= (credits_completed * SCHOLARSHIP_RATE) * eligible_for_scholarship

eligible_display = "Yes" * eligible_for_scholarship or "No"
violations_display = "Yes" * has_violation or "No"

# Print Receipt
print("\n====================================")
print("       SCHOLARSHIP EVALUATION")
print("====================================")
print(f"Name          : {name}")
print(f"GPA           : {gpa:.2f}")
print(f"Credits Done  : {credits_completed}")
print(f"Age           : {age}")
print(f"Violations    : {violations_display}")
print("------------------------------------")
print(f"Eligible      : {eligible_display}")
print(f"Award Amount  : ${award_amount:.2f}")
print("====================================")