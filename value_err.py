#!/usr/bin/env python3
while True:
    x = input ("введите число(или нажмите Enter для завершения): ")
    if not x:
        break
    try:
        print (int(x))
    except ValueError as err:
        print ("ошибка ввода - нужно целое число")
        print (err)
print ("конец программы")
