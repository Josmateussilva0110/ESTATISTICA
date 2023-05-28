from FUNCOES import *
population = [1453756, 653385, 3221940, 395725, 7065573, 587311, 1243627]
area = [237576.167, 164165.250, 1559161.810, 224298.980, 1247689.515, 142814.585, 277620.914]
region = ['RO', 'AC', 'AM', 'RR', 'PA', 'AP', 'TO']
density_total = list()

density_total = calculate_density(population, area)
sun_density = sum(density_total)
sun_population = sum(population)

percentage = calculate_percentage(density_total, sun_density)
percentage_population = calculate_percentage(population, sun_population)

result = occupy_dict(region, percentage)
result2 = occupy_dict(region, percentage_population)

print_dict(result, 'PORCENTAGEM DA DENSIDADE:')
print_dict(result2, 'PORCENTAGEM DA POPULAÇÃO:')
