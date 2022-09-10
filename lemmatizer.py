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
        if isinstance(val, dict):
            nested = nested_vals(val, word)
            if(nested):
                return(list(d.keys())[i] + ' ' + nested)
        else:
            if(d[list(d.keys())[i]] == word):
                return(list(d.keys())[i])


def get_info(word, verbs):
    verb_list = [i.split(',')[0] for i in verbs]
    if(word in verb_list):
        return(word, 'infinitive')
    max_val = len(word)
    while(max_val >= 1):
        for i, verb in enumerate(verb_list):
            shared_root = find_shared_root(verb, word)
            if(len(shared_root) >= max_val):
                conjs = conjugate(*verbs[i].split(', '))
                conj_type = nested_vals(conjs, word)
                if(conj_type):
                    return(verb, conj_type)
        max_val -= 1

#Get all of the verbs
with open('data.txt', 'r', encoding='utf-8') as f:
    verbs = f.read().split('\n')


def get_lemma(word):
    return get_info(word, verbs)[0]

def get_morph(word):
    return get_info(word, verbs)[1]