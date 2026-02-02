import random

answer = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess == answer:
        print(f"Correct! It took you {attempts} guesses.")
        break
    elif guess > answer:
        print("Too high!")
    else:
        print("Too low!")

