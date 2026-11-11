secret = 27
attemps = 5

print("Welcome to the  number Guessing Game!")
print("guess a number between 1 and 50")

while attemps > 0:
    guess = int(input("enter your guess:"))

    if guess == secret:
        print("Congratulations! You guessed the number!")
        break
    elif guess < secret:
        print("Your guess is too low.")

        if secret - guess <= 5:
            print("HOT!")
        elif secret - guess <= 10:
            print("WARM!")
        elif secret - guess <= 20:
            print("COLD!")
        else:
            print("Ice cold!")
    else:
        print("Your guess is too high.")

        if guess - secret <= 5:
            print("HOT!")
        elif guess - secret <= 10:
            print("WARM!")
        elif guess - secret <= 20:
            print("COLD!")
        else:
            print("Ice cold!")

    if guess != secret:
        attemps = attemps - 1

        for i in range(attemps):
            print("❤️", end=" ")
    print("\nRemaining attempts:", attemps)
if attemps == 0 and guess != secret:
    print("game over!")
    print("The secret number was:", secret)