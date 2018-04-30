#! python3.6

# Esercizio proposto sul gruppo Facebook Python Italia
# Stampa numeri da 1 a 100 e, se il numero è multiplo di 3 stampa Fizz
# Se il numero è multiplo di 5 stampa Buzz e, se è multiplo di entrambi stampa FizzBuzz
# Versione con un solo print

for i in range(1, 101):
    print(f"{i}{'' if i % 3 else 'Fizz'}{'' if i % 5 else 'Buzz'}")
