#/usr/bin/env python3
# Программа случайной генерации текста из словаря
# Pavel Pavlov (c) 2016

import random
import sys

# Dictonary
articles = ["the", "a", "another", "her", "his"]
subjects = ["cat", "dog", "horse", "man", "woman", "boy", "girl"]
verbs = ["sang", "ran", "jumped", "said", "fought", "swam", "saw",
         "heard", "felt", "slept", "hopped", "hoped", "cried",
         "laughed", "walked"]
adverbs = ["loudly", "quietly", "quickly", "slowly", "well", "badly",
           "rudely", "politely"]
lines = 5 # default value
if len(sys.argv) > 1: # если длина списка аргументов больше 1, т.е. есть аргументы после имени программы
    try:
        temp = int(sys.argv[1]) # временная переменная для хранения аргумента
        if 1 < temp < 10: # проверка нахождения аргумента от 1 до 10
            lines = temp
        else:
            print("lines must be between 1 and 10")

    except ValueError:
        print ("you need print awfulpoetry3_ans.py [number_of_lines]")
while lines:
    # выбираем по случайному слову из каждого раздела словаря
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    # случайно выбираем порядок слов в предложении
    if random.randint (0,1) == 0:
        print ("-", article, subject, verb, adverb)
    else:
        print ("-",article, subject, verb)
    lines -= 1
