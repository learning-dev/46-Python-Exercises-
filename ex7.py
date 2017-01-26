"""reversing the string in many ways 1. using inbuit function reversed
                                      2. using slicing method [::-1]
                                      3. using custom built function"""
def rev_str(input_str):
    out_str=''
    i = len(input_str)-1
    while i >= 0:
        out_str = out_str+ str(input_str[i])
        i-=1
    return  out_str

str_in= raw_input("enter the string:")

print rev_str(str_in)

