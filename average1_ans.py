#!/usr/bin/env python3
# программа для подсчета списка введеных чисел

count = 0 # инициализация переменных
summ = 0
num_list = []
highest = 0
lowest = 0

while True:
        line = input("Input a number or press Enter to finish: ")
        if line:
            try:
                number = int(line)
            except ValueError as err:
                print(err)
                continue
            num_list += line
            count += 1
            summ += number
            if number >= highest:
                highest = number
            if lowest is 0 or number <= lowest:
                lowest = number
        else:
             break
if count:
    print ("numbers:",num_list)
    print ("count =", count, "sum =", summ, "lowest =", lowest, "highest  =", highest, "mean =", summ/count)
