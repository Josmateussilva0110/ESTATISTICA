values = list()
cont = dict()
modas = list()
for _ in range(10):
    value = int(input())
    values.append(value)
for i in values:
    if i in cont:
        cont[i] += 1
    else:
        cont[i] = 1
moda = 0
for k, v in cont.items():
    if v > moda:
        moda = v
        aux = k


for j, l in cont.items():
    if l == moda:
        modas.append(j)

if len(modas) == 1:
    print(f'moda = {modas}')
else:
    print(f'modas = {modas}')
