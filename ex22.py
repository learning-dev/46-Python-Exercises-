"""Caeser Cipher text program : decoding and encoding using ROT - 13 e.g.  'a' is 'n', 'b' is 'o' and so on """
key_dict = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}


def caeser_cipher(in_str):
    flag = raw_input("what do you want to do? Decode (D) or Encode (E):")
    while True:
        if flag is None:
            print "Error: Invalid input!"
            continue
        else:
            print type(flag)
            break
    if flag.lower() == 'e':
        return cipher_encode(in_str)
    elif flag.lower() == 'd':
        return cipher_encode(in_str)
    else:
        print "invalid operation"


def cipher_encode(in_str):
    enc_str = ''
    for i in in_str:
        if i.isalpha():
            enc_str += key_dict[i]
        else:
            enc_str += i

    return enc_str


# def cipher_decode(in_str):
#     dec_str = ''
#     for i in in_str:
#         dec_str += key_dict[i]
#     return dec_str


while True:
    in_str = raw_input("Enter a string:")
    if in_str is None or in_str.isspace():
        print "Error: invalid input "
        continue
    else:
        break
print caeser_cipher(in_str)
