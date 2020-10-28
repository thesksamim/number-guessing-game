import random
randomNum = random.randint(1, 100)

guess = 0


guessNum = None

while(guessNum != randomNum):
    guessNum = int(input("guess the number"))
    guess +=1
    if(guessNum == randomNum):
       print("you guessed the right number")
    if(guessNum > randomNum):
        print("Lower number please")
    elif(guessNum < randomNum):
        print("higher number please")
print(f"you guessed the number in {guess} attempt")


# If you break the record of previous record for how many trial it takes to guess the number currecty,
# the code below will save your achievement in "highscore.txt" file.

with open("highscore.txt") as f :
    highscore = int(f.read())

if(guess<highscore):
    print("you have just broken the High score")
    with open("highscore.txt" , "w") as f:
        f.write(str(guess))
        
