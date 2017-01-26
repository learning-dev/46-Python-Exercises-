def word_to_list(passed_list):
    num_list = []
    for i in passed_list:
        num_list.append(len(i))
    return num_list

in_str = raw_input("enter a list of words:")
in_list = in_str.split(' ')
print word_to_list(in_list)