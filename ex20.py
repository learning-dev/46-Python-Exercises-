"""program to create dict of swedish words and translate input  using the dict """

def translate(in_str):
    out_list = []
    comp_dict = {"merry":"god",
                 "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
    for i in in_str:
        if i in comp_dict.keys():
            out_list.append(comp_dict[i])
        else:
            out_list.append('No value')
    return out_list


while True:
    in_str = raw_input("Enter a string:")
    if in_str is None or in_str.isspace():
        print "Error: invalid input "
        continue
    else:
        break
in_str = list(in_str.split( ))
print  in_str
print translate(in_str)




