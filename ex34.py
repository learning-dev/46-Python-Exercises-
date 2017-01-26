# finding a freq of the words in file


def char_freq_table(list_str):
    out_list = []
    for i in range(len(list_str)):  # iterating for each word
        count = 0
        temp = list_str[i]
        for j in list_str:   # finding the word in list
            if j == temp:
                count += 1   # increasing the count
        freq = {temp :count}     # creating a dict with word: frequency manner
        out_list.append(freq)
    return out_list   # list of dictionaries


file_name = raw_input("Enter the file name :")
try:
    fh = open(file_name, 'r')  # opening the file
    str_ = fh.read()
    str_in = str_.split('\n')
    print str_in


except IOError as e:  # if file doesn't exists
    print "Sorry, file doesn't exists"
    raise e

ret_dict_list = char_freq_table(str_in)
for i in ret_dict_list:   # printing the list of words with dict
    print i

