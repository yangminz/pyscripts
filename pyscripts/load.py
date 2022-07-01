import re

def add_subtree_dic(keys, value, dic):
    d = dic
    lastkey = ""
    lastdic = {}
    for key in keys:
        lastdic = d
        lastkey = key
        if key in d:
            # key existing
            d = d[key]
        else:
            # add new key
            d[key] = {}
            d = d[key]
    lastdic[lastkey] = value
    return dic

def add_dic_items_from_kventry(entry, dic):
    assert(isinstance(entry, str))
    # parse lines to keys and values
    result = re.search(r"(?P<keys>([\w\-]+\.)+[\w\-]+)\s*=\s*(?P<value>[\w\-]+)", entry)
    if result == None:
        return dic
    keys = result.group("keys").split(".")
    value = result.group("value")
    # add to dictionary
    return add_subtree_dic(keys, value, dic)

def get_dic_from_kvlines(content_lines):
    dic = {}
    for line in content_lines:
        dic = add_dic_items_from_kventry(line, dic)
    return dic

'''
load file as dictionary:
key1.key2.key3.key4 = value
'''
def load_dictionary_kvtree(filepath):
    with open(filepath, "r", encoding="utf-8") as fr:
        return get_dic_from_kvlines(fr.readlines())