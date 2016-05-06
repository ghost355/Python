#/usr/bin/env python3
# Pavel Pavlov (c) 2016

import random

articles = ["the", "another", "a", "her",  "his"]
nouns = ["man", "women",  "boy",  "cat", "dog"]
verbs = ["goes", "swimed", "cry", "run", "slept"]
adverbs =  ["slowly", "quickly", "loudly", "well"]

current_line = 0 # количество строк по умолчанию
lines = 5

while current_line < int(lines):
    if random.randint(0,1) == 0: # функция как условие, не нужна  отдельная переменная  для результата функции
        print (current_line + 1, random.choice(articles), random.choice(nouns), random.choice(verbs), random.choice(adverbs))
    else:
        print (current_line + 1, random.choice(articles), random.choice(nouns), random.choice(verbs))
    current_line += 1

print ("\nЭто все, ребята!")
