from requests import get


"""Получение и вывод 20 покемонов"""
pokemons = get('https://pokeapi.co/api/v2/pokemon/').json()["results"]
print([pokemon["name"] for pokemon in pokemons])

"""Ввод имени покемона и получение его данных"""
find_name = input("Enter a pokemon name: ")
res_pokemon = get(f'https://pokeapi.co/api/v2/pokemon/{find_name}').json()

pokemon_types = res_pokemon['types']
pokemon_abilities = [ab['ability']['name'] for ab in res_pokemon['abilities']]
"""Вывод данных покемона"""
print('Имя:', res_pokemon['name'])
print('Тип:', ', '.join([type['type']['name'] for type in pokemon_types]))

print('Вес:', res_pokemon['weight'])
print('Рост:', res_pokemon['height'])
print('Способности:', ', '.join(pokemon_abilities))
