"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

from collections import namedtuple, deque

firm = namedtuple("Firm", ['name', 'income'])


def statistic():
    quantity = int(input('Введите количество предприятий для расчета прибыли: '))
    common_sum = 0
    avg = 0
    f_deq = deque([])
    firms = [reg_firm(
        input('Введите название предприятия: '),
        input('Через пробел введите прибыль за каждый квартал года: '))
        for _ in range(quantity)]
    for unit in firms:
        common_sum += unit.income
        avg = common_sum / len(firms)
    for unit in firms:
        if unit.income > avg:
            f_deq.appendleft(unit.name)
        else:
            f_deq.append(unit.name)
    return common_sum, avg


def reg_firm(name, income):
    return firm(name, sum(map(int, income.split())))


print(statistic())
