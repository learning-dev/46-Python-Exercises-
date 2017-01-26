"""a program without "in" operator """

def is_member(in_list, element):
    x = len(in_list)
    flag = False
    for i in range(x):
        if i == element:
            flag = True
    return flag

in_str = raw_input("enter a list :")
in_list = in_str.split(' ')
print in_list
ele = raw_input("Enter an element:")
for i in range(len(in_list)):
    i = int(i)
print is_member(in_list, int(ele))

