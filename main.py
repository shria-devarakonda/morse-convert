import json
from utils.util import input_taker, check_in, check_out

class Morse:
    f = open("morse-code.json")
    morse_dict = json.load(f)
    f.close()
    def __init__(self, type_morse, val):
        self.val = val
        self.type_morse = type_morse

    def converter(self):
        if self.type_morse == "morse":
            return self.convert(self.val,type_morse="morse")
        elif self.type_morse == "text":
            return self.convert(self.val, type_morse="text")
        else:
            raise Exception("please give input as 'morse' or 'text' for the needed conversion.")

    def convert(self, val, type_morse):
        if type_morse== "text":
            val = list(val)
            for i in range(len(val)):
                if val[i] in Morse.morse_dict.keys():
                    val[i]= Morse.morse_dict[val[i]]
                else:
                    val[i]=" "
            return ' '.join(val)
        else:
            val = val.strip(' ').split(' ')
            key_list = list(Morse.morse_dict.keys())
            val_list = list(Morse.morse_dict.values())
            for i in range(len(val)):
                if val[i] in val_list:
                    pos = val_list.index(val[i])
                    val[i] = key_list[pos]
                else:
                    val[i] = " "
            val = ''.join(val)
            return ' '.join(val.split())


type_morse, val, out_type, in_type, in_file = input_taker()
lines = check_in(in_file,val)
morse_made = Morse(type_morse, lines)
converted = morse_made.converter()
check_out(out_type, converted, type_morse)
