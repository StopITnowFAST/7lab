#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, найти наименьший элемент и переставить его с
# последним элементом. Преобразованный массив вывести.

if __name__ == '__main__':

    numbers = [0]*10

    for i in range(10):
        numbers[i] = int(input())

    print("Изначальный список: ", numbers)

    num_id = numbers.index(min(numbers))

    buf = numbers[num_id]
    numbers[num_id] = numbers[9]
    numbers[9] = buf

    print("Преобразованный список: ", numbers)
