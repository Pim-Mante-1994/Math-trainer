from random import randint
from random import uniform
from random import choice

# Trainer settings #
print(""" Hi, this is a mental math trainer. It helps you practice your mental arithmatic skills.
          You can change the difficulity by changing the range of numbers the program uses to create questions.
          The trainer will help you practice on whole and on decimal numbers. The decimal question can be rounded to 2 decimals.
          For every correct answer you get 1 point. For every incorrect answer you loose 2 points. Once you reach a score of 100 points the program closes it's self.""")
score = 0
print("Range of numbers for calculations should start at: ")
start = int(input())
print("Range of numbers for calculations should stop at: ")
stop = int(input())

#integer functions

## addition
def additionint():
    global score
    print("{}+{}".format(a, b))
    answer = int(input())
    if answer != (a + b):
        print("Wrong")
        score -= 2
    elif answer == (a + b):
        score += 1

## substraction
def substractionint():
    global score
    print("{}-{}".format(a, b))
    answer = int(input())
    if answer != (a - b):
        print("Wrong")
        score -= 2
    elif answer == (a - b):
        score += 1

## multiplication
def multiplicationint():
    global score
    print("{}*{}".format(a, b))
    answer = int(input())
    if answer != (a * b):
        print("Wrong")
        score -= 2
    elif answer == (a * b):
        score += 1

## division
def divisionint():
    global score
    print("{}/{}".format(a, b))
    answer = float(input())
    if answer != round((a / b), 2):
        print("Wrong")
        score -= 2
    elif answer == round((a / b), 2):
        score += 1

# float functions

## addition
def additionfloat():
    global score
    print("{}+{}".format(x, y))
    answer = float(input())
    if answer != (x + y):
        print("Wrong")
        score -= 2
    elif answer == (x + y):
        score += 1

## substraction
def substractionfloat():
    global score
    print("{}-{}".format(x, y))
    answer = float(input())
    if answer != (x - y):
        print("Wrong")
        score -= 2
    elif answer == (x - y):
        score += 1

## multiplication
def multiplicationfloat():
    global score
    print("{}*{}".format(x, y))
    answer = int(input())
    if answer != round((x * y), 2):
        print("Wrong")
        score -= 2
    elif answer == round((x * y), 2):
        score += 1

## division
def divisionfloat():
    global score
    print("{}/{}".format(x, y))
    answer = float(input())
    if answer != round((x / y), 2):
        print("Wrong")
        score -= 2
    elif answer == round((x / y), 2):
        score += 1

# functionlist
functionlist = [additionint, substractionint, multiplicationint, divisionint, additionfloat, substractionfloat, multiplicationfloat, divisionfloat]

# change the number here if you want more or less practice until the program closes
while score < 100:

    a = randint(start, stop)
    b = randint(start, stop)
    x = round(uniform(start, stop), 2)
    y = round(uniform(start, stop), 2)
    choice(functionlist)()

print("Good job!")
