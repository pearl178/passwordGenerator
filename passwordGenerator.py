# Password Generator Project
# Import elements needed for generating as three lists 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Get input from users
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Generating password
password = ""
for element in range(0,nr_letters):
 password += random.choice(letters)
for element in range(0,nr_symbols):
 password += random.choice(symbols)
for element in range(0,nr_numbers):
 password += random.choice(numbers)

# Randomize the order of characters in the password
password_random = ""
chars = []
for n in range(0,len(password)):
  chars.append(password[n])
for n in range(0,len(password)):
  password_random += random.choice(chars)
print(password_random)
