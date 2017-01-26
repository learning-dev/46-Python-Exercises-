# To check if the word is a semordnilap for e.g. desserts is stressed. Different word when spelled reversed

def is_semordnilap(list_str):
    out_list = []
    for i in list_str:
        rev_str = i[::-1]
        if rev_str in list_str and rev_str != i:
            out_list.append(i + " " + rev_str)
    return out_list


file_name = raw_input("Enter the file name :")
try:
    fh = open(file_name, 'r')  # opening the file
    str_ = fh.read()
    str_in = str_.split('\n')
    print str_in


except IOError:  # if file doesn't exists
    print "Sorry, file doesn't exists"
    exit()

flag = is_semordnilap(str_in)
for i in flag:
    print i
