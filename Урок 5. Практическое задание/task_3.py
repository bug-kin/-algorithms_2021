"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""
from collections import deque
from timeit import timeit

load = [i for i in range(10)]
just_list = [i for i in range(10000)]
special_deque = deque([i for i in range(10000)])

# Вставка элемента в конец
print('# Вставка элемента в конец')
print(timeit('just_list.append(0)', globals=globals()))
print(timeit('special_deque.append(0)', globals=globals()))
print(len(just_list), len(special_deque))
# Удаление и возврат элементов с конца
print('# Удаление и возврат элементов с конца')
print(timeit('just_list.pop()', globals=globals()))
print(timeit('special_deque.pop()', globals=globals()))
print(len(just_list), len(special_deque))
# Вставка элементов в начало
print('# Вставка элементов в начало')
print(timeit('just_list.insert(0, 0)', globals=globals(), number=100000))
print(timeit('special_deque.appendleft(0)', globals=globals(), number=100000))
print(len(just_list), len(special_deque))
# Удаление и возврат элементов из начала
print('# Удаление и возврат элементов из начала')
print(timeit('just_list.pop(0)', globals=globals(), number=100000))
print(timeit('special_deque.popleft()', globals=globals(), number=100000))
print(len(just_list), len(special_deque))
# Добавление итерируемого объекта
print('# Добавление итерируемого объекта')
print(timeit('just_list.extend(load)', globals=globals(), number=1000))
print(timeit('special_deque.extend(load)', globals=globals(), number=1000))
print(len(just_list), len(special_deque))
print('# Добавление итерируемого объекта в начало')
print(timeit('just_list[:] = load + just_list', globals=globals(), number=1000))
print(timeit('special_deque.extendleft(load)', globals=globals(), number=1000))
print(len(just_list), len(special_deque))
"""
# Вставка элемента в конец
0.1443261
0.0948833
1010000 1010000
# Удаление и возврат элементов с конца
0.09339629999999999
0.0750419
10000 10000
# Вставка элементов в начало
3.0702363
0.007594199999999773
110000 110000
# Удаление и возврат элементов из начала
1.5433470000000002
0.005149100000000573
10000 10000
# Добавление итерируемого объекта
0.00010520000000013852
0.00015369999999936823
20000 20000
# Добавление итерируемого объекта в начало
0.49374619999999947
0.00016449999999945675
30000 30000

Итог: Проведя аналогичные операции для структур Дек и Список можно сказать что Дек
действительно более оптимальный для работ со списками и выполняется намного быстрее,
не считая .extend(), тут Список выигывает.
"""
