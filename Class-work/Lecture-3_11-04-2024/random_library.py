import random

#print(random.randint(1000000,999999))
#print(random.choice([1,90,77,444,555,"tops",python,True,False]))

num = random.randint(1,20)

while True:
    guess=int(input("Guess A Number Between 1 TO 20: "))

    if guess==num:
        print("You guessed A Correct Number")
        break
    elif guess>num:
        print("You guessed A Greater Number")
    elif guess<num:
        print("You guessed A Smaller Number")

