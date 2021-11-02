import random

key = 'Hundefutter12qwdqweqweijqwidjiasd2'

meta = ['Cool', 'TOP', 'Super Service', 'Alex', 'Bob', 'Anna']

for daten in range(5):
    meta.append(key)
    random.shuffle(meta)
    result = ' '.join(meta)
    a = len(result)

    if a > 70 and a <= 160:
        print(result)
    else:
        continue
