#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# Ввести список А из 10 элементов, найти наименьший элемент и переставить его с
# последним элементом. Преобразованный массив вывести.

if __name__ == '__main__':

    N = 10

    numbers = [int(a) for a in input().split()]
    if len(numbers) != N:
        print("Неправильный размер массива")
        sys.exit()

    print("Изначальный список: ", numbers)

    dx = numbers.index(min(numbers))

    buf = numbers[dx]
    numbers[dx] = numbers[len(numbers)-2]
    numbers[len(numbers)-2] = buf

    print("Преобразованный список: ", numbers)
