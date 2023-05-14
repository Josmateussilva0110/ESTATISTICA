values = list()
for _ in range(10):
    value = int(input())
    values.append(value)
values.sort()
print(f'{values}')
if len(values) % 2 != 0:
    mediana = len(values) // 2
    for i, v in enumerate(values):
        if i == mediana:
            aux = v
    print(f'mediana = {aux}')
else:
    mediana = (len(values) // 2) -1 
    mediana2 = mediana + 1
    for i, v in enumerate(values):
        if i == mediana:
            aux = v
        if i == mediana2:
            aux2 = v
    result = (aux + aux2) / 2
    print(f'mediana = {result}')
