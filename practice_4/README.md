# Practice 4

### Задачи:

```python
Task 1
# Класс Book для объекта книги
class Book:

  # Задание заголовка, автора и года при инициализации
  def __init__(self, title: str, author: str, year: str):
    self.title = title
    self.author = author
    self.year = year

  # получение заголовка, автора и года
  def info(self) -> str:
    return f'{self.title} - {self.author} ({self.year})'

# Создание объекта класса Book
test = Book('Kapital', 'Karl Marks', '19**')

# Получение информации из объекта
print(test.info())
```

```python
Task 2
# Класс Book для объекта книги
class Book:

  # Задание заголовка, автора и года при инициализации
  def __init__(self, title: str, author: str, year: str):
    self.title = title
    self.author = author
    self.year = year

  # получение заголовка, автора и года
  def info(self) -> str:
    return f'{self.title} - {self.author} ({self.year})'

class Ebook(Book):

  # вызов метода инициализации из род класса и определение аттр format
  def __init__(self, title: str, author: str, year: str, format: str):
    super().__init__(title, author, year)
    self.format = format

  # Адаптированный (Переделанный) метод info
  def info(self) -> str:
    return f'{self.title} - {self.author} ({self.year}), format - {self.format}'

# Создание объекта класса Book
test_book = Book('Kapital', 'Karl Marks', '19**')
test_ebook = Ebook('EBOOK', 'Lenin', '19**-19**', 'electron')

# Получение информации из объекта
print(test_ebook.info())
```

```python
Task 3
class Book:
    # Задание заголовка, автора и года при инициализации
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    # получение заголовка, автора и года
    def info(self) -> str:
        return f'{self.title} - {self.author} ({self.year})'

    # При строковвом преобразовании вызывает info
    def __str__(self) -> str:
        return self.info()

    # Сравнивает классы объектов и заголовки
    def __eq__(self, other) -> bool:
        return isinstance(other, Book) and self.title == other.title

    # возраст = текущий год - год написания
    @property
    def age(self) -> str:
        return str(2025 - int(self.year))

    # установить год в зависимости от переданного возраста
    @age.setter
    def age(self, value: str) -> str:
        self.year = str(2025 - int(value))

    # Создание объекта из строки
    @classmethod
    def from_string(cls, data) -> dict:
        title, author, year = data.split(';')
        return cls(title, author, year)

class Ebook(Book):
    # вызов метода инициализации из род класса и определение аттр format
    def __init__(self, title: str, author: str, year: str, format: str):
        super().__init__(title, author, year)
        self.format = format

    # Адаптированный (Переделанный) метод info
    def info(self) -> str:
        return f'{self.title} - {self.author} ({self.year}), format - {self.format}'

test_book = Book('EBOOK', 'Lenin', '1969')
test_from_string = Book.from_string('title;anyone;1843')

print(test_from_string == test_book)
```

```python
Task 4
from abc import ABC, abstractmethod


# Абстрактный класс с выводом информации
class Printable:
    # выводит информацию
    @abstractmethod
    def print_info():
        pass

# наследуется от абстрактного класса Printable
class Book(Printable):
    # Задание заголовка, автора и года при инициализации
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    # Получение заголовка, автора и года
    def info(self) -> str:
        return f'{self.title} - {self.author} ({self.year})'

    def print_info(self):
        print(self.info())

    # При строковвом преобразовании вызывает info
    def __str__(self) -> str:
        return self.info()

    # Сравнивает классы и заголовки объектов
    def __eq__(self, other) -> bool:
        return isinstance(other, Book) and self.title == other.title

    # возраст = текущий год - год написания
    @property
    def age(self) -> str:
        return str(2025 - int(self.year))

    # установить год в зависимости от переданного возраста
    @age.setter
    def age(self, value: str) -> str:
        self.year = str(2025 - int(value))

    # Создание объекта из строки
    @classmethod
    def from_string(cls, data) -> dict:
        title, author, year = data.split(';')
        return cls(title, author, year)

# Наследуется от Book
class Ebook(Book):
    # вызов метода инициализации из род класса и определение аттр format
    def __init__(self, title: str, author: str, year: str, format: str):
        super().__init__(title, author, year)
        self.format = format

    # Адаптированный (Переделанный) метод info
    def info(self) -> str:
        return f'{self.title} - {self.author} ({self.year}), format - {self.format}'

test_book = Book('EBOOK', 'Lenin', '1969')
test_from_string = Book.from_string('title;anyone;1843')

test_book.print_info()
```

# Практики

```python
'''Практика 1'''
class Employee:
    # присваивание базовых аттрибутов классу
    def __init__(self, name, age, coef, base_salary):
        self.name = name
        self.age = age
        self.coef = coef
        self.base_salary = base_salary
    
    # Метод для получения зарплаты
    def salary(self):
        return self.base_salary * self.coef
    
# Наследуется от Employee
class Manager(Employee):
    # Определение аттрибутов класса
    def __init__(self, name, age, coef, base_salary, bonus):
        super().__init__(name, age, coef, base_salary)
        self.bonus = bonus

    # Переопределение метода salary
    def salary(self):
        return self.base_salary * self.coef + self.bonus
    
class Developer(Employee):
    # Определение аттрибутов класса
    def __init__(self, name, age, coef, base_salary, bonus):
        super().__init__(name, age, coef, base_salary)
        self.bonus = bonus
    
    # Переопределение метода salary
    def salary(self):
        return self.base_salary * self.coef + self.bonus
    
emp = Employee('Ivan', 25, 1.5, 1000)
manager = Manager('Lena', 23, 1.3, 500, 10000)
developer = Developer('Igor', 20, 15, 10000, 100000)

print(emp.salary())
print(manager.salary())
print(developer.salary())
```

```python
'''Практика 2'''
class Transport:
    def __init__(self, speed):
        self.speed = speed

    def info(self):
        return f'Объект класса транспорт с максимальной скоростью {self.speed} км/ч'

# Наследуется от Transport и содержит инфо о машине
class Car(Transport):
    def __init__(self, speed, color, model):
        super().__init__(speed)
        self.color = color
        self.model = model

    def info(self):
        return f'Объект класса машина с максимальной скоростью {self.speed} км/ч, цвет {self.color}, модель {self.model}'

# Наследуется от Transport и содержит инфо о автобусе
class Bus(Transport):
    def __init__(self, speed, color, capacity):
        super().__init__(speed)
        self.color = color
        self.capacity = capacity

    def info(self):
        return f'Объект класса автобус с максимальной скоростью {self.speed} км/ч, цвет {self.color}, вместимость {self.capacity} человек'

# Наследуется от Transport и содержит инфо о поезде
class Train(Transport):
    def __init__(self, speed, company):
        super().__init__(speed)
        self.company = company

    def info(self):
        return f'Объект класса поезд с максимальной скоростью {self.speed} км/ч, компания {self.company}'

# Функция для вызова метода info из переданного объекта    
def getInfo(obj):
    return obj.info()

# Создание объектов
transport = Transport(100)
car = Car(150, 'red', 'BMW')
bus = Bus(80, 'blue', 50)
train = Train(90, 'Gazprom')

# Вызов метода info для каждого объекта и вывод результата
for obj in [transport, car, bus, train]:
    print(getInfo(obj))
```

```python
'''Практика 3'''
from decimal import Decimal


# класс для единицы продукта
class Product:
    def __init__(self, name: str, price: Decimal, is_available: bool, category: str):
        self.name = name
        self.price = price
        self.is_available = is_available
        self.category = category

    # метод для вывода информации о продукте
    def __str__(self):
        return f'Product: {self.name}, price: {self.price}, is_available: {self.is_available}, category: {self.category}'

# класс для корзины
class Shopping_cart:
    def __init__(self, products: list[dict]):
        # products = [
        #     {
        #         'count': 2,
        #         'product': Product(
        #             name='Product 1',
        #             price=100,
        #             is_available=True,
        #             category='Category 1'
        #          )      
        #     }
        # ]
        self.products = products

    # метод для добавления продукта в корзину
    def add_Product(self, added_product: Product) -> str:
        for product in self.products:
            if product['product'] == added_product:
                product['count'] += 1
                return 'amount increased'
        
        self.products.append({
            'count': 1,
            'product': added_product
        })
        return 'Added new product'
    
    # метод для изменения количества продукта в корзине
    def set_count_product(self, product: Product, count: int) -> str:
        for exist_product in self.products:
            if exist_product['product'] == product:
                exist_product['count'] = count
                return 'count changed'
        
        self.products.append({count: count, 'product': product})
        return 'Added new product with count'

    # метод для удаления продукта из корзины
    def remove_Product(self, removed_product: Product) -> str:
        for product in self.products:
            if product['product'] == removed_product:
                product['count'] -= 1
                return 'amount decreased'
                break
        else:
            return 'Product not found'

    # метод для очистки корзины
    def clear(self):
        self.products = []

    # метод для вывода информации о продуктах в корзине
    def get_products_as_str(self):
        return [f"count: {el['count']}, {str(el['product'])}" for el in self.products]
    
    # метод для получения общей стоимости товаров в корзине без учета скидки и налога
    def get_prelim_price(self):
        total_price = 0
        for el in self.products:
            total_price += el['product'].price * el['count']
        return total_price

# класс для заказа
class Order:
    def __init__(self, status: str, price: Decimal, shopping_cart: Shopping_cart, discount: Decimal, tax: Decimal):
        self.status = status
        self.price = price
        self.discount = discount
        self.tax = tax

    # метод для получения общей стоимости заказа c учетом скидки и налога
    def calculate_total_price(self) -> Decimal:
        return self.price * (1 - self.discount) * (1 + self.tax)
    
# класс для покупателя
class Customer:
    def __init__(self, name: str, email: str, address: str, past_orders: list = []):
        self.name = name
        self.email = email
        self.address = address
        self.past_orders = past_orders

# customer = Customer('name', 'testEmail@gmail.com', 'Kalinovskaya 12')

# prod1 = Product('Product 1', 100, True, 'Category 1')
# prod2 = Product('Product 2', 200, True, 'Category 2')
# prod3 = Product('Product 3', 300, True, 'Category 3')

# list_of_products = [
#     {'product': prod1, 'count': 2}, 
#     {'product': prod2, 'count': 1}
# ]

# shopping_cart = Shopping_cart(list_of_products)

# print(shopping_cart.get_products_as_str())

# shopping_cart.add_Product(prod2)
# print(shopping_cart.get_products_as_str())

# shopping_cart.remove_Product(prod2)
# print(shopping_cart.get_products_as_str())

# order = Order('in proccess', shopping_cart.get_prelim_price(), shopping_cart, 0.1, 0.2)
# print(order.calculate_total_price())
```
