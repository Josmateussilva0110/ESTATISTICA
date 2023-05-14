values = list()
decis = list()
for _ in range(20):
    value = int(input())
    values.append(value)
values.sort()
print(values)
tam = len(values)
for i in range(1, 11):
    lower_index = int(tam * (i-1) / 10)
    upper_index = int(tam * i / 10)
    decis.append(values[lower_index:upper_index])
for i, decil in enumerate(decis):
    print(f"Decil {i+1}: {decil}")
