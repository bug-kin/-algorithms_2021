"""
2.*	Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
"""

from collections import defaultdict

# num1 = input('1 число, в 16 формате: ')
# num2 = input('2 число, в 16 формате: ')


def var1(num1='A2', num2="C4F"):
    defdict = defaultdict()
    defdict[num1] = list(num1)
    defdict[num2] = list(num2)
    defdict['sum'] = list(hex(int(num1, 16) + int(num2, 16)))[2:]
    defdict['mul'] = list(hex(int(num1, 16) * int(num2, 16)))[2:]
    print(f'Пользователь ввел значения {num1} и {num2}.\n'
          f'Значения сохранены как {defdict[num1]} и {defdict[num2]}.\n'
          f'Сумма: {defdict["sum"]}. \nПроизведение: {defdict["mul"]}.')
    return ''


class HexNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return f"Сложение: {list(hex(int(self.number, 16) + int(other.number, 16)))[2:]}"

    def __mul__(self, other):
        return f"Произведение: {list(hex(int(self.number, 16) * int(other.number, 16)))[2:]}"

    def __str__(self):
        return f'Введено число {self.number} и преобразовано в {list(self.number)}'


var1()
print('<>'*30)
var2_num1 = HexNumber('A2')
var2_num2 = HexNumber('C4F')
print(var2_num1, var2_num2, sep='\n')
print(var2_num1 + var2_num2)
print(var2_num1 * var2_num2)
