""" Naive approach for pangram program
"""


def is_pangram(in_str):   # method to check if pangram or not
    in_str = list(sorted(in_str.lower()))  # sorting and converting to lower case
    in_str = [x for x in in_str if ' ' not in x] # removing spaces
    com_str = 'abcdefghijklmnopqrstuvwxyz'
    com_str = list(com_str)   # creating a list of 26 alphabets
    return set(in_str) == set(com_str)  # comparing the sets for pangram

while True:
    in_str = raw_input()
    if len(in_str) is 0 or in_str.isspace():
        print "Input Error. Please enter valid input"
        continue
    else:
        break
print is_pangram(in_str)
