# ENCRYPITION
from random import choice
import pandas as pd

chars = "({[/:<-*&^%`|_~$#@!+>;\]})"
a, b = list(chars[:(len(chars)//2)]), list(chars[len(chars)//2:])
inp_message, result_encoded = input("Enter the message: "), ""
for i in inp_message:
    encry = ''.join([choice(a) if z=="x" else z for z in list(hex(ord(i)))[::-1]])
    result_encoded += choice(b)+choice(b)+encry+choice(b)

########################################################################################
# DECRYPITION
message, result_decode = result_encoded[2:], []
for i in range(0,len(message),7):
    if i+4 > len(message):
        break
    else: result_decode.append(str(message[i:i+4]))
for i in result_decode:
    x = list(i)
    for q in range(len(x)):
        for j in a:
            if x[q] == j:
                x[q]="x"
    result_decode[result_decode.index(i)]="".join(x)

val_dic = {'13x0': '1', '23x0': '2', '33x0': '3', '43x0': '4', '53x0': '5', '63x0': '6', '73x0': '7',
           '83x0': '8', '93x0': '9', '03x0': '0', '14x0': 'A', '24x0': 'B', '34x0': 'C', '44x0': 'D',
           '54x0': 'E', '64x0': 'F', '74x0': 'G', '84x0': 'H', '94x0': 'I', 'a4x0': 'J', 'b4x0': 'K',
           'c4x0': 'L', 'd4x0': 'M', 'e4x0': 'N', 'f4x0': 'O', '05x0': 'P', '15x0': 'Q', '25x0': 'R',
           '35x0': 'S', '45x0': 'T', '55x0': 'U', '65x0': 'V', '75x0': 'W', '85x0': 'X', '95x0': 'Y',
           'a5x0': 'Z', '16x0': 'a', '26x0': 'b', '36x0': 'c', '46x0': 'd', '56x0': 'e', '66x0': 'f',
           '76x0': 'g', '86x0': 'h', '96x0': 'i', 'a6x0': 'j', 'b6x0': 'k', 'c6x0': 'l', 'd6x0': 'm',
           'e6x0': 'n', 'f6x0': 'o', '07x0': 'p', '17x0': 'q', '27x0': 'r', '37x0': 's', '47x0': 't',
           '57x0': 'u', '67x0': 'v', '77x0': 'w', '87x0': 'x', '97x0': 'y', 'a7x0': 'z', '02x0': ' ',
           '12x0': '!', '32x0': '#', '04x0': '@', "42x0": '$', '52x0': '%', 'e5x0': '^', '62x0': '&',
           'a2x0': '*', '82x0': '(', '92x0': ')', 'f5x0': '_', 'd2x0': '-', 'b2x0': '+', 'd3x0': '=',
           'f2x0': '/', 'c2x0': ',', 'e2x0': '.', '06x0': '`', 'e7x0': '~', 'f3x0': '?', 'b3x0': ';',
           'a3x0': ';', 'c3x0': '<', 'e3x0': '>', 'b7x0': '{', 'd7x0': '}', 'b5x0': '[', 'd5x0': ']',
           '72x0': "'", '22x0': '"'}

end_res = "".join([str(i) for i in list(pd.Series(result_decode).map(val_dic))])

print('\n'+'-'*50,'\n')
print(result_encoded, end_res, sep='\n\n')
