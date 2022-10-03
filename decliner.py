def read_from_file(file):
    with open(f'data\\{file}.txt', 'r', encoding='utf-8') as f:
        return f.read().split('\n')

NOUNS = read_from_file('nouns')
PROPER_NOUNS = read_from_file('propernouns')

#Which declension the noun ending in 'is' is part of (first or third)
FIRST_IS_DECLENSIONS = read_from_file('first_is_declensions')
THIRD_IS_DECLENSIONS = read_from_file('third_is_declensions')

PRN_DECLENSIONS = [i.split('\t') for i in read_from_file('pronoun_declension')]

with open('data\\noun_data.txt', 'r', encoding='utf-8') as f:
    NOUN_DECLENSIONS = [i.split(', ') for i in f.read().split('\n')]
    CUSTOM_DECLENSIONS = {i[0]: i for i in NOUN_DECLENSIONS}

CASE_NAMES = ['Nominative', 'Genitive', 'Dative', 'Accusative', 'Instrumental', 'Locative', 'Vocative']
GRAM_GENDERS = ['masculine', 'feminine']
CASE_NAMES_PRN = ['Nominative', 'Genitive', 'Dative', 'Accusative', 'Instrumental', 'Locative']
NUMBERS = ['Singular', 'Plural']

ADJ_THIRD_DECLEN_TYPES_DATA = [i.split(', ') for i in read_from_file('adjective_declension_data')]
ADJ_THIRD_DECLEN_TYPES = {i[0]: i[1] for i in ADJ_THIRD_DECLEN_TYPES_DATA}


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


DATA_ADJS = {
    'ias': [
        [
            ['ias', 'io', 'iam', 'ią', 'iu', 'iame'],
            ['i', 'ių', 'iems', 'ius', 'iais', 'iuose']
        ],
        [
            ['ia', 'ios', 'iai', 'ią', 'ia', 'ioje'],
            ['ios', 'ių', 'ioms', 'ias', 'iomis', 'iose']
        ]
    ],
    'as': [
        [
            ['as', 'o', 'am', 'ą', 'u', 'ame'],
            ['i', 'ų', 'iems', 'us', 'ais', 'uose']
        ],
        [
            ['a', 'os', 'ai', 'ą', 'a', 'oje'],
            ['os', 'ų', 'oms', 'as', 'omis', 'ose']
        ]
    ],
    'us': [
        [
            ['us', 'aus', 'iam', 'ų', 'iu', 'iame'],
            ['ūs', 'ių', 'iems', 'ius', 'iais', 'iuose']
        ],
        [
            ['i', 'ios', 'iai', 'ią', 'ia', 'ioje'],
            ['ios', 'ių', 'ioms', 'ias', 'iomis', 'iose']
        ]
    ],
    'is': [
        [
            ['is', 'io', 'iam', 'į', 'iu', 'iame'],
            [['iai', 'i'], 'ios', ['iams', 'iems'], 'ius', 'iais', 'iuose']
        ],
        [
            ['ė', 'ės', 'ei', 'ę', 'e', 'ėje'],
            ['ės', 'ių', 'ėms', 'es', 'ėmis', 'ėse']
        ]
    ]

}



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
    for cur_decl in PRN_DECLENSIONS:
        cur_decl = [i.strip() for i in cur_decl]
        if(pronoun in cur_decl):
            return dict(zip(CASE_NAMES_PRN, cur_decl))


def decline_noun(noun):
    """Gets the declension for a noun
    Parameters:
        noun (string): the noun to decline
    Returns:
        declension (dict): the declension of the noun"""
    declension = {}
    if(noun in IRREGULAR_NOUNS):
        return IRREGULAR_NOUNS[noun]
    
    for i, ending in enumerate(ENDINGS):
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
                                declension[NUMBERS[num_index]][cur_case] = CUSTOM_DECLENSIONS[noun][num_unconfident]
                            num_unconfident += 1
                        else:
                            declined_noun = noun_stem + case
                            if(noun_stem.endswith('t') and case.startswith('i')):
                                declined_noun = noun_stem[:-1] + 'č' + case
                            if(noun_stem.endswith('d') and case.startswith('i')):
                                declined_noun = noun_stem[:-1] + 'dž' + case
                            declension[NUMBERS[num_index]][cur_case] = declined_noun
    return declension


def decline_adjective(adjective):
    for ending in DATA_ADJS.keys():
        if(adjective.endswith(ending)):
            declension = {}
            adjective_stem = adjective[:-len(ending)]
            for gender, next_declensions in enumerate(DATA_ADJS[ending]):
                declension[GRAM_GENDERS[gender]] = {}
                for number, final_declension in enumerate(next_declensions):
                    declension[GRAM_GENDERS[gender]][NUMBERS[number]] = {}
                    for case_index, case in enumerate(final_declension):
                        if(isinstance(case, list)):
                            declension[GRAM_GENDERS[gender]][NUMBERS[number]][CASE_NAMES[case_index]] = adjective_stem + case[int(ADJ_THIRD_DECLEN_TYPES[adjective])]
                        else:
                            declension[GRAM_GENDERS[gender]][NUMBERS[number]][CASE_NAMES[case_index]] = adjective_stem + case
            return declension