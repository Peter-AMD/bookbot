def count_words(str):
    return len(str.split())


def count_char_instances(str):
    chars_dict = {}

    for char in str:
        lowered = char.lower()

        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1

    return chars_dict

# def sort_dict(str_dict):
#   return dict(sorted(str_dict.items(), key=lambda x:x[1], reverse=True))


def sort_dict(str_dict):
    str_list = []

    for key in str_dict:
        str_list.append({
            "char": key,
            "num": str_dict[key]
        })
    str_list.sort(reverse=True, key=lambda x:x["num"])
    return str_list
