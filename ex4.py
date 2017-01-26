def if_vowel(in_char):
    v_list=['a', 'e', 'i', 'o', 'u']
    if in_char in v_list:
        return True
    else:
        return False


in_str = raw_input("Enter a character:")
print if_vowel(in_str)
#     print
# else:
#     print "False"
