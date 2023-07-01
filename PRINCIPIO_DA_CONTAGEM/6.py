def prime(n):
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont +=1
    if cont == 2:
        return True
    else:
        return False


ans = list()  # tam 6

algarismos = list()
for i in range(10):
    algarismos.append(i)


# pegar os primos
primes = list()
for i in range(len(algarismos)):
    if prime(algarismos[i]):
        primes.append(algarismos[i])
qnt_primes = len(primes)


# pegar os multiplos de 4
mult_for = list()
for i in algarismos:
    if i % 4 == 0:
        mult_for.append(i)
qnt_mult_for = len(mult_for)


for i in range(6):
    if i == 0:
        ans.append(qnt_primes)
    if i == 1 or i == 3:
        ans.append(len(algarismos))
    if i == 2:
        ans.append(qnt_mult_for)
    if i == 4 or i == 5:
        ans.append(1)

# resultado

print(ans)
result = 1
for i in ans:
    result *= i
print(f'{result} maneiras.')
