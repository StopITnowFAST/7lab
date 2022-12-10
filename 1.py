#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, найти наименьший элемент и переставить его с
# последним элементом. Преобразованный массив вывести.

if __name__ == '__main__':

    numbers = [int(a) for a in input().split()]

    print("Изначальный список: ", numbers)

    dx = numbers.index(min(numbers))

    buf = numbers[dx]
    numbers[dx] = numbers[len(numbers)-2]
    numbers[len(numbers)-2] = buf

    print("Преобразованный список: ", numbers)
