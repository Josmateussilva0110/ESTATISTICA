def calculate_density(population, area):
    density_total = list()
    for i in range(len(area)):
        density = population[i] / area[i]
        density_total.append(density)
    return density_total


def sum_density(density):
    return sum(density)


def calculate_percentage(density_total, sun_density):
    percentage = list()
    for i in range(len(density_total)):
        total = (density_total[i] * 100) / sun_density
        percentage.append(total)
    return percentage


def occupy_dict(region, percentage):
    result = dict()
    for i, element in enumerate(region):
        result[element] = percentage[i]
    return result


def print_dict(dados, lista = ''):
    print(lista)
    for k, i, in dados.items():
        print(f'{k} - {i:.2f}%')
