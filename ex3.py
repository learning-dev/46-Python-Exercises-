def len_str(in_str):
    count = 0
    for i in in_str:
        count += 1
    return count

in_string = raw_input("Enter the string:")
print len_str(in_string)
print len(in_string)

