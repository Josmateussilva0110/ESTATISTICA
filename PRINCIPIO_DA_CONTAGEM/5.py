# A
ans = list()
men = 4
women = 6
men_women = men + women
j = 0
for i in range(3):
    ans.append(men_women -j)
    j += 1
result = 1
for i in ans:
    result *= i


# B
ans2 = list()
k = 1
result2 = 1
ans2.append(women)
for i in range(2):
    ans2.append(men_women - k)
    k += 1
for i in ans2:
    result2 *= i
print(f'{result} modos.')
print('letra B:')
print(f'{result2} modos.')
