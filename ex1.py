def max(num1, num2):     # function to get the max number
    if num1 > num2:         # checking for the max
        return num1
    else:
        return num2


numbers = raw_input("Enter two numbers:")
in_list = numbers.split(',')        # splitting the input in a list 
print max(int(in_list[0]),int(in_list[1]))

