import random

key = input('Key: ')
count = int(input('Anzahl: '))

meta = ['TOP-Auswahl!', '★ TOP Qualität', 'Super Service ☆', '✓ hier klicken ▶ und mehr erfahren']


for daten in range(count):
    meta.append(key)
    random.shuffle(meta)
    result = ' '.join(meta)
    a = len(result)

    if a > 70 and a <= 160:
        print(result)
    else:
        continue

print('Finish')