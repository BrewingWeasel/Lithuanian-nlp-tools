from conjugator import conjugate

def write_conj(d, f):
    for k, v in d.items():
        if(isinstance(v, dict)):
            write_conj(v, f)
        else:
            f.write(d[k] + '\n')


with open('data.txt', 'r', encoding='utf-8') as f:
    verbs = f.read().split('\n')
    verbs = [i.split(',')[0] for i in verbs]

with open('allconjs.txt', 'w', encoding='utf-8') as f:
    for i in verbs:
        a = conjugate(i)
        write_conj(a, f)
        
