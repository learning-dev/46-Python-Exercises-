def large_of_three(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    else:
        if num2 > num3:
            return num2
        else:
            return num3

numbers = raw_input("Enter three numbers:")
in_list = numbers.split(',')
print in_list
# for i in in_list:
#     i = int(i)
#     print type(i)
#
print large_of_three(int(in_list[0]), int(in_list[1]), int(in_list[2]))


