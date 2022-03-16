import random
guess=random.randint(1,9)
chance=0
print("Guess a number between 1 to 9")
while chance < 5:
    user_input=int(input("Enter your guess: "))
    if guess==user_input:
        print("Congratulations!! you won")
        break
    elif guess>user_input:
        print("Your guess is too low.Guess a number higher than ",user_input)
    else:
        print("Your guess is too high.Guess a number lesser than ",user_input)
    chance+=1
if not chance<5:
    print("You lose!! The number was ",guess)