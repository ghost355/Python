#/usr/bin/env python3
# Программа случайной генерации текста из словаря
# Pavel Pavlov (c) 2016

import random

# Dictonary

articles = []
subjects = []
verbs = []
adverbs = []

# Переменные

lines = 5

while  lines:
    # выбираем по случайному слову из каждого раздела словаря
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    # случайно выбираем порядок слов в предложении
    if random.randint (0,1) == 0:
        print (article, subject, verb, adverb)
    else:
        print (article, subject, verb)
