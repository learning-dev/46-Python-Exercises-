some_str = 'tiger'

user_input = raw_input('Enter a string: ')

input_as_list = list(user_input)

for index, value in enumerate(input_as_list):
    if value in some_str:
        if index == some_str.find(value):
            input_as_list[index] = '[' + value + ']'
        else:
            input_as_list[index] = '(' + value + ')'
    else:
        pass

print ''.join(input_as_list)
