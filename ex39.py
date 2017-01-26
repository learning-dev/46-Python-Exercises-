import random

name = raw_input("Hello, what is your name? :")
print "Well, {}, I am thinking of a number between 1 and 20.".format(name)
print "Take a guess"
tries = 0
while True:
    rand_num = random.randrange(1, 20)
    guess = raw_input()
    tries += 1
    if int(guess) == rand_num:
        print "Good job, {0}! You guessed my number in {1} guesses! ".format(name, tries)
        break
    elif int(guess) <= rand_num:
        print "Your guess is too low"
    else:
        print "Your guess is too high"

s