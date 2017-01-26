def my_reduce(func, in_st):
    large = in_st[0]
    for i in range(1, len(in_st)):
        large = func(large, in_st[i])
    return large


def func(num1, num2):
    if int(num1) > int(num2):
        return num1
    else:
        return num2


while True:
    in_str = raw_input("Enter a string:")
    if in_str is not None:
        break
    else:
        print " Error: Invalid input "
        continue
in_str = in_str.split()
print my_reduce(func, in_str)
