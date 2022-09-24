with open('data\\pronoun_declension.txt', 'r', encoding='utf-8') as f:
    CONJS = [i.split('\t') for i in f.read().split('\n')]

with open('data\\noun_data.txt', 'r', encoding='utf-8') as f:
    NOUN_DECLENSIONS = [i.split(', ') for i in f.read().split('\n')]
    CUSTOM_DECLENSIONS = {i[0]: i for i in NOUN_DECLENSIONS}

with open('data\\nouns.txt', 'r', encoding='utf-8') as f:
    NOUNS = f.read().split('\n')

with open('data\\propernouns.txt', 'r', encoding='utf-8') as f:
    PROPER_NOUNS = f.read().split('\n')

with open('data\\first_is_declensions.txt', 'r', encoding='utf-8') as f:
    FIRST_IS_DECLENSIONS = f.read().split('\n')

with open('data\\third_is_declensions.txt', 'r', encoding='utf-8') as f:
    THIRD_IS_DECLENSIONS = f.read().split('\n')

CASE_NAMES = ['Nominative', 'Genitive', 'Dative', 'Accusative', 'Instrumental', 'Locative', 'Vocative']
CASE_NAMES_PRN = ['Nominative', 'Genitive', 'Dative', 'Accusative', 'Instrumental', 'Locative']
NUMBERS = ['Singular', 'Plural']

ENDINGS = ['as', 'is', 'ys', 'ias', 'a', 'ė', 'is', 'us', 'ius', 'uo']
DATA = [
        [
            ['as', 'o', 'ui', 'ą', 'u', ['e', 'ai', 'au']],
            ['ai', 'ų', 'ams', 'us', 'ais', 'uose', 'ai']
        ],
        [
            ['is', 'io', 'iui', 'į', 'iu', 'yje', 'i'],
            ['iai', 'ių', 'iams', 'ius', 'iais', 'iuose', 'iai']
        ],
        [
            ['ys', 'io', 'iui', 'į', 'iu', 'yje', 'y'],
            ['iai', 'ių', 'iams', 'ius', 'iais', 'iuose', 'iai']
        ],
        [
            ['ias', 'io', 'iui', 'ią', 'iu', 'yje', ['y', 'iau']],
            ['iai', 'ių', 'iams', 'ius', 'iais', 'iuose', 'iai']
        ],
        [
            ['a', 'os', 'ai', 'ą', 'a', 'oje', 'a'],
            ['os', 'ų', 'oms', 'as', 'omis', 'ose', 'os']
        ],
        [
            ['ė', 'ės', 'ei', 'ę', 'e', 'ėje', 'e'],
            ['ės', 'ių', 'ėms', 'es', 'ėmis', 'ėse', 'ės']
        ],
        [
            ['is', 'ies', ['iai', 'iui'], 'į', 'imi', 'yje', 'ie'],
            ['ys', ['ių', 'ų'], 'ims', 'is', 'imis', 'yse', 'ys']
        ],
        [
            ['us', 'aus', 'ui', 'ų', 'umi', 'uje', 'au'],
            ['ūs', 'ų', 'ums', 'us', 'umis', 'uose', 'ūs']
        ],
        [
            ['ius', 'iaus', 'iui', 'ių', 'iumi', 'iuje', 'iau'],
            ['iai', 'ių', 'iams', 'ius', 'iais', 'iuose', 'iai']
        ],
        [
            ['uo', 'ens', 'eniui', 'enį', 'eniu', 'enyje', 'enie'],
            ['enys', 'enų', 'enims', 'enis', 'enimis', 'enyse', 'enys']
        ],
    ]

IRREGULAR_NOUNS = {
    'duktė': {
        'Singular': {
            'Nominative': 'duktė',
            'Genitive': 'dukters',
            'Dative': 'dukteriai',
            'Accusative': 'dukterį',
            'Instrumental': 'dukteria',
            'Locative': 'dukteryje',
            'Vocative': 'dukterie'
        },
        'Plural': {
            'Nominative': 'dukterys',
            'Genitive': 'dukterų',
            'Dative': 'dukterims',
            'Accusative': 'dukteris',
            'Instrumental': 'dukterimis',
            'Locative': 'dukteryse',
            'Vocative': 'dukterys'
        }
    },
    'sesuo': {
        'Singular': {
            'Nominative': 'sesuo',
            'Genitive': 'sesers',
            'Dative': 'seseriai',
            'Accusative': 'seserį',
            'Instrumental': 'seseria',
            'Locative': 'seseryje',
            'Vocative': 'seserie'
        },
        'Plural': {
            'Nominative': 'seserys',
            'Genitive': 'seserų',
            'Dative': 'seserims',
            'Accusative': 'seseris',
            'Instrumental': 'seserimis',
            'Locative': 'seseryse',
            'Vocative': 'seserys'
        }
    },
    'moteris': {
        'Singular': {
            'Nominative': 'moteris',
            'Genitive': 'moters',
            'Dative': 'moteriai',
            'Accusative': 'moterį',
            'Instrumental': 'moterimi',
            'Locative': 'moteryje',
            'Vocative': 'moterie'
        },
        'Plural': {
            'Nominative': 'moterys',
            'Genitive': 'moterų',
            'Dative': 'moterims',
            'Accusative': 'moteris',
            'Instrumental': 'moterimis',
            'Locative': 'moteryse',
            'Vocative': 'moterys'
        }
    },
    'dieveris': {
        'Singular': {
            'Nominative': 'dieveris',
            'Genitive': 'dieviers',
            'Dative': 'dieveriui',
            'Accusative': 'dieverį',
            'Instrumental': 'dieverimi',
            'Locative': 'dieveryje',
            'Vocative': 'dieverie'
        },
        'Plural': {
            'Nominative': 'dieverys',
            'Genitive': 'dieverių',
            'Dative': 'dieverims',
            'Accusative': 'dieveris',
            'Instrumental': 'dieverimis',
            'Locative': 'dieveryse',
            'Vocative': 'dieverys'
        }
    },
    'obelis': {
        'Singular': {
            'Nominative': 'obelis',
            'Genitive': 'obelies',
            'Dative': 'obeliai',
            'Accusative': 'obelį',
            'Instrumental': 'obelimi',
            'Locative': 'obelyje',
            'Vocative': 'obelie'
        },
        'Plural': {
            'Nominative': 'obelys',
            'Genitive': 'obelų',
            'Dative': 'obelims',
            'Accusative': 'obelis',
            'Instrumental': 'obelimis',
            'Locative': 'obelyse',
            'Vocative': 'obelys'
        }
    },
    'šuo': {
        'Singular': {
            'Nominative': 'šuo',
            'Genitive': 'šuns',
            'Dative': 'šuniui',
            'Accusative': 'šunį',
            'Instrumental': 'šuniu',
            'Locative': 'šunyje',
            'Vocative': 'šunie'
        },
        'Plural': {
            'Nominative': 'šunys',
            'Genitive': 'šunų',
            'Dative': 'šunims',
            'Accusative': 'šunis',
            'Instrumental': 'šunimis',
            'Locative': 'šunyse',
            'Vocative': 'šunys'
        }
    },
    'mėnuo': {
        'Singular': {
            'Nominative': 'mėnuo',
            'Genitive': 'mėnesio',
            'Dative': 'mėnesiui',
            'Accusative': 'mėnesį',
            'Instrumental': 'mėnesiu',
            'Locative': 'mėnesyje',
            'Vocative': 'mėnesi'
        },
        'Plural': {
            'Nominative': 'mėnesiai',
            'Genitive': 'mėnesių',
            'Dative': 'mėnesiams',
            'Accusative': 'mėnesius',
            'Instrumental': 'mėnesiais',
            'Locative': 'mėnesiuose',
            'Vocative': 'mėnesiai'
        }
    },
    'žmogus': {
        'Singular': {
            'Nominative': 'žmogus',
            'Genitive': 'žmogaus',
            'Dative': 'žmogui',
            'Accusative': 'žmogų',
            'Instrumental': 'žmogumi',
            'Locative': 'žmoguje',
            'Vocative': 'žmogau'
        },
        'Plural': {
            'Nominative': 'žmonės',
            'Genitive': 'žmonių',
            'Dative': 'žmonėm',
            'Accusative': 'žmones',
            'Instrumental': 'žmonėmis',
            'Locative': 'žmonėse',
            'Vocative': 'žmonės'
        }
    },
    'pati': {
        'Singular': {
            'Nominative': 'pati',
            'Genitive': 'pačios',
            'Dative': 'pačiai',
            'Accusative': 'pačią',
            'Instrumental': 'pačia',
            'Locative': 'pačioje',
            'Vocative': 'pačia'
        },
        'Plural': {
            'Nominative': 'pačios',
            'Genitive': 'pačių',
            'Dative': 'pačioms',
            'Accusative': 'pačias',
            'Instrumental': 'pačiomis',
            'Locative': 'pačiose',
            'Vocative': 'pačios'
        }
    },
    'marti': {
        'Singular': {
            'Nominative': 'marti',
            'Genitive': 'marčios',
            'Dative': 'marčiai',
            'Accusative': 'marčią',
            'Instrumental': 'marčia',
            'Locative': 'marčioje',
            'Vocative': 'marčia'
        },
        'Plural': {
            'Nominative': 'marčios',
            'Genitive': 'marčių',
            'Dative': 'marčioms',
            'Accusative': 'marčias',
            'Instrumental': 'marčiomis',
            'Locative': 'marčiose',
            'Vocative': 'marčios'
        }
    },
}



def decline_pronoun(pronoun):
    for cur_conj in CONJS:
        cur_conj = [i.strip() for i in cur_conj]
        if(pronoun in cur_conj):
            return dict(zip(CASE_NAMES_PRN, cur_conj))


def decline_noun(noun):
    declension = {}
    if(noun in IRREGULAR_NOUNS):
        return IRREGULAR_NOUNS[noun]
    for i, ending in enumerate(ENDINGS):
        print(i, ending)
        if(noun.endswith(ending)):
            if(not ending == 'is' or ((i == 1 and noun in FIRST_IS_DECLENSIONS) or (i == 6 and noun in THIRD_IS_DECLENSIONS))):
                noun_stem = noun.rstrip(ending)
                num_unconfident = 1
                for num_index, num in enumerate(DATA[i]):
                    declension[NUMBERS[num_index]] = {}
                    for case_index, case in enumerate(num):
                        cur_case = CASE_NAMES[case_index]
                        #If the case can vary
                        if(isinstance(case, list)):
                            #Vocative for nouns ending in as
                            if(i == 0):
                                if(noun in NOUNS):
                                    if(noun_stem.endswith('j')):
                                        declension['Singular']['Locative'] = CUSTOM_DECLENSIONS[noun][num_unconfident]
                                        declension['Singular']['Vocative'] = noun_stem + 'au'                                    
                                    else:
                                        declension['Singular']['Vocative'] = noun_stem + 'e'
                                if(noun in PROPER_NOUNS):
                                    declension['Singular']['Vocative'] = noun_stem + 'ai'
                            else:
                                print(num_unconfident)                        
                                declension[NUMBERS[num_index]][cur_case] = CUSTOM_DECLENSIONS[noun][num_unconfident]
                            num_unconfident += 1
                        else:
                            declined_noun = noun_stem + case
                            if(noun_stem.endswith('t') and case.startswith('i')):
                                declined_noun = noun_stem[:-1] + 'č' + case
                            if(noun_stem.endswith('d') and case.startswith('i')):
                                declined_noun = noun_stem[:-1] + 'dž' + case
                            declension[NUMBERS[num_index]][cur_case] = declined_noun
    return(declension)