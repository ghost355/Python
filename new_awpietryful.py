#/usr/bin/env python3
# Программа случайной генерации текста из словаря
# Pavel Pavlov (c) 2016

import random

# Dictonary

articles = ["the", "a", "another", "her", "his"]
subjects = ["cat", "dog", "horse", "man", "woman", "boy", "girl"]
verbs = ["sang", "ran", "jumped", "said", "fought", "swam", "saw",
         "heard", "felt", "slept", "hopped", "hoped", "cried",
         "laughed", "walked"]
adverbs = ["loudly", "quietly", "quickly", "slowly", "well", "badly",
           "rudely", "politely"]

lines = 5 # Кол-во строк

while  lines:
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
