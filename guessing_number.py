secret_number = 7
guess_count = 0
attempts = 3
while guess_count < attempts:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("you won bitch!")
        break
else:
    print("you lost bitch!")