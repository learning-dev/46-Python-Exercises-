# Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.


def filter_long_words(list_words, len_limit):
    return filter(lambda x: len(x) > len_limit, list_words)



while True:
    in_str = raw_input("Enter a string:")
    len_check = raw_input("Enter the limit:")
    if in_str is not None and int(len_check):
        break
    else:
        print " Error: Invalid input "
        continue

in_list_words = in_str.split()
print in_list_words
print filter_long_words(in_list_words, int(len_check))

