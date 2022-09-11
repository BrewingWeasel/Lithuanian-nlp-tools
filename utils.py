accented = 'ãúàáąìíĩũỹýòõóẽéèñù'
unaccented = 'auaaąiiiuyyoooeeenu'

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ą', 'č', 'ę', 'ė', 'į', 'š', 'ų', 'ū', 'ž', ',', ' ', '\n']

replace_dict = {
    'ė́': 'ė',
    'l̃': 'l',
    'õ': 'o',
    'ỹ': 'y',
    'ė̃': 'ė',
    'r̃': 'r',
    'm̃': 'm',
    'ū̃': 'ū',
    'ū́': 'ū',
    'ą̃': 'ą',
    'ù': 'u',
    'ę́': 'e',
    'į̃': 'į',
    'ą́': 'a',
    'ą́': 'a',
    'ę̃': 'ę',
    'ų́': 'ų'
}

def remove_accents(text):
    trans = text.maketrans(accented, unaccented)
    new_text = text.translate(trans)
    for i, o in replace_dict.items():
        new_text = new_text.replace(i, o)
    return new_text


def add_prefix(d, prefix):
    for k, v in d.items():
        if(isinstance(v, dict)):
            add_prefix(v, prefix)
        else:
            d[k] = prefix + v