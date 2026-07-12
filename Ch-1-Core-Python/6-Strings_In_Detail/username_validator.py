entered_username = input("Choose a username: ")
print(f"You chose username: {entered_username}")

#Validate length
valid_length = True if 3 <= len(entered_username) <= 15 else False
is_only_letter_n_symbol = True if entered_username.isalnum() else False
start_with_num = True if entered_username[0].isdigit() else False
have_admin = True if "admin" in entered_username.lower() else False
is_banned = True if (entered_username == "root" or entered_username == "test" or
                     entered_username == "user" or entered_username == "guest") else False

temp_username = entered_username
if valid_length and is_only_letter_n_symbol and not start_with_num and not have_admin and not is_banned:
    print(f"Username accepted. Welcome, {entered_username}!")
else:
    if not valid_length:
        print("- Insufficient length!")
    if not is_only_letter_n_symbol:
        print("- Contains invalid characters!")
    if start_with_num:
        print("- Can't start with a number!")
        temp_username = "user_" + temp_username
    if have_admin:
        print("- Username can't have admin in it!")
        temp_username += "_2026"
    if is_banned:
        print("- Not allowed to use this username!")

    temp_username = entered_username.strip().lower()
    temp_username = temp_username.replace(" ", "_")

    cleaned = ""
    for char in temp_username:
        if char.isalnum() or char == "_":
            cleaned += char
    temp_username = cleaned

    if temp_username and temp_username[0].isdigit():
        temp_username = "user_" + temp_username

    if len(temp_username) < 3:
        temp_username += "_2026"
    elif len(temp_username) > 15:
        temp_username = temp_username[:15]

    if "admin" in temp_username or temp_username in ["root", "test", "user", "guest"]:
        temp_username += "_2026"

    print(f"\nSuggested username: {temp_username}")
    print("That username works! Go with it?")


