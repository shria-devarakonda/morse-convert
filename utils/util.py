def check_out(out_,converted,type_morse):
    if "y" in out_:
        from datetime import datetime
        with open(f"file_from{type_morse}_{datetime.now().strftime('%H:%M:%S_%d:%m:%Y')}.txt","w+") as fi:
            fi.write(converted)
        print("File Updated")
    else:
        print(converted)

def check_in(in_file,val):
    if in_file:
        try:
            with open(f"{in_file}","r") as fi:
                strs = fi.readlines()
        except:
            raise Exception("File does not exist! Have you added the extension to the file name too? "
                            "Or checked the path?")
        return '\n'.join(strs)
    else:
        return val


def input_taker():
    type_morse_ = input(f"Type 'morse' if you wish to convert from morse to text\n"
                       "Type 'text' if you wish to convert text to morse.\n").lower()
    in_type = input("Would you require your input read from a file? 'y' for yes and 'n' for no\n").lower()
    val_ = None
    if "y" not in list(in_type):
        val_ = input("Enter your string to perform the operation on\n")
    out_type = input("Would you require your output in a file? 'y' for yes and 'n' for no\n").lower()
    in_file=None
    if "y" in list(in_type):
        in_file = input("Please provide filename of the file to read.").lower()
    return type_morse_, val_, out_type,in_type,in_file