#!/usr/bin/env python3
# программа для подсчета списка введеных чисел

count = 0 # инициализация переменных
summ = 0
num_list = []
highest = None # Значение None для присвоения  первого значения как  исходного для сравнения
lowest = None

while True:
        line = input("Input a number or press Enter to finish: ")  # вводим число
        if line:
            try:
                number = int(line)  # переводим в число,проверяем на правильность, присваиваем
            except ValueError as err:
                print(err)
                continue  # после ошибки продолжаем цикл!
            num_list.append(number)
            count += 1
            summ += number
            if highest is None or number >= highest: # сравниваем  на больше меньше и присваиваем нужное значение
                highest = number
            if lowest is None or number <= lowest:
                lowest = number
        else:
             break
if count:
    print ("numbers:",num_list)
    print ("count =", count, "sum =", summ, "lowest =", lowest, "highest  =", highest, "mean =", summ/count)
