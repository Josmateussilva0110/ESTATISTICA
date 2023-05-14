from random import randint

values = list()
for _ in range(10):
    value = randint(0, 100)
    values.append(value)
sun = sum(values)
print(f'media = {sun / 10}')
