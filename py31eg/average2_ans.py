#!/usr/bin/env python3
# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

numbers = []#для списка чисел
indexes = []#для индексов списка чисел
total = 0
lowest = None
highest = None

while True:
    try:
        line = input("enter a number or Enter to finish: ")# вводим числа в список чисел
        if not line:
            break
        indexes.append(len(numbers))    #  добавляем в список индексов длину списка (первый = 0)
        #  так как список пустой еще
        number = int(line)              #  переводим введеное число из строки в целое число
        numbers.append(number)          #  добавляем число в список numbers
        total += number                 #  увеличиваем счетчик введеных чисел
        if lowest is None or lowest > number:
            lowest = number
        if highest is None or highest < number:
            highest = number
    except ValueError as err:
        print(err)

swapped = True #инициализировали переменную цикла
while swapped:
    swapped = False # условие выхода из цикла - если не выполняются условия в цикле for
    for index in indexes:               #  цикл перебором списка индексов
        if index + 1 == len(numbers):   #  цикл прекратится если  достигнуто предпоследнее число в списке
            break
        if numbers[index] > numbers[index + 1]:
            temp = numbers[index]
            numbers[index] = numbers[index + 1]
            numbers[index + 1] = temp
            swapped = True

if numbers:
    index = int(len(numbers) / 2)
    median = numbers[index]
    if index and index * 2 == len(numbers):
        median = (median + numbers[index - 1]) / 2

print("numbers:", numbers)
if numbers:
    print("count =", len(numbers), "total =", total,
          "lowest =", lowest, "highest =", highest,
          "mean =", total / len(numbers), "median =", median)
