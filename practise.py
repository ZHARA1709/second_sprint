class Phone:
    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value


rotary_phone = Phone('дисковый')
keypad_phone = Phone('кнопочный')

# Печать значения атрибута класса.
print(f'Тип линии - {rotary_phone.line_type}')
# Печать значения атрибута объекта.
print(f'Тип набора - {rotary_phone.dial_type}')

rotary_phone.dial_type = 'кнопочный'

print(f'Тип набора - {rotary_phone.dial_type}')

# Печать значения атрибута класса.
print(keypad_phone.line_type)
# Печать значения атрибута объекта.
print(keypad_phone.dial_type)

print(f'Тип линии: {Phone.line_type}')
Phone.line_type = 'беспроводной'
print(f'Тип линии: {Phone.line_type}')

# Создать объект класса Phone.
rotary_phone = Phone(dial_type_value='дисковый')
keypad_phone = Phone(dial_type_value='кнопочный')

# Распечатать значение атрибута класса.
print(f'Тип линии: {rotary_phone.line_type}')
print(f'Тип линии: {keypad_phone.line_type}')

# Поменять значение атрибута line_type для объекта rotary_phone.
rotary_phone.line_type = 'радио'

# Снова распечатать значения.
print(f'Тип линии: {rotary_phone.line_type}')
print(f'Тип линии: {keypad_phone.line_type}')

# Поменять значение атрибута класса через класс.
Phone.line_type = 'спутниковый'

# Снова распечатать значения.
print(f'Тип линии: {rotary_phone.line_type}')
print(f'Тип линии: {keypad_phone.line_type}')