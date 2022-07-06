import math

def get_hex_table_from_ascii_string(ascii_str):
    length = len(ascii_str)
    print(repr(ascii_str))
    table = [["Offset", "Hex"]]
    for i in range(math.ceil(length/8)):
        number = ""
        for j in range(8):
            index = j + i * 8
            if index < len(ascii_str):
                ch = str(hex(ord(ascii_str[index])))[2:]
                number = "0" * (2 - len(ch)) + ch + number
            else:
                number = "00" + number
        astr = "".join([repr(c)[1:-1] if len(repr(c)) == 4 else " " + c for c in ascii_str[i * 8: i * 8 + 8][::-1]])
        astr = " " * (len(number) - len(astr)) + astr
        table += [["[" + str(i * 8) + "]", number], ["", astr]]
    return table