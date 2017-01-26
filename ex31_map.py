def fucn(num):
    return num**2


def my_map(fucn,in_list):
    out_list = []
    for i in in_list:
        out_list.append(fucn(int(i)))
    return out_list


while True:
    in_list = raw_input("Enter a string:")
    if in_list is not None:
        break
    else:
        print " Error: Invalid input "
        continue
in_list = in_list.split( )
print my_map(fucn, in_list)

