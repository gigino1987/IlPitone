# -*- coding: utf-8 -*-
# Esercizio proposto sul gruppo Facebook Python Italia
# Stampa numeri da 1 a 100 e, se il numero è multiplo di 3 stampa Fizz
# Se il numero è multiplo di 5 stampa Buzz e, se è multiplo di entrambi stampa FizzBuzz
# Versione che implementa la funzione di stampa (print) per ogni condizione

i, m3, m5 = 1, 1, 1

while i <= 100:
    if i == m3 * 3 and i == m5 * 5:
        print('FizzBuzz')
        m3+=1
        m5+=1
    elif i == m3 * 3:
        print('Fizz')
        m3+=1
    elif i == m5 * 5:
        print('Buzz')
        m5+=1
    else:
        print(i)
    i+=1