def is_palindrome(input_str):
    output_str = ""
    for i in input_str:
        output_str = i + output_str
    if output_str == input_str:
        return True
    return False


str_in= raw_input("enter the string:")

print is_palindrome(str_in)
