from lemmatizer import get_lemma, get_morph
from conjugator import conjugate

print(conjugate('pasikalbėti')['past']['second person singular'])

print(get_lemma('kalbėčiau'))
print(get_morph('kalbėčiau'))
