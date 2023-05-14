values = list()
for _ in range(20):
    value = int(input())
    values.append(value)
values.sort()
print(values)
tam = len(values)
q1 = int(tam * 0.25)
q2 = int(tam * 0.5)
q3 = int(tam * 0.75)
print('q1 = ', end='')
for i in range(q1):
    print(f'{values[i]}', end=' ')
print()
print('q2 = ', end='')
for i in range(q1, q2):
    print(f'{values[i]}', end=' ')
print()
print('q3 = ', end='')
for i in range(q2, q3):
    print(f'{values[i]}', end=' ')
print()
print('q4 = ', end='')
for i in range(q3, tam):
    print(f'{values[i]}', end=' ')
