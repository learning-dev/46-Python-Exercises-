def sum(num_list):
    if num_list is []:
        return -1
    add=0
    for i in num_list:
        add += i
    return add
def multiply(num_list):
    if num_list is []:
        return -1
    mul_all=1
    for i in num_list:
        mul_all *= i
    return  mul_all

in_list = [1, 0,-1]

print sum(in_list)
print multiply(in_list)
