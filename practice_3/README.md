# Практика №3
```python
import datetime
from decimal import Decimal


DATE_FORMAT = '%Y-%m-%d'
goods = {}

# Добавляет продукт в переданный объект
def add(items, title, amount, expiration_date=None):
    if expiration_date:
        year, month, day = [int(el) for el in expiration_date.split('-')]
        expiration_date = datetime.date(year, month, day)

    obj_of_food = {'amount': amount, 'expiration_date': expiration_date}

    if title in items.keys():
        items[title].append(obj_of_food)
    else:
        items[title] = [obj_of_food]

# Преобразовывает строку в читаемые данные и передает их в функцию "add"
def add_by_note(items, note):
    split_note = note.split(' ')
    date = None
    amount = None
    title = None

    if '-' in split_note[-1]:
        date = split_note.pop()
    amount = Decimal(split_note.pop())
    title = ' '.join(split_note)
    add(items, title, amount, date)

# Проходится по ключам переданного объекта и возвращает те, в которые входит переданная подстрока
def find(items, needle):
    search_result = []
    for title in items.keys():
        if needle.lower() in title.lower():
            search_result.append(title)
    return search_result

# Получает подходящие под переданную подстроку названия продуктов с помощью "find" и подсчитывает количество
def amount(items, needle):
    titles = find(items, needle)
    total_amount = Decimal('0')

    for title in titles:
        total_amount += sum(el['amount'] for el in items[title])
    return total_amount
```
