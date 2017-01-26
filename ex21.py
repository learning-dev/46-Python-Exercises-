""" Program to check a frequency of charcters in input"""

def char_freq(in_str):
    out_dict = {}
    count = 0
    in_str = list(in_str)
    n = len(in_str)
    for j in range(n):
        temp = in_str[j]
        count = 0
        for i in in_str:
            if temp is i:
                count += 1
        out_dict[temp] = count
    return out_dict

while True:
    in_str = raw_input("Enter a string:")
    if in_str is None:
        print "Error: Invalid input!"
        continue
    else:
        break
print char_freq(in_str)

