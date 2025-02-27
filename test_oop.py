# Импортируйте нужную библиотеку.
"""
from datetime import datetime

class Store:
    def __init__(self, address):
        self.address: str = address

    def __is_open(self, date) -> bool:
        # Метод __is_open() в родительском классе всегда возвращает False,
        # это "код-заглушка", метод, предназначенный для переопределения
        # в дочерних классах.
        # Не переопределяйте содержимое этого метода.
        return False

    def get_info(self, text_date) -> str:
        # С помощью шаблона даты преобразуйте строку date_str в объект даты:
        date_object = datetime.strptime(text_date, '%d.%m.%Y')

        # Передайте в метод __is_open() объект даты date_object и определите,
        # работает ли магазин в указанную дату.
        # В зависимости от результата будет выбрано значение
        # для переменной info.
        if self.__is_open(date_object):
            info = 'работает'
        else:
            info = 'не работает'
        return f'Магазин по адресу {self.address} {text_date} {info}'


class MiniStore(Store):
    # Переопределите метод __is_open().
    # Обратите внимание на имя метода/name mangling
    def _Store__is_open(self, date: datetime) -> bool:
        if date.weekday() in [0, 1, 2, 3, 4]:
            return True
        else:
            return False


class WeekendStore(Store):
    # Переопределите метод __is_open().
    # Обратите внимание на имя метода/name mangling
    def _Store__is_open(self, date: datetime) -> bool:
        if date.weekday() in [5, 6]:
            return True
        else:
            return False


class NonStopStore(Store):
    # Переопределите метод __is_open().
    # Обратите внимание на имя метода/name mangling
    def _Store__is_open(self, date: datetime) -> bool:
        return True


mini_store = MiniStore('Улица Немига, 57')
print(mini_store.get_info('29.03.2024'))
print(mini_store.get_info('30.03.2024'))

weekend_store = WeekendStore('Улица Толе би, 321')
print(weekend_store.get_info('29.03.2024'))
print(weekend_store.get_info('30.03.2024'))

non_stop_store = NonStopStore('Улица Арбат, 60')
print(non_stop_store.get_info('29.03.2024'))
print(non_stop_store.get_info('30.03.2024'))

"""


class Customer:
    def __init__(self, name: str):
        self.name = name
        # Добавьте сюда приватный атрибут "скидка"
        # со значением по умолчанию 10.
        self.__discount = 10

    # Метод set_discount() принимает на вход
    # новое значение для приватного атрибута "скидка".
    # Если new_value превышает 80 -
    # новое значение скидки должно стать 80.
    # Метод не должен ничего возвращать.
    def set_discount(self, new_value: int):
        if new_value >= 80:
            self.__discount = 80
        else:
            self.__discount = new_value

    # Метод get_price() получает на вход исходную стоимость товара
    # и должен вернуть новую цену товара с учётом
    # скидки покупателя.
    # Возвращаемое значение округлите до двух знаков после запятой.
    def get_price(self, price: int) -> float:
        price = price * ((100 - self.__discount) / 100)
        return round(price, 2)


# Проверим работу программы.
# Создаём объект покупателя:
customer = Customer('Иван Иванович')

original_price = 85

print(
    f'С исходной скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)
# Изменим скидку до неприемлемого уровня.
# Метод set_discount() должен установить размер скидки равным 80.
customer.set_discount(90)
print(
    f'С новой скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)