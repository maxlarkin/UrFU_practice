# Коды
### Задача 1
```python
alphEn = 'abcdefghijklmnopqrstuvwxyz'
alphRu = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

inp = list(input('Введите строку: ').lower())
fId = input('Выберите функцию: 1 - кодирование, 2 - декодирование: ')

def coding(s: list[str]):
    alph = ''
    res = ''

    if s[0] in alphEn:
        alph = alphEn
    elif s[0] in alphRu:
        alph = alphRu
    else:
        print('Невозможно определить язык')
        return 0
    
    for char in s:
        i = alph.index(char)
        res += alph[(i+1) if (i+1 < len(alph)) else 0]

    return res

def decoding(s: list[str]):
    alph = ''
    res = ''

    if s[0] in alphEn:
        alph = alphEn
    elif s[0] in alphRu:
        alph = alphRu
    else:
        print('Невозможно определить язык')
        return 0
    
    for char in s:
        i = alph.index(char)
        res += alph[(i-1) if (i-1) >= 0 else len(alph)-1]

    return res

if fId == '1':
    print(coding(inp))
elif fId == '2':
    print(decoding(inp))
else: 
    print('Невозможно определить функцию')
```
### Задача 2
```python 
def check_winners(scores: list[int], student_score: str):
    if student_score in sorted(scores)[-3:]:
        print('Вы в тройке победителей!')
    elif student_score in scores:
        print('Вы не попали в тройку победителей.')
    else:
      print('Ваши баллы не найдены в списке.')

scores = [int(x) for x in input('Введите баллы через пробел: ').split(' ')]
student_score = int(input('Введите свои баллы: '))

check_winners(scores, student_score)
```
### Задача 3
```python
def print_pack_report(cnt_cupcakes: int):
    for i in range(cnt_cupcakes, 1, -1):
        if i % 3 == 0 and i % 5 == 0:
            print(f'{i} - расфасуем по 3 или по 5')
        elif i % 5 == 0: 
            print(f'{i} - расфасуем по 5')
        elif i % 3 == 0:
            print(f'{i} - расфасуем по 3')
        else:
            print(f'{i} - не заказываем!')

cnt_cupcakes = int(input('Введите число: '))
print_pack_report(cnt_cupcakes)
```

### Задача 4
```python 
from random import shuffle, choices

def generate_password(options):
    uperAlph = 'abcdefghijklmnopqrstuvwxyz'.upper()
    lowerAlph = 'abcdefghijklmnopqrstuvwxyz'
    nums = '0123456789'
    specChars = '!@#$%^&*'

    chars = ''
    if options['isLowerReg']: chars += lowerAlph
    if options['isUpperReg']: chars += uperAlph
    if options['specChars']: chars += specChars
    if options['nums']: chars += nums

    if chars == '': return 'Нет доступных для выбора символов'

    return ''.join(choices(chars, k=options['passwordLen']))

options = {}
print('1 - Да, 0 - нет')
options['isLowerReg'] = int(input('Добавить символы нижнего регистра? '))
options['isUpperReg'] = int(input('Добавить символы верхнего регистра? '))
options['specChars'] = int(input('Добавить спец символы? '))
options['nums'] = int(input('Добавить цифры? '))
options['passwordLen'] = int(input('Введите длину пароля: '))

print(generate_password(options))
```

### Задача 5
```python
rimChars = {'I': 1,
           'V': 5,
           'X': 10,
           'L': 50,
           'C': 100,
           'D': 500,
           'M': 1000
           }

def fromRimToDec(rimNum: str):
    prev = 0
    res = 0
    for i in range(len(rimNum), 0, -1):
        num = rimChars[rimNum[i-1]]
        if rimChars[rimNum[i-1]] < prev:  
            res -= num
        else:
            res += rimChars[rimNum[i-1]]
        prev = num
    return res

def fromDecToRim(n: int):

    decNums = list(rimChars.values())
    chars = list(rimChars.keys())
    res = ''

    for i in range(len(decNums), 0, -1):
        curValue = decNums[i-1]
        curChar = chars[i-1]
        numChars = n // curValue

        if i % 2 == 0:
            if n // decNums[i-2] == 9:
                res += chars[i-2] + chars[i]
                n -= (decNums[i] - decNums[i-2])
                continue

        if numChars > 3:
            res += curChar + chars[i]
        else:
            res += numChars * curChar
        n -= numChars * curValue
        
        
        
    return res

print('1 - Перевод римского числа в десятичное, 2 - перевод из десятичного в римское')
f = input('Введите функцию: ')
n = input('Введите число: ')

if f == '1':
    print(fromRimToDec(n))
else:
    print(fromDecToRim(int(n)))

'''Test'''
# roman_tests = ['IV', 'IX', 'XLII', 'XCIX', 'MMXXIII']
# decNums = [fromRimToDec(x) for x in roman_tests]
# rimNums = [fromDecToRim(x) for x in decNums]
# print('from rim to dec: ', decNums)
# print('from dec to rim: ', rimNums)
```

### Задача 6
```python 
from getpass import getpass

# функция выводит виселицу в консоль и в зависимости от количества ошибок добавляет в исходный выход символы
def showGallows(cntErrors):
    print('_________')
    print('|--|   ' + ('|' if cntErrors >= 1 else ' '))
    print('|--|   ' + ('O' if cntErrors >= 2 else ' '))
    print('|--|  ' + ('/' if cntErrors >= 3 else ' ') + ('|' if cntErrors >= 4 else ' ') + ('\\' if cntErrors >= 5 else ' '))
    print('|--|  ' + ('/' if cntErrors >= 6 else ' ') + (' \\' if cntErrors >= 7 else ' '))
    print('|__|')


word = list(getpass('Первый игрок загадывает слово (ничего не отображается при вводе): '))
cntErrors = 0
usedChars = set()
temp = ['|*|'] * len(word)

while cntErrors < 7:
    letter = input('Второй игрок вводит букву: ').lower()
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                temp[i] = f'|{letter}|'
    else:
        cntErrors += 1

    showGallows(cntErrors)

    print(''.join(temp))

    usedChars.add(letter)
    print('Использованные буквы: ', ' '.join(usedChars))

    if '|*|' not in temp:
        print('Выиграл второй игрок!')
        break
    elif cntErrors == 7:
        print('Выиграл первый игрок!')
```
