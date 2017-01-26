
def make_3sg_form(in_str):
    out_string =''
    if in_str.endswith('y'):
        out_string = in_str[:len(in_str)-1]
        return out_string + 'ies'
    elif in_str.endswith('o') or in_str.endswith('ch') or in_str.endswith('s') or in_str.endswith('sh') or in_str.endswith('x') or in_str.endswith('es'):
        out_string = in_str[:len(in_str)]
        return out_string + 'es'
    else:
        out_string = in_str[:len(in_str)]
        return  out_string + 's'
while True:
    in_str = raw_input("Enter a string:")
    if in_str is None or in_str.isspace():
        print "Error: invalid input "
        continue
    else:
        break
print make_3sg_form(in_str)
