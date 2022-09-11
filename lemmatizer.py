from conjugator import conjugate

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


def get_info(word, verbs):
    verb_list = [i.split(',')[0] for i in verbs]
    if(word in verb_list):
        return(word, 'infinitive')
    max_val = len(word)
    while(max_val >= 1):
        for i, verb in enumerate(verb_list):
            shared_root = find_shared_root(verb, word)
            if(len(shared_root) >= max_val):
                try_verb = verbs[i].split(', ')[0]
                conjs = conjugate(verb)
                conj_type = nested_vals(conjs, word)
                if(conj_type):
                    return(verb, conj_type)
                #Try reflexive version if the normal version didn't work
                if('s' in word):
                    conjs = conjugate(verb + 's')
                    conj_type = nested_vals(conjs, word)
                    if(conj_type):
                        return(verb + 's', conj_type)
        max_val -= 1

#Get all of the verbs
with open('data.txt', 'r', encoding='utf-8') as f:
    verbs = f.read().split('\n')


def get_lemma(word):
    return get_info(word, verbs)[0]

def get_morph(word):
    return get_info(word, verbs)[1]