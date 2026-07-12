import random
secret = random.randint(1, 100)

print("The computer has picked a number between 1 and 100.")
print("You get 7 attempts. Don't embarrass yourself.")

for i in range(7):

    attempt = i + 1
    guess = int(input(f"Attempt {attempt} / 7 → Your guess: "))

    if guess == secret:
        if attempt == 1:
            print("ARE YOU CHEATING?? No one gets it in 1.")
        elif attempt in [2, 3]:
            print("Okay that was actually fire. Respect.")
        elif attempt in [4, 5]:
            print("Decent. Not impressive, but decent.")
        else:
            print("Took you long enough but sure, we'll count it.")
        break

    difference = abs(guess - secret)
    hint = "Go higher" if guess < secret else "Go lower"

    if attempt < 7:
        if difference <= 2:
            print(f"SO CLOSE and you STILL missed. {hint}.")
        elif difference <= 10:
            print(f"Warm... but still wrong. {hint}.")
        elif difference <= 25:
            print(f"Getting there but not really. {hint}.")
        else:
            print(f"Not even close bro. {hint}.")
    else:
        print(f"\nBro used all 7 attempts and STILL couldn't guess {secret}.")
        print("Touch grass. Uninstall Python.")