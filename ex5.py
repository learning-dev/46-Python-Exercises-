"""
input: this is fun   program to convert the string into "robber's language"
output: tothohisos isos fofunon
"""


def swed_lang(in_str):
    v_list=['a', 'e', 'i', 'o', 'u']
    in_str=list(in_str)
    out_str=''
    for i in in_str:
        if i not in v_list:
            out_str=out_str+i+'o'+i
        else:
            out_str=out_str+i
    return out_str

in_string = raw_input("Enter a string to translate:")
print swed_lang(in_string.lower())

