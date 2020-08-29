## The user has to guess the number the computer selected
import random

minNumber = 1
maxNumber = 100

listNumbers = list(range(minNumber,maxNumber+1))

randomNumber = random.randint(1, 100)

guess = int(input())

while guess!=randomNumber:
    if guess>randomNumber:
        print("mas bajo")
    elif guess<randomNumber:
        print("mas alto")

    guess = int(input())

print("YES! The number is",randomNumber)
