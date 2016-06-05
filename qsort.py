#!/usr/bin/env python3
# быстрая сортировка

def qsort(L):
    if L:
        sorted_list = qsort([x for x in L if x < L[0]]) + [x for x in L if x == L[0]]+ qsort([x  for x in L if x>L[0]])
        return sorted_list
    return []

raw_list = []
while True:
    number = input ("введите значение для списка или нажмите Enter для вывода упорядочненного списка: ")
    if number:
        raw_list.append(number)
        continue
    break
print ("Исходный список:\n", raw_list)
print ("Упорядочненный список:\n", qsort(raw_list))
