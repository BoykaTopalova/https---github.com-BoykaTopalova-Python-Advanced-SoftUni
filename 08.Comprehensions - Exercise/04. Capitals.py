# lands = [land for land in input().split(', ')]
# capitals = [capital for capital in input().split(', ')]
# dicts = {lands[ind]: capitals[ind] for ind in range(len(lands))}
# for x, y in dicts.items():
#     print(f'{x} -> {y}')
countries = input().split(', ')
capitals = input().split(', ')
dictionary = {key: value for (key, value) in zip(countries, capitals)}
[print(f"{country} -> {capital}") for country, capital in zip(countries, capitals)]
# [print(f"{country} -> {capital}") for country, capital in dictionary.items()]