values = list()

for _ in range(10):
    value = int(input())
    values.append(value)
values.sort()
print(values)
lower = upper = values[0]
for i in values:
    if i > upper:
        upper = i
    if i < lower:
        lower = i
difference = upper - lower 
print(f'Anplitude = {difference}')
