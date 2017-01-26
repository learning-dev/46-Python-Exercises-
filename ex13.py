def max_in_list(passed_list):
    max_ele = -1000000
    for i in range(len( passed_list)):
        if int(passed_list[i]) > max_ele:
            max_ele = int(passed_list[i])
    return max_ele
int_list = []
in_str = raw_input(" Enter a list:")
in_list = in_str.split(' ')
print in_list
for x in in_list:
    int_list.append(int(x))
  #  print type(x)
print int_list  
print max_in_list(int_list)