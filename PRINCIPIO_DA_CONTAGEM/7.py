numeros = [0, 1, 2, 3, 4, 5]

ans = list()  # qnt 3
ans.append(5)
for i in range(2):
    ans.append(6)
result = 1
for i in ans:
    result *= i
print(f'letra A: {result} maneiras.')
b = list()
b.append(5)
for i in range(1, 2+1):
    if i == 1:
        b.append(5)
    else:
        b.append(4)
ans_b = 1
for i in b:
    ans_b *= i
print(f'letra B: {ans_b} maneiras')
c = list()
c.append(5)
for i in range(2):
    if i == 0:
        c.append(6)
    else:
        c.append(3)
ans_c = 1
for i in c:
    ans_c *= i
print(f'letra C: {ans_c} maneiras.')

d = list()
d.append(4)
for i in range(2):
    if i == 0:
        d.append(4)
    else:
        d.append(3)
ans_d = 1
for i in d:
    ans_d *= i
print(f'letra D: {ans_d} maneiras.')
