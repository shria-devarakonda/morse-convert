import json

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
            return ''.join(val)



def input_taker():
    type_morse_ = input(f"Type 'morse' if you wish to convert from morse to text\n"
                       "Type 'text' if you wish to convert text to morse.\n").lower()
    val_ = input("Enter your string to perform the operation on\n")
    return type_morse_, val_

type_morse, val = input_taker()
morse_made = Morse(type_morse, val)
converted = morse_made.converter()
print(converted)