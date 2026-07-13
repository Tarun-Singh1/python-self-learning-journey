secret_word = "Storm".lower()

correct_letter_correct_position = "✓"
correct_letter_wrong_position = "?"
wrong_letter_entirely = "✗"

secret_list = list(secret_word)
guess_history = []

for attempt in range(6):
    if guess_history:
        print("\n--- History ---")
        for past_result in guess_history:
            print(past_result)
        print("---------------\n")

    while True:
        guess = input(f"Attempt {attempt + 1}/6: Enter the guess: ").strip().lower()
        if len(guess) != 5:
            print("Not a 5-letter word. Try again. (doesn't count as attempt)")
            continue
        break

    guess_list = list(guess)
    remaining_secret = secret_list.copy()
    answer_list = [None] * 5

    # Pass 1: Mark exact matches
    for i in range(5):
        if guess_list[i] == secret_list[i]:
            answer_list[i] = correct_letter_correct_position
            remaining_secret[i] = None

    # Pass 2: Mark misplaced matches
    for i in range(5):
        if answer_list[i] is None:
            if guess_list[i] in remaining_secret:
                answer_list[i] = correct_letter_wrong_position
                match_index = remaining_secret.index(guess_list[i])
                remaining_secret[match_index] = None
            else:
                answer_list[i] = wrong_letter_entirely

    result = " | ".join([f"{guess_list[i]} {answer_list[i]}" for i in range(5)])
    print(result)
    guess_history.append(result)

    if guess == secret_word:
        print("\n🎉 You won!")
        break
else:
    print(f"\n💀 You lost. The word was: {secret_word.upper()}")