# Write a function find_longest_word() that takes a list of words and returns the length of the longest one. Use only higher order functions.


def find_longest_word(in_list):
    return reduce(lambda x, y: x if (x > y) else y, [len(x) for x in in_list])


while True:
    in_str = raw_input("Enter a string:")
    if in_str is not None:
        break
    else:
        print " Error: Invalid input "
        continue

in_list_words = in_str.split()
print in_list_words
print find_longest_word(in_list_words)
