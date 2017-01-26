import re


def rev_check(str_check):  # function to check if a sentence is palindrome
    if str_check == '':
        return False
    rev_str = ''
    j = len(str_check) - 1
    while j >= 0:  # reverse a string
        rev_str += str_check[j]
        j -= 1
    return rev_str == str_check


def palin_check(file_handle):  # takes the list of sentences
    out_str = ''
    list_palindrome = []
    regex = r"\w+"  # regex for finding non-space characters
    for i in file_handle:  # runs for every sentence in file
        # print i
        temp = re.findall(regex, i.strip())
        out_str = ''.join(temp)  # joining all the non space characters
        if rev_check(out_str.lower()):  # check if the sentence without spaces is palindrome
            if i != '':
                list_palindrome.append(i)
    return list_palindrome


file_name = raw_input("Enter the file name :")
try:
    fh = open(file_name, 'r')  # opening the file
    str_ = fh.read()
    list_str = str_.split('\n')
    # print list_str


except IOError:  # if file doesn't exists
    print "Sorry, file doesn't exists"
    exit()

check = palin_check(list_str)  # calling the function
if check == []:
    print "Palindrome not found in file"
else:
    print "Palindrome found"
    for k in check:
        print k
        # print str_.lower()
