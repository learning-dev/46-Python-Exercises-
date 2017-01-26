def line_no(in_list):
    file_out = open("out_file.txt", 'w')
    n = 1
    for i in in_list:
        temp = str(n) + '.' + i
        file_out.write(temp)
        file_out.write('\n')
        n += 1
    file_out.close()


file_name = raw_input("Enter the file name :")
try:
    fh = open(file_name, 'r')  # opening the file
    str_ = fh.read()
    str_in = str_.split('\n')
    print str_in


except IOError as e:  # if file doesn't exists
    print "Sorry, file doesn't exists"
    raise e
line_no(str_in)
print "printing the files files from %s" % 'out_file.txt'

file_open = open('out_file.txt', 'r')
print file_open.read()
