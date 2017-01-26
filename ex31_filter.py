# filter Implementation


len_limit = raw_input("Enter a limit:")

def func(in_c):
      return len(in_c) > int(len_limit)



def my_filter(func, in_str):
    out_list = []
    for i in in_str:
        if func(i):
            out_list.append(i)
    return out_list


while True:
    in_str = raw_input("Enter a string:")
    if in_str is not None and int(len_limit):
        break
    else:
        print " Error: Invalid input "
        continue
in_str = in_str.split( )
print my_filter(func, in_str)
