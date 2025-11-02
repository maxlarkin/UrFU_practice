import requests
from typing import Optional
from random import randint


class Pokemon:
    """Класс покемона"""
    def __init__(self, name: str, abilities: list[str]):
        self.name = name
        self.abilities = abilities

    """Сравнение покемонов"""
    def __eq__(self, value):
        if isinstance(value, Pokemon) and self.name == value.name:
            return True
        return False


def get_pokemon_by_name(name: str) -> Optional[Pokemon]:
    """Получение покемона по имени"""
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}').json()
        if response:
            return Pokemon(response['name'], response['abilities'])
        else:
            return None
    except Exception:
        print('Нет такого покемона')
        return None


class Team:
    """Класс команды"""
    def __init__(self, pokemons: list[Pokemon]):
        self.pokemons = pokemons

    """Добавить покемона в команду"""
    def add_pokemon(self, name: str) -> str:
        pokemon = get_pokemon_by_name(name)
        if pokemon not in self.pokemons and pokemon:
            self.pokemons.append(pokemon)
            return 'Покемон добавлен в команду'
        else:
            return ''

    """Удалить покемона из команды"""
    def remove_pokemon(self, name: str) -> str:
        pokemon = get_pokemon_by_name(name)
        if pokemon in self.pokemons:
            self.pokemons.remove(pokemon)
            return 'Покемон удален из команды'
        else:
            return 'Такого покемона нет в команде'

    """Получить информацию о покемоне"""
    def get_info_pokemon(self, pokemon_name: str) -> Optional[Pokemon]:
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                return pokemon
        return None

    """Бой между двумя покемонами"""
    def buttle(self, first_pokemon_name: str, second_pokemon_name: str) -> str:
        first_pokemon = self.get_info_pokemon(first_pokemon_name)
        second_pokemon = self.get_info_pokemon(second_pokemon_name)

        if first_pokemon and second_pokemon:
            num = randint(1, 10)
            message = 'Победил '
            message += first_pokemon.name if num <= 5 else second_pokemon.name
            return message
        else:
            return 'Введено неправильное название покемона'

    """Вывод команды"""
    def __str__(self):
        return ', '.join([pokemon.name for pokemon in self.pokemons])


names = list(map(lambda y: y['name'], requests.get('https://pokeapi.co/api/v2/pokemon/').json()['results']))

init_names = input('Введите имена покемонов через пробел: ').split()
init_pokemons = [el for el in [get_pokemon_by_name(name) for name in init_names] if el]

team = Team(init_pokemons)

while True:
    print('*' * 100)
    command = input('1 - добавить покемона, \
    2 - удалить покемона,\
    3 - получить информацию о покемоне,\
    4 - бой между двумя покемонами,\
    5 - список покемонов, \
    0 - выход: ')

    match command:
        case '1':
            name = input('Введите имя покемона: ')
            print(team.add_pokemon(name))
        case '2':
            if team.pokemons:
                name = input('Введите имя покемона: ')
                print(team.remove_pokemon(name))
            else:
                print('Команда пуста')
        case '3':
            if team.pokemons:
                name = input('Введите имя покемона: ')
                pokemon = team.get_info_pokemon(name)
                if pokemon:
                    print('Имя:', pokemon.name)
                    print('Способности:', ', '.join([ability['ability']['name'] for ability in pokemon.abilities]))
            else:
                print('Команда пуста')
        case '4':
            if team.pokemons:
                first_pokemon_name = input('Введите имя первого покемона: ')
                second_pokemon_name = input('Введите имя второго покемона: ')
                print(team.buttle(first_pokemon_name, second_pokemon_name))
            else:
                print('Команда пуста')
        case '5':
            if team.pokemons:
                print(team)
            else:
                print('Команда пуста')
        case _:
            break
