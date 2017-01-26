# Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list comprehensions.

# 1. using high order function map()

def str_to_intlen(list):
     return map(len_words, list)


def len_words (word): # calculates the len of the word
    return len(word)


while True:
    in_str = raw_input("Enter a string:")
    if in_str is not None:
        break
    else:
        print " Error: Invalid input "
        continue
in_list_words = in_str.split( )
print in_list_words
print str_to_intlen(in_list_words)

