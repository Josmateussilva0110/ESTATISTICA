from random import randint
values = list()

for _ in range(10):
    value = randint(1, 100)
    values.append(value)
values.sort()
print(values)
lower = min(values)
upper = max(values)
difference = upper - lower 
print(f'Anplitude = {difference}')
