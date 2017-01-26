""" Program to check overlapping of list  without using two loops as told in the exercise """


def overlapping(first, second):
    for x in range(len(first)):
        for y in range(len(second)):
            if first[x] == second[y]:
                return True
    return False



#  first_list = [1, 4, 5] # false condition

first_list = [1, 2, 4, 5]
second_list = [2, 6, 7]
print overlapping(first_list, second_list)
