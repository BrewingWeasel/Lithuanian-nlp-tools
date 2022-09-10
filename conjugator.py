present_conj_data = [
    ['u', 'i', 'a', 'ame', 'ate'],
    ['iu', 'i', 'i', 'ime', 'ite'],
    ['au', 'ai', 'o', 'ome', 'ote']
]

past_conj_data = [
    ['au', 'ai', 'o', 'ome', 'ote'],
    ['iau', 'ei', 'ė', 'ėme', 'ėte']
]

future_conj_data = ['iu', 'i', '', 'ime', 'ite']

conditional_conj_data = ['čiau', 'tum(ei)', 'tų', 'tu(mė)me', 'tu(mė)te']

meanings = ['first person singular', 'second person singular', 'third person', 'first person plural', 'second person plural']


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



def conjugate_present(third_pres):
    conj_present = {}
    #Get present tense conjugation for the verb
    for cj in present_conj_data:
        if(third_pres.endswith(cj[2])):
            stem = third_pres[:-1]
            for i, form in enumerate(cj):
                if(stem.endswith('d') and i == 0):
                    conj_present[meanings[i]] = stem[:-1] + 'dž' + form
                else:
                    #If the final letter of the stem is already the letter for the conjugation, ignore it            
                    if(form != stem[-1]):
                        conj_present[meanings[i]] = stem + form
                    else:
                        conj_present[meanings[i]] = stem
    
    return(conj_present)


def conjugate_imperative(stem):
    imperative_stem = stem
    if(stem.endswith('g') or stem.endswith('k')):
        imperative_stem = stem[:-1]
    
    return{
        'second person singular': imperative_stem + 'k',
        'second person plural': imperative_stem + 'kite',
        'first person plural': imperative_stem + 'kime'
    }


def conjugate_past(third_past):
    #Get past tense conjugation for the verb
    conj_past = {}
    for cj in past_conj_data:        
        if(third_past.endswith(cj[2])):
            stem = third_past[:-1]
            for i, form in enumerate(cj):
                #Palatalize verb if necessary                
                if(i == 0 and cj[2] == 'ė' and (stem[-1] == 'd' or stem[-1] == 't')):
                    if(stem[-1] == 't'):
                        conj_past[meanings[i]] = stem[:-1] + 'č' + form
                    else:
                        conj_past[meanings[i]] = stem[:-1] + 'dž' + form
                else:
                    conj_past[meanings[i]] = stem + form
        
    return(conj_past)


def conjugate_past_iterative(stem):
    iterative_data = {}
    for i, cj in enumerate(past_conj_data[0]):
        iterative_data[meanings[i]] = stem + 'dav' + cj
    return iterative_data

def conjugate_future(stem, third_past, third_pres):
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
            future_data['third person'] = beginning + future_stem[len(beginning):]
        else:
            future_data[meanings[i]] = future_stem + cj
    return(future_data)

def conjugate_conditional(stem):
    conditional_data = {}
    for i, form in enumerate(conditional_conj_data):
        conditional_data[meanings[i]] = stem + form
    return(conditional_data)

def conjugate(infinitive, third_pres='', third_past=''):
    if(not third_past or not third_pres):
        with open('data.txt', 'r', encoding='utf-8') as f:
            for verb in f.read().split('\n'):
                verb_info = verb.split(', ')
                if(verb_info[0] == infinitive):
                    third_pres = verb_info[1]
                    third_past = verb_info[2]

    data = {}
    stem = infinitive[:-2]
    
    data['present'] = conjugate_present(third_pres)    
    data['imperative'] = conjugate_imperative(stem)    
    data['past'] = conjugate_past(third_past)
    data['past iterative'] = conjugate_past_iterative(stem)
    data['future'] = conjugate_future(stem, third_past, third_pres)
    data['conditional'] = conjugate_conditional(stem)
    
    return(data)
