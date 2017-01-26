""" The python way of checking for a string is pangram or not """
import string


def is_pangram(in_string, alphabet=string.ascii_lowercase):  # function for checking pangram or not
    alphaset = set(alphabet) # creating a set of all lower case
    return alphaset <= set(in_string.lower()) # checking


while True:
    in_str = raw_input("Enter a string to check :")
    if in_str is None or in_str.isspace():
        print "Error: Invalid input!"
        continue
    else:
        break
print is_pangram(in_str)
