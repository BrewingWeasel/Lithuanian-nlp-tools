from lemmatizer import get_lemma, get_morph
from conjugator import conjugate

print(conjugate('galėti')['present']['first person singular'])

print(get_lemma('galiu'))
print(get_morph('eik'))