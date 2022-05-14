def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_chosen = [choice(letters) for _ in range(0, randint(8, 10))]
    symbols_chosen = [choice(symbols) for _ in range(0, randint(2, 4))]
    numbers_chosen = [choice(numbers) for _ in range(0, randint(2, 4))]
    password = letters_chosen + symbols_chosen + numbers_chosen
    shuffle(password)
    password_random = "".join(password)
    password_input.insert(0, password_random)
    pyperclip.copy(password_random)
