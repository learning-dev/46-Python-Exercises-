# sentence splitter
import  re
regex = r"(?<!Mr)(?<!Mrs)(?<!Dr)(\.\s)([A-Z])"
def sentence_file(file_str):
    out_file = open('output.txt','w')
    out_str = re.sub(regex, r'.\n\1',file_str)
    out_str = re.sub(r'\!\s',r'!\n',out_str)
    out_str = re.sub(r'\?\s', r'\n\?', out_str)
    out_file.write(out_str)
    out_file.close()


file_name = raw_input("Enter the file name :")
try:
    fh = open(file_name, 'r')  # opening the file
    str_ = fh.read()
    print str_

except IOError as e:
    # if file doesn't exists
    print "Sorry, file doesn't exists"
    raise e

sentence_file(str_)