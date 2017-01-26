"""
If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
If the verb ends in ie, change ie to y and add ing
For words consisting of consonant-vowel-consonant, double the final letter before adding ing
By default just add ing
"""


def make_ing_form(in_str):
    out_string = ''
    if in_str.endswith('ie'):
        out_string = in_str[:len(in_str) - 2]
        return out_string + 'ying'
    elif in_str.endswith('e'):
        out_string = in_str[:len(in_str) - 1]
        return out_string + 'ing'

    elif len(in_str) > 3:
        if in_str[0] not in ['a', 'e', 'i', 'o', 'u'] and in_str[1] in ['a', 'e', 'i', 'o', 'u']:
            if in_str[2] not in ['a', 'e', 'i', 'o', 'u']:
                out_string = in_str[:len(in_str)]
        return out_string +in_str[len(in_str)-1] + 'ing'
    else:
        return in_str + 'ing'

while True:
        in_str = raw_input("Enter a string:")
        if in_str is None or in_str.isspace():
            print "Error: invalid input "
            continue
        else:
            break
print make_ing_form(in_str)
#print in_str[:len(in_str)-2]