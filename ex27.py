# Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list comprehensions.

# 1. using for-loop


def str_to_intlen(list):
    len_words= []
    count = 0
    for i in list:
        count = 0
        for j in i:
            count += 1
        len_words += [count]

    return len_words

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

