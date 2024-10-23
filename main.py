from random import choice

# Lambda - function:
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for i in data_set:
                file.write(str(i) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# метод __call__:


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())










# Пример 1 - lambda-функции
# Иногда нужны простые одноразовые функции, для которых def слишком жирно.
# my_func = lambda x: x + 10
#
# print(my_func(x = 42))
# print(type(my_func))

# Пример 2 - лямбда форма может принимать как несколько параметров, так и не одного
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
#
# result = map(lambda x, y: x + y, my_numbers, they_numbers)
# print(list(result))

# Лямбда форма функции имеет ограниченное применение:
# # - Она созадается в процессе выполнения кода ( а не при компиляции) и может просадить быстродействие
# # - Она плохо сериализуется - могут быть проблемы в крупных фреймворках
# # - Не пытайтесь записать в лямбду сложное выражение: если там более 3-5 операторов - пора сделать def

# def get_multiplier_v1(n):
#     if n == 2:
#         def multiplier(x):
#             return x * 2
#     elif n == 3:
#         def multiplier(x):
#             return x * 3
#     else:
#         raise Exception('Я могу сделать умножители только на 2 или 3!')
#
#     return multiplier
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# by_2 = get_multiplier_v1(2)
# by_3 = get_multiplier_v1(3)
#
# result = map(by_2, my_numbers)
# print(list(result))
# result = map(by_3, my_numbers)
# print(list(result))
# # get_multiplier_v1 - функция высшего порядка, она возвращает функции

# def get_multiplier_v2(n):
#
#     def multiplier(x):
#         return x * n
#
#     return multiplier
#
# by_5 = get_multiplier_v2(5)
# print(by_5(x = 42))
#
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# by_10 = get_multiplier_v2(10)
# by_100 = get_multiplier_v2(100)
#
# print(list(map(by_10, my_numbers)))
# print(list(map(by_100, my_numbers)))

# Пример 5 - показатель того, что не стоит передавать аргументы функций изменяемые обьекты и пытаться их замыкать
# from pprint import pprint
#
# def matrix(some_list):
#
#     def multiply_column(x):
#         res = []
#         for element in some_list:
#             res.append(element * x)
#         return res
#
#     return multiply_column
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
#
# matrix_on_my_numbers = matrix(my_numbers)
#
# result = map(matrix_on_my_numbers, they_numbers)
# pprint(list(result))

# Пример 6 - создание объекта, который можно вызывать
#
# class Multiplier:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __call__(self, x):
#         # если есть такой метод у класса - то его объект можно "вызывать" как функцию
#         return x * self.n
#
#
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# by_100500 = Multiplier(n = 100500)
#
# result = by_100500(x = 42)
# print(result)
#
# result = map(by_100500, my_numbers)
# print(list(result))