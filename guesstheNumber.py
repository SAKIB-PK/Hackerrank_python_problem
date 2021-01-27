import random
secretNumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20.")
#Ask player  6 time
for i in range (1,7):
    guess = int(input("Take a guess."))
    if guess < secretNumber:
            print("Your guess to low.")
            
    elif guess > secretNumber:
            print ("you are guess too high.")
    else:
            break
if guess == secretNumber:
    print("Good job! You guessed my number in " + str(i) + " guesses!")
else:
    print("Nope.The number I was thinking of was " + str(secretNumber) )
