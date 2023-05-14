from random import randint

values = list()
ocorrencias = dict()
modas = list()
for _ in range(10):
    value = randint(0, 10)
    values.append(value)

print(f'valores = {values}')
for i in values:
    if i in ocorrencias:
        ocorrencias[i] += 1
    else:
        ocorrencias[i] = 1
moda = 0
for key, item in ocorrencias.items():
    if item > moda:
        moda = item
        aux = key

for key1, item1 in ocorrencias.items():
    if item1 == moda:
        modas.append(key1)
if len(modas) == 1:
    print(f'moda = {modas}')
else:
    print(f'modas {modas}')
