from utils import add_prefix


present_conj_data = [
    ['u', 'i', 'a', 'ame', 'ate'],
    ['iu', 'i', 'i', 'ime', 'ite'],
    ['au', 'ai', 'o', 'ome', 'ote']
]

past_conj_data = [
    ['au', 'ai', 'o', 'ome', 'ote'],
    ['iau', 'ei', 'ė', 'ėme', 'ėte']
]

reflexive_endings = ['i', 'i', 'i', '', '']

future_conj_data = ['iu', 'i', '', 'ime', 'ite']

conditional_conj_data = ['čiau', 'tum(ei)', 'tų', 'tu(mė)me', 'tu(mė)te']

meanings = ['first person singular', 'second person singular', 'third person', 'first person plural', 'second person plural']

with open('data.txt', 'r', encoding='utf-8') as f:
    verbs = f.read().split('\n')
    verbs = [i.split(',')[0] for i in verbs]

with open('verb_prefixes.txt', 'r', encoding='utf-8') as f:
    PREFIXES = f.read().split('\n')

def get_shared_chars(str1, str2):
    max_char = 0
    for i, char in enumerate(str1):
        max_char = i
        try:
            if(char != str2[i] and not ((char == 'u' and str2[i] == 'ū') or (char == 'i' and str2[i] == 'y'))):
                break   
        except IndexError:
            break     

    return(str1[:max_char])


def get_reflexive(conj, i):
    if(conj.endswith('e')):
        conj = conj[:-1] + 'ė'
    return conj + 's' + reflexive_endings[i]

def main_prefix_removal(verb):
    for i in PREFIXES:
        if(verb.startswith(i)):
            if(verb[len(i):] in verbs):
                return(verb[len(i):])
            else:
                verb_found = main_prefix_removal(verb[len(i):])
                if(verb_found):
                    return(verb_found)


def remove_prefixes(verb):
    if(verb.startswith('ne')):
        verb = verb[2:]
    if(verb.startswith('be')):
        verb = verb[2:]
    return main_prefix_removal(verb)


def conjugate_present(third_pres, reflexive=False):
    conj_present = {}
    #Get present tense conjugation for the verb
    for cj in present_conj_data:
        if(third_pres.endswith(cj[2])):
            stem = third_pres[:-1]
            for i, form in enumerate(cj):
                conj = ''
                if(stem.endswith('d') and i == 0):
                    conj = stem[:-1] + 'dž' + form
                else:
                    #If the final letter of the stem is already the letter for the conjugation, ignore it            
                    if(form != stem[-1]):
                        conj = stem + form
                    else:
                        conj = stem
                if(reflexive):
                    if(cj[2] == 'a'):
                        if(i == 0):
                            conj += 'osi'
                        elif(i == 1):
                            conj += 'esi'
                        else:
                            conj = get_reflexive(conj, i)
                    else:
                        conj = get_reflexive(conj, i)
                conj_present[meanings[i]] = conj
    
    return(conj_present)


def conjugate_imperative(stem, reflexive=False):
    imperative_stem = stem
    if(stem.endswith('g') or stem.endswith('k')):
        imperative_stem = stem[:-1]
    if(reflexive):
        return{
        'second person singular': imperative_stem + 'ks',
        'second person plural': imperative_stem + 'kitės',
        'first person plural': imperative_stem + 'kimės'
    }

    return{
        'second person singular': imperative_stem + 'k',
        'second person plural': imperative_stem + 'kite',
        'first person plural': imperative_stem + 'kime'
    }


def conjugate_past(third_past, reflexive=False):
    #Get past tense conjugation for the verb
    conj_past = {}
    for cj in past_conj_data:        
        if(third_past.endswith(cj[2])):
            stem = third_past[:-1]
            conj = ''
            for i, form in enumerate(cj):
                #Palatalize verb if necessary                
                if(i == 0 and cj[2] == 'ė' and (stem[-1] == 'd' or stem[-1] == 't')):
                    if(stem[-1] == 't'):
                        conj = stem[:-1] + 'č' + form
                    else:
                        conj = stem[:-1] + 'dž' + form
                else:
                    conj = stem + form
                    if(reflexive):
                        conj = get_reflexive(conj, i)
                    conj_past[meanings[i]] = conj
        
    return(conj_past)


def conjugate_past_iterative(stem, reflexive=False):
    iterative_data = {}
    for i, cj in enumerate(past_conj_data[0]):
        conj = stem + 'dav' + cj
        if(reflexive):
            conj = get_reflexive(conj, i)
        iterative_data[meanings[i]] = conj
    return iterative_data

def conjugate_future(stem, third_past, third_pres, reflexive=False):
    future_data = {}
    future_stem = stem
    if(not stem.endswith('s')):
        if(stem.endswith('š') or stem.endswith('ž')):
            future_stem += 'š'
        else:
            future_stem += 's'
    for i, cj in enumerate(future_conj_data):
        if(i == 2):
            beginning = get_shared_chars(get_shared_chars(third_past, third_pres), stem)
            conj = beginning + future_stem[len(beginning):]
            if(reflexive):
                conj += 'is'
            future_data['third person'] = conj
        else:
            conj = future_stem + cj
            if(reflexive):
                conj = get_reflexive(conj, i)
            future_data[meanings[i]] = conj
    return(future_data)

def conjugate_conditional(stem, reflexive=False):
    conditional_data = {}
    for i, form in enumerate(conditional_conj_data):
        conj = stem + form
        if(reflexive):
            if(i == 1):
                conj = stem + 'tumeisi'
            else:
                conj = get_reflexive(conj, i)
        conditional_data[meanings[i]] = conj

    return(conditional_data)

def conjugate(infinitive, third_pres='', third_past=''):
    reflexive = infinitive.endswith('s')
    if(reflexive):
        infinitive = infinitive[:-1]
    prefix = ''
    if(infinitive not in verbs):
        root_verb = remove_prefixes(infinitive)
        prefix = infinitive.split(root_verb)[0]
        infinitive = root_verb
    if(not third_past or not third_pres):
        with open('data.txt', 'r', encoding='utf-8') as f:
            for verb in f.read().split('\n'):
                verb_info = verb.split(', ')
                if(verb_info[0] == infinitive):
                    third_pres = verb_info[1]
                    third_past = verb_info[2]

    data = {}    
    stem = infinitive[:-2]    
    data['present'] = conjugate_present(third_pres, reflexive)    
    data['imperative'] = conjugate_imperative(stem, reflexive)    
    data['past'] = conjugate_past(third_past, reflexive)
    data['past iterative'] = conjugate_past_iterative(stem, reflexive)
    data['future'] = conjugate_future(stem, third_past, third_pres, reflexive)
    data['conditional'] = conjugate_conditional(stem, reflexive)

    if(data):
        add_prefix(data, prefix)

    return(data)
