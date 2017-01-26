# def histogram(pass_list):  # inbuilt function
#     for i in pass_list:
#         print int(i)*'*'
def histogram(pass_list):
    temp_str = ''
    for i in range(len(pass_list)):
        temp_str = ''
        for j in range(int(pass_list[i])):
            temp_str += '*'
        print temp_str


in_str = raw_input("enter a list:")
in_list = in_str.split(' ')
# print in_list
for n in in_list:
    n = int(n)
histogram(in_list)
