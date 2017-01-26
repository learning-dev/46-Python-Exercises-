# program of guessing game to create an anagram of random word in a list and make the user guess it

import random


def index_random(list_index):
    temp = []
    while list_index != []:  # iterate till list is empty
        random_gen = random.randrange(len(list_index))   # generate the random index and append
        temp.append(list_index.pop(random_gen))
    return temp


def get_anagram(in_list):    # to get anagram e.g. blue as "buel" or similar
    n = len(in_list)
    list_index  = random.randrange(0, n)   # selecting an index randomly
    index_list = []
    list_ele =  in_list[list_index]        # element of the random index
    for i in range(len(in_list[list_index])):  # make a list of indexes of element blue = [0,1,2,3]
        index_list.append(i)
    new_anagram = index_random(index_list)    # to randomize the sequence
    new_str = ''
    for i in new_anagram:              # creating an element using random sequence of element
        new_str += list_ele[i]
    temp_list = list()
    temp_list.append(new_str)            # list = element + random sequence of the element
    temp_list.append(list_ele)
    return temp_list


in_list = raw_input("Enter a list of words:")
if in_list.isspace():   # input check
    print "Invalid input"
    exit()
in_list = in_list.split()   # splitting the input with spaces
anagram = get_anagram(in_list)   # getting anagram (jumbled word) and corresponding word
print anagram[0]
#print "color words: {}".format({anagram})
while True:
    guess = raw_input("Enter your guess:")  # staring the game
    if guess ==anagram[1] :  # stop when the guess is correct
        print "Correct!"
        break
    else:
        print "Wrong! Try again"
     # continue