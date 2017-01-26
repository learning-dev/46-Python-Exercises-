# high order functions
# Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well call the reduce() function directly?

from functools import reduce


def max_in_list(in_list):
    max_ele = reduce(mass, in_list)
    return max_ele


def mass(x, y):
    return max(x, y)


print max_in_list([5, 9, 67, 2, 1])
