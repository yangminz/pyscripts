import re

def find_value_by_key_from_text_lines(filename, searchkey):
    # KEY:: key
    # value
    result = []
    with open(filename, "r", encoding="utf-8") as fr:
        content = fr.read()
        key_matches = re.finditer(r"(?<=\nKEY::)\s*(?P<key1>[^\n]+)(?=\n)|^KEY::\s*(?P<key2>[^\n]+)(?=\n)", content)
        for match in key_matches:
            key = "".join([x if x != None else "" for x in [match.group("key1"), match.group("key2")]])
            if searchkey.lower() in key.lower():
                valStartIndex = match.span()[1]
                valueSpan = re.search(r".*(?=KEY::)", content[valStartIndex + 1:]).span()
                value = content[valStartIndex + 1 : valueSpan[1] + valStartIndex + 1].rstrip("\n")
                result += [(key, value)]
    return result