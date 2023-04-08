"""
    This is modul with 4 task  HW 8 Rostyslav Putnikov
"""
# Важно: не использовать циклы для реализации основной логики.
# Нужно использовать рекурсию.
# Цикл можно использовать только в 4 задании для нахождения суммы чисел.

# Напишите рекурсивную функцию, которая принимает одномерный массив
# из 100 целых чисел заполненных случайным образом и находит позицию,
# с которой начинается последовательность из 10 чисел,
# сумма которых минимальна.

import random

my_list = []


def int_unique_gen(some_list, length):
    """
    Recursive function returning a list of random integers
    """
    if length == 0:
        return some_list
    item = random.randint(1, 25)
    if item in some_list:
        return int_unique_gen(some_list, length)
    some_list.append(item)

    return int_unique_gen(some_list, length - 1)


int_unique_gen(my_list, 25)

print("Список уникальных целых чисел:")
print(my_list)
# print(f"Длина списка: {len(my_list)}")
print()

my_dict = dict()


def add_ten(some_list, num):
    """
    A recursive function that returns the index of the number
    from which the sequence of 10 begins, the sum of which is minimal.
    """
    if num == 91:
        return my_dict
    # fmt: off
    value = sum(some_list[num:num + 10])
    # fmt: on
    my_dict[num] = value

    return add_ten(some_list, num + 1)


add_ten(my_list, 0)

print(
    f"Порядковый номер числа, с которого начинается"
    f"последовательность из 10 чисел, сумма которых минимальна: "
    f"{min(my_dict, key=my_dict.get) + 1}"
)
print(f"Индекс этого числа: {min(my_dict, key=my_dict.get)}")
