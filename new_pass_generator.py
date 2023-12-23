#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for i in range(nr_letters):
  if i < nr_letters:
    a = random.randint(0,len(letters)-1)
    password.append(letters[a])

  if i < nr_symbols:
    b = random.randint(0,len(symbols)-1)
    password.append(symbols[b])

  if i < nr_numbers:
    c = random.randint(0,len(numbers)-1)
    password.append(numbers[c])

# final_pass = []

# for i in range(len(password)):
#     a = random.randint(0,len(password)-1)
#     final_pass.append(a)




# passw = ""

# for i in range(len(final_pass)):
#   passw+=final_pass[i]
passw = ""
for i in password:
  passw += i

print(passw)

new_pass = ""

for _ in passw:
  a = random.randint(0,len(passw)-1)
  new_pass += passw[a]

print(new_pass)
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P