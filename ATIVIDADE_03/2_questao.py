from math import sqrt
dados = [22, 22, 26, 24, 23, 27, 25, 20, 24, 26, 25, 25, 19, 24, 20, 22, 24, 25, 25, 20]
result = sum(dados) / len(dados)
dados.sort()
occurence = list()

#pegar a moda
for i in dados:
    occurence.append(dados.count(i))
upper = max(occurence)

# pegar a moda 
for i in dados:
    if dados.count(i) == upper:
        style = i

#pegar a mediana
for index, value in enumerate(dados):
    if index == 10:
        median = (dados[index] + dados[index+1]) / 2
        break

#pegar a variancia
difference = list()
for i in dados:
    diff = ((i - result) ** 2)
    difference.append(diff)
sun_difference = sum(difference)
variance = sun_difference / len(dados)

#pegar o desvio padrão
standard_deviation = sqrt(variance)

print(f'media = {result:.2f}')
print(f'moda = {style}')
print(f'mediana = {median:.2f}')
print(f'variancia = {variance:.2f}')
print(f'desvio padrao = {standard_deviation:.2f}')
