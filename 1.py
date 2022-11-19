#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, найти наименьший элемент и переставить его с
# последним элементом. Преобразованный массив вывести.

if __name__ == '__main__':

    n = 10
    numbers = [0] * n

    numbers = [int(input()) for i in numbers]

    print("Изначальный список: ", numbers)

    dx = numbers.index(min(numbers))

    buf = numbers[dx]
    numbers[dx] = numbers[n-1]
    numbers[n-1] = buf

    print("Преобразованный список: ", numbers)
