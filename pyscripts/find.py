import re

def find_value_by_key_from_text_lines(filename, searchkey):
    result = []
    with open(filename, "r", encoding="utf-8") as fr:
        content = fr.read()
        keylines = re.finditer(r"(?<=\n\n)[^\n]+(?=\n)|^[^\n]+(?=\n)", content)
        for match in keylines:
            keyline = match.group()
            if searchkey.lower() in keyline.lower():
                # key found here
                # match to next '\n\n' as end of value
                key = match.group()
                valStartIndex = match.span()[1]
                valueSpan = re.search(r".*(?=\n\n)", content[valStartIndex + 1:]).span()
                value = content[valStartIndex + 1 : valueSpan[1] + valStartIndex + 1]
                result += [(key, value)]
    return result