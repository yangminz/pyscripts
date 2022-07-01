import math

def get_hex_table_from_ascii_string(ascii_str):
    length = len(ascii_str)
    print(repr(ascii_str))
    table = [["Offset", "Hex", "ASCII"]]
    for i in range(math.ceil(length/8)):
        line = ["[" + str(i * 8) + "]"]
        number = ""
        for j in range(8):
            index = j + i * 8
            if index < len(ascii_str):
                number = str(hex(ord(ascii_str[index])))[2:] + number
            else:
                number = "00" + number
        line += [number]
        line += [repr(ascii_str[i * 8: i * 8 + 8][::-1])]
        line[-1] = line[-1][1:-2]
        table += [line]
    return table