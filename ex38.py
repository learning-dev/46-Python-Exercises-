def avg_word_length(word_list):
    sum = 0
    no_of_words = 0
    averg = 0
    for i in word_list:
        sum += len(i)
        no_of_words += 1
    averg = sum / no_of_words
    print  "sum: ", sum
    return averg


file_name = raw_input("Enter the file name :")
try:
    fh = open(file_name, 'r')  # opening the file
    str_ = fh.read()
    str_in = str_.split( )
    print str_in
    print "len of whole:", len(str_in)


except IOError as e:  # if file doesn't exists
    print "Sorry, file doesn't exists"
    raise e
print  "avg:", avg_word_length(str_in)