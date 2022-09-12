from conjugator import conjugate

with open('verb_prefixes.txt', 'r', encoding='utf-8') as f:
    PREFIXES = f.read().split('\n') + ['ne', 'be']

with open('allconjs.txt', 'r', encoding='utf-8') as f:
    CONJS = f.read().split('\n')

with open('data.txt', 'r', encoding='utf-8') as f:
    VERBS = f.read().split('\n')

def find_shared_root(word, verb):
    char_num = len(word)
    try:
        for i in range(1, len(word)):
            char_num = i
            if(word[:-i] in verb.strip('ti')):
                break
    except IndexError:
        return('')
    return(word[:-char_num])

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


def main_prefix_removal(verb):
    if(verb in CONJS):
        return(verb)
    for i in PREFIXES:
        if(verb.startswith(i)):
            if(verb[len(i):] in CONJS):
                return(verb[len(i):])
            else:
                verb_found = main_prefix_removal(verb[len(i):])
                if(verb_found):
                    return(verb_found)
    return(verb)


def get_prefix(word):
    root = main_prefix_removal(word)
    return(word.replace(root, ''))

def get_info(word, verbs):
    verb_list = [i.split(',')[0] for i in verbs]
    if(word in verb_list):
        return(word, 'infinitive')
    max_val = len(word)
    prefix = get_prefix(word)
    word = word.strip(prefix)
    while(max_val >= 1):
        for i, verb in enumerate(verb_list):
            shared_root = find_shared_root(verb, word)
            if(len(shared_root) >= max_val):
                conjs = conjugate(prefix + verb)
                conj_type = nested_vals(conjs, prefix + word)
                if(conj_type):
                    return(prefix + verb, conj_type)
                #Try reflexive version if the normal version didn't work
                if('s' in word):
                    conjs = conjugate(prefix + verb + 's')
                    conj_type = nested_vals(conjs, prefix + word)
                    if(conj_type):
                        return(prefix + verb + 's', conj_type)
        max_val -= 1




def get_lemma(word):
    return get_info(word, VERBS)[0]

def get_morph(word):
    return get_info(word, VERBS)[1]