"""Lab #1"""

# Hello, World
print("Hello, World")


"""Lab #2"""

# Tipos de datos numéricos
print("Python has three numeric types: int, float, and complex")

# Creación de una variable
myValue=1

print(myValue)

print(type(myValue))

print(str(myValue) + " is of the data type " + str(type(myValue)))

# Presentar el tipo de dato flotante
myValue=3.14

print(myValue)

print(type(myValue))

print(str(myValue) + " is of the data type " + str(type(myValue)))

# Definir el tipo de dato complejo
myValue=5j

print(myValue)

print(type(myValue))

print(str(myValue) + " is of the data type " + str(type(myValue)))

# Definir el tipo de dato booleano
myValue=True

print(myValue)

print(type(myValue))

print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=False

print(myValue)

print(type(myValue))

print(str(myValue) + " is of the data type " + str(type(myValue)))

# Presentar el tipo de dato de cadena
myString = "This is a string."
print(myString)

print(type(myString))

# Para combinar números y texto, utilice la función integrada str()
print(myString + " is of the data type " + str(type(myString)))

"""Lab #3"""
# Trabajando con el tipo de dato de cadena

# Concatenación de cadenas
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? ")

print(name)

# Dar formato a las cadenas de salida
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))

"""Lab #4"""
# Trabajando con listas, tuplas y diccionarios

# Definición del tipo de dato de lista
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

# Acceso a una lista por posición
print(myFruitList[0])

print(myFruitList[1])

print(myFruitList[2])

# Modificación de los valores de una lista
myFruitList[2] = "orange"

print(myFruitList)

# Definición del tipo de dato de tupla
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

# Acceso a una tupla por posición
print(myFinalAnswerTuple[0])

print(myFinalAnswerTuple[1])

print(myFinalAnswerTuple[2])

# Presentar el tipo de dato de diccionario
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)

# Acceso al diccionario por nombre
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])

print(myFavoriteFruitDictionary["Saanvi"])

print(myFavoriteFruitDictionary["Paulo"])

"""Lab #5"""
# Clasificación de valores
# Crear una lista de varios tipos
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))