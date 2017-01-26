def longest_word(passed_list):
    long_str = ''
    max_len = -10000
    for i in passed_list:
        if len(i) > max_len:
            long_str = i
            max_len = len(i)
    return long_str


in_str = raw_input("enter a list of words:")
in_list = in_str.split(' ')
print longest_word(in_list)
