def len_trim_word(passed_list, n):
    num_list = []
    for i in passed_list:
        if i not in [None, ''] and len(i) > n:
            num_list.append(i)
    return num_list

in_str = raw_input("enter a list of words:")
in_list = in_str.split(' ')
num = raw_input("enter the exceeding limit:")
print len_trim_word(in_list, int(num))