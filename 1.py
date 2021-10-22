# Ввести список А из 10 элементов, найти наименьший элемент и переставить его с
# последним элементом. Преобразованный массив вывести.

numbers = [0]*10
minHere = 10000

for i in range(10):
    numbers[i] = int(input())
    if minHere > numbers[i]:
        minHere = numbers[i]
        id = i

numbers[id] = numbers[9]
numbers[9] = minHere

print(numbers)
