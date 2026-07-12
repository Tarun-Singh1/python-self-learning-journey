from pickletools import dis

name = input("Enter your name: ")
age = int(input("How old is you: "))
credits_hrs = int(input("How many credits you're handling: "))
junior = age < 18

COST_PER_CREDIT_HOUR = 850
SUPPLEMENT_FEE = 200

tuition = credits_hrs * COST_PER_CREDIT_HOUR
discount = (tuition * 0.1) * junior
total_fee = (tuition + SUPPLEMENT_FEE) - discount

print("==============================")
print("     SEMESTER INVOICE")
print("==============================")
print(f"Student    : {name}")
print(f"Age        : {age}")
print(f"Credits    : {credits_hrs}")
print(f"Tuition    : ${tuition:.2f}")
print(f"Semester   : ${SUPPLEMENT_FEE:.2f}")
print(f"Discount   : ${discount:.2f}")
print("------------------------------")
print(f"TOTAL DUE  : ${total_fee:.2f}")
print("==============================")