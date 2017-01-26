""" program takes strings and ignores special characters (including spaces) to compare palindrome strings
Implemented using regular expressions"""
import  re

def is_palindrome(input_str):
    out_str=''
    i = len(input_str)-1
    while i >= 0:
        out_str += str(input_str[i])
        i -= 1
    if out_str == input_str:
        print out_str
        return True
    else:
        print out_str
        return False

str_in= raw_input("enter the string:")
in_string =''.join(e for e in str_in if e.isalnum())
print in_string
in_re = r"\w+"
re_result =re.findall(in_re, str_in)
print "%s" %re_result
test_str = ''.join(re_result)
print test_str
# for match in re_result:
#     print "%s" %match

print is_palindrome(test_str.lower())