from conjugator import conjugate

with open('data\\verb_prefixes.txt', 'r', encoding='utf-8') as f:
    PREFIXES = f.read().split('\n') + ['ne', 'be']

with open('data\\allconjs.txt', 'r', encoding='utf-8') as f:
    CONJS = {i.split(', ')[0]: i.split(', ')[1] for i in f.read().split('\n')}

with open('data\\data.txt', 'r', encoding='utf-8') as f:
    VERBS = f.read().split('\n')


def nested_vals(d, word):
    for i, val in enumerate(d.values()):
        cur_key = list(d.keys())[i]
        if isinstance(val, dict):
            nested = nested_vals(val, word)
            if(nested):
                return(cur_key + ' ' + nested)
        else:
            is_word = d[cur_key] == word
            if('(' in d[cur_key] and not is_word):
                is_word = d[cur_key].replace('(', '').replace(')', '') == word
            if('(' in d[cur_key] and not is_word):
                removed_parens = d[cur_key].split('(')[0] + d[cur_key].split('(')[1].split(')')[1]
                is_word = removed_parens == word
            if(is_word):
                return(cur_key)


def main_prefix_removal(verb, unprefixed_verb):
    if(verb == unprefixed_verb):
        return(verb)
    for i in PREFIXES:
        if(verb.startswith(i)):
            if(verb[len(i):] == unprefixed_verb):
                return(verb[len(i):])
            else:
                verb_found = main_prefix_removal(verb[len(i):], unprefixed_verb)
                if(verb_found):
                    return(verb_found)


def get_prefix(word, unlemmatized):
    root = main_prefix_removal(word, unlemmatized)
    try:
        return(word.replace(root, ''))
    except TypeError:
        return('')

def get_info(word):
    for unlemmatized, lemma in CONJS.items():
        if(word.endswith(unlemmatized)):
            prefix = get_prefix(word, unlemmatized)
            if(prefix != ''):
                word = word.strip(prefix)
                return [prefix + lemma, conjugate(prefix + lemma)]


def get_lemma(word):
    return get_info(word)[0]

def get_morph(word):
    return get_info(word)[1]