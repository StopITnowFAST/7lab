#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, найти наименьший элемент и переставить его с
# последним элементом. Преобразованный массив вывести.

if __name__ == '__main__':

    numbers = [0]*10

    i = 0
    while i < len(numbers):
        numbers[i] = int(input())
        i = i + 1

    print("Изначальный список: ", numbers)

    dx = numbers.index(min(numbers))

    buf = numbers[dx]
    numbers[dx] = numbers[9]
    numbers[9] = buf

    print("Преобразованный список: ", numbers)
