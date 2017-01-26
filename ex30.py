def translate(list_words, dict_):
    return map(dict_map(dict_), list_words)


def dict_map(dict_in):
    print dict_in
    def cb(i):
        print dict_in
        if i in dict_in.keys():
            print dict_in[i]
        else:
            print "no-key"

    return cb


while True:
    in_str = raw_input("Enter a string:")
    if in_str is not None:
        break
    else:
        print " Error: Invalid input "
        continue

list_dict = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}

in_list_words = in_str.split()
print in_list_words

print translate(in_list_words, list_dict)
