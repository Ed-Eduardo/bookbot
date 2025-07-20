def get_num_words(string):
    return len(string.split())

def get_num_chars(string):
    chars = dict()
    for char in string.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_key(items):
    return (items["num"])

def sort_char(dict):
    list = []
    for char in dict:
        sub_dict = {}
        sub_dict["char"] = char
        sub_dict["num"] = dict[char]
        list.append(sub_dict)
    list.sort(reverse=True, key=sort_key)
    return list
