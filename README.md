# Lithuanian-nlp

A python tool to programmatically do several nlp tools for Lithuanian, such as:
-Conjugate verbs
-Decline nouns & adjectives
-Lemmatize words (currently only works for verbs)

verb data (data/data.txt) from verbalyser by ror-expert (https://github.com/ror-expert/verbalyser)

Future plans:
- ~~support reflexive verbs~~
- ~~support lemmatization of verbs with prefixes~~
- support ~~nouns and adjectives~~ (partially completed)
- support prepositions
- support detection of word type
- add more features :)

Usage:
```
conjugate('norėti')['present']['first person singular'] --> noriu
lemmatize('noriu') --> norėti
```


(this is my first github project)
