# -*- coding: utf-8 -*-
# Esercizio proposto sul gruppo Facebook Python Italia
# Stampa numeri da 1 a 100 e, se il numero è multiplo di 3 stampa Fizz
# Se il numero è multiplo di 5 stampa Buzz e, se è multiplo di entrambi stampa FizzBuzz
# Versione con un solo print

i, m3, m5 = 1, 1, 1
p = ''

while i <= 100:
    if i == m3 * 3 and i == m5 * 5:
        p = 'FizzBuzz'
        m3+=1
        m5+=1
    elif i == m3 * 3:
        p = 'Fizz'
        m3+=1
    elif i == m5 * 5:
        p = 'Buzz'
        m5+=1
    else:
        p = i
    print(p)
    i+=1