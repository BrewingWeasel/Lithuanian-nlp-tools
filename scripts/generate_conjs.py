from conjugator import conjugate

def write_conj(d, i, f):
    for k, v in d.items():
        if(isinstance(v, dict)):
            write_conj(v, i, f)
        else:
            f.write(f'{d[k]}, {i}\n')


with open('data\\data.txt', 'r', encoding='utf-8') as f:
    verbs = f.read().split('\n')
    verbs = [i.split(',')[0] for i in verbs]

with open('allconjs.txt', 'w', encoding='utf-8') as f:
    for i in verbs:
        f.write(i + ', ' + i + '\n')
        a = conjugate(i)
        write_conj(a, i, f)
    for i in verbs:
        i = i + 's'
        f.write(i + ', ' + i + '\n')
        a = conjugate(i)
        write_conj(a, i, f)
        
