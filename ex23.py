# 1) two or more occurrences of the space character is compressed into one, and 2) inserts an extra #space after a
# period if the period is directly followed by a letter. E.g. correct("This   is  very #funny  and    cool.Indeed!")
# should return "This is very funny and cool. Indeed!"




import re

def correct(in_str):
    regex = r"\s+"
    text = re.sub(regex,' ',in_str)
    reg = r"(\.)(\w)"
    text = re.sub(reg,r'\1 \2',text)
    # regex1 = r"\.\w+"
    # text = re
    # print '{}' .format(text)
    return text

while True:
        in_str = raw_input("Enter a string:")
        if in_str is None or in_str.isspace():
            print "Error: invalid input "
            continue
        else:
            break
print correct(in_str)