import random
num = random.randint(1,6)

while True:
    guess=int(input("Guess A Number Between 1 TO 6: "))

    if guess==num:
        print("You guessed A Correct Number")
        break
    elif guess>num:
        print("You guessed A Greater Number")
    elif guess<num:
        print("You guessed A Smaller Number")
