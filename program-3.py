"""Lab #8"""
# Trabajando con un bucle while

# Impresión de las reglas del juego
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# Importación aleatoria y escritura de un bucle while
import random

number = random.randint(1,10)

isGuessRight = False

# El bucle while repetirá el código hasta que se adivine el número correcto
# Python utiliza la sangría con espacios para determinar los bloques lógicos, es decir, qué instrucciones se consideran parte del bucle

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        
        