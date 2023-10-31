# aws_restart
Repositorio de Cloud Computing - AWS re/Start 
Amazon Web Services Bootcamp en colaboración CodingDogo

# Información general sobre los laboratorio

# python-cloud9

Bienvenido a la introducción a la programación. 

Para los laboratorios, utilizará el lenguaje de programación Python.

Nota: La extensión de los archivos en Python es .py.

# Lab.#1: Creación de un programa Hello, World

En este laboratorio, escribirá su primer programa en Python.

# Ejercicio 1: Presentar Python

Python es un lenguaje de programación de uso general y alto nivel. Los lenguajes de programación se utilizan con el objetivo de escribir instrucciones para las computadoras. Alto nivel significa que los comandos de Python se escriben como una combinación de palabras en inglés y símbolos especiales. De uso general significa que muchas personas utilizan Python para diferentes tipos de aplicaciones, como aplicaciones de escritorio y sitios web.

Python tiene dos versiones principales en uso hoy en día. Estas versiones se conocen como Python versión 2.x y Python versión 3.x. Para la Introducción a la programación, utilizará Python versión 3.6.x. La compatibilidad con versiones anteriores significa que el código heredado seguirá funcionando en nuevas versiones del lenguaje. En general, Python sigue siendo compatible con versiones secundarias. Sin embargo, las versiones principales presentan incompatibilidades de sintaxis entre ellas, como entre Python versión 2.x y Python versión 3.x.

El sitio web python.org contiene los instaladores y la documentación general sobre Python.

La mayoría de los sistemas ya tendrán una o más versiones de Python instaladas, con Python versión 2.7 como la predeterminada.

    Para confirmar la versión predeterminada de Python que está instalada en su laboratorio, en la pestaña del terminal abierta, escriba lo siguiente:

    python --version

    Para comprobar cuáles son las demás versiones disponibles de Python, escriba los siguientes comandos:

    python2 --version
    python3 --version

# Ejercicio 2: Escribir su primer programa en Python

Proporcione un nombre adecuado para el archivo de ejercicio (por ejemplo, hello-world.py)

# Lab.#2: Trabajo con tipos de datos numéricos

Python simplifica las matemáticas. De hecho, Python es un lenguaje popular entre los científicos de datos, quienes deben analizar grandes cantidades de datos. En este laboratorio, explorará los tipos de datos básicos que se utilizan para almacenar valores numéricos.

En este laboratorio, deberá realizar lo siguiente:

    utilizar el shell de Python
    utilizar el tipo de dato int (entero)
    utilizar el tipo de dato float (flotante)
    utilizar el tipo de dato complex (complejo)
    utilizar el tipo de dato bool (booleano)

# Ejercicio 1: Utilizar el shell de Python

En la pestaña del terminal, se puede iniciar un shell de Python escribiendo el siguiente comando: python3                                       

Los tres símbolos para “mayor que” (>>>) representan el símbolo del sistema donde el usuario puede escribir comandos de Python. En las siguientes actividades, practicará el uso del shell de Python mediante algunos comandos numéricos.
Escriba la siguiente entrada:
      *    Adición            2 + 2
      *    Sustracción        4 - 2
      *    Multiplicación     2 * 2
      *    División           4 / 2

Para salir del shell de Python, escriba el siguiente comando: quit()

# Ejercicio 2: Presentar el tipo de dato entero

Para obtener más información sobre los tipos de datos, utilizará algunas funciones integradas. Una función es un fragmento de código reutilizable con un nombre. Utiliza una función mediante las siguientes acciones:

    *    Llamarla por su nombre
    *    Incluir una lista de una o más entradas llamadas argumentos, que se encuentran entre paréntesis

Python tiene varias funciones integradas que puede utilizar para escribir programas más útiles.

Un conjunto de funciones se denomina biblioteca. El conjunto de funciones integradas de Python se denomina Biblioteca estándar de Python.
Edición de un archivo en Python

En vez de escribir los comandos uno por uno en el shell de Python, editará un archivo de texto que contiene una secuencia de comandos.
  
# Creación de una variable

Una variable es como una caja etiquetada que almacena información. Puede cambiar el contenido de la caja, pero la etiqueta seguirá siendo la misma. En esta actividad, utilizará el nombre de variable myValue, pero almacenará diferentes tipos de datos en esa caja etiquetada.

# Ejercicio 3: Presentar el tipo de dato flotante

El tipo de dato entero solo almacena números enteros. Si desea almacenar un número con decimales, como 3.14, necesita un nuevo tipo de dato denominado flotante.

Para escribir el valor de la variable en el shell, utilice la función print()
Obtenga el tipo de dato en la variable con la función integrada type()
Para combinar números y texto, utilice la función integrada str():

# Ejercicio 4: Presentar el tipo de dato complejo

En la matemática avanzada, un número imaginario es un número complejo, el cual se puede escribir como un número real que se multiplica por la unidad imaginaria i. El tipo de dato complejo es complicado porque tiene que representar una letra y un número, como 5j.

# Ejercicio 5: Presentar el tipo de dato booleano

El tipo de datos bool (booleano) comprende los nombres permanentes True (Verdadero) y False (Falso), que se representan mediante los numerales 1 y 0, donde 1 = Verdadero y 0 = Falso. El tipo de dato booleano se implementa como un subconjunto de los enteros y no se considera un tipo de dato real. Sin embargo, en algunos lenguajes de programación, se implementa como un tipo de dato diferente. Estos ejercicios denominan al tipo booleano de Python un tipo de dato simulado.

Ha aprendido acerca de los tres tipos de datos numéricos de Python: entero, flotante y complejo. Además, recibió información introductoria sobre el tipo de dato simulado de Python denominado booleano. 
Tenga en cuenta que el tipo booleano corresponde, en realidad, a los números 0 y 1, que representan los valores True (Verdadero) y False (Falso).

# Lab #3: Presentar el tipo de dato booleano

En Python, un conjunto de letras y símbolos se denomina cadena. Las cadenas se suelen utilizar en Python para la entrada y la salida.

En este laboratorio, deberá realizar lo siguiente:

    escribir código Python que utilice el tipo de dato de cadena
    concatenar cadenas
    utilizar un string para solicitar datos de entrada
    dar formato a cadenas para la salida

# Ejercicio 1: Presentar el tipo de dato de cadena

Se denomina script a un archivo de texto que contiene una secuencia lógica de comandos.

En el archivo, escriba el siguiente código:

    Amplíe el script de Python con la función integrada type() para obtener el tipo de dato de la variable. 
    
    Escriba el siguiente código: print(type(myString))

    Para convertir el valor de retorno del tipo en una cadena, utilice la función integrada str():

    print(myString + " is of the data type " + str(type(myString)))

# Ejercicio 2: Trabajar con concatenación de cadenas

La concatenación de cadenas es el proceso por el cual se combinan dos cadenas para formar una sola. De hecho, ha estado realizando concatenaciones de cadenas desde el laboratorio 1. Sin embargo, simplemente no se refería a este proceso con ese término. El símbolo “+” se emplea para concatenar cadenas. Cuando se utiliza el símbolo “+” con cadenas, funciona de una forma distinta a cuando se utiliza con números. En el laboratorio 1, utilizó el signo más “+” para sumar números. Ahora, utilizará el signo más “+” para combinar o concatenar cadenas.

Cree dos cadenas y, luego, concaténelas escribiendo el siguiente código:

    firstString = "water"
    secondString = "fall"
    thirdString = firstString + secondString
    print(thirdString)

# Ejercicio 3: Trabajar con cadenas de entrada

En la codificación, la información que escribe un usuario se conoce como entrada. Utilizará una función integrada denominada input() para obtener información del usuario. La función input() detendrá el código hasta que un usuario escriba una cadena y presione ENTER (Intro). 

Regrese al script en Python y escriba el siguiente código:

    name = input("What is your name? ")

Utilice la función print() para escribir el valor de la variable en el shell:

    print(name)

# Ejercicio 4: Dar formato a las cadenas de salida

Cuando un script busca comunicar información al usuario, se denomina salida. Ha estado utilizando la función print() para escribir la salida en el shell. Creará una encuesta y enviará la información recopilada de vuelta al usuario.

Regrese al script en Python y escriba el siguiente código:

    color = input("What is your favorite color?  ")
    animal = input("What is your favorite animal?  ")

Ha estado utilizando la función print() con una sola variable, pero también se puede usar con múltiples variables para dar formato a una cadena. Escriba el siguiente código:

    print("{}, you like a {} {}!".format(name,color,animal))

La instrucción final print() utiliza la función format(). En la función format(), las llaves de apertura y cierre “{}” actúan como marcadores de posición para las variables que se transmitirán, es decir, se ubicarán entre los paréntesis de la función.

Ha utilizado Python para concatenar cadenas, recibir entradas del usuario y generar una salida en cadena con formato.

# Lab. #4:Trabajando con listas, tuplas y diccionarios

En Python, los tipos de datos numéricos y de cadena se suelen utilizar en grupos denominados colecciones. La lista, la tupla y el diccionario son tres de estas colecciones compatibles con Python.

En este laboratorio, deberá realizar lo siguiente:

    utilizar el tipo de dato de lista
    utilizar el tipo de datos de “tupla” (tuple)
    utilizar el tipo de dato de diccionario

# Ejercicio 1: Presentar el tipo de dato de lista
Acceso al IDE de AWS Cloud9

# Definición de una lista

En esta actividad, editará un script en Python para almacenar una colección de nombres de frutas o una lista.

# Acceso a una lista por posición

En los lenguajes de programación, el posicionamiento en una lista comienza en el cero (0). Los corchetes indican a Python qué posición en la lista desea. Para acceder a la cadena apple, escriba el siguiente código:
Puede acceder al contenido de una lista por su posición. En esta actividad, mostrará cada elemento de nuestra lista por su posición.

Para acceder a la cadena cherry, escriba el siguiente código: print(myFruitList[2])

Los valores de una lista se pueden cambiar. En esta actividad, cambiará cherry por orange.

    En Python, el posicionamiento en la lista comienza en cero (0), por lo que tiene que utilizar el número 2 para acceder a la tercera posición. 
    Escriba el siguiente código: myFruitList[2] = "orange"

# Ejercicio 2: Presentar el tipo de dato de tupla

# Definición de una tupla
Una tupla es similar a una lista, pero no se puede cambiar. Un tipo de dato que no se puede cambiar después de su creación se conoce como inmutable. Para definir una tupla, se utilizan paréntesis en lugar de corchetes ([]).

    # Cree una tupla escribiendo el siguiente código:
    
    myFinalAnswerTuple = ("apple", "banana", "pineapple")
    print(myFinalAnswerTuple)
    print(type(myFinalAnswerTuple))

    # Acceso a una tupla por posición

Al igual que con una lista, también se puede acceder a los elementos de una tupla por su posición:

    Para acceder a la cadena apple, escriba el siguiente código: print(myFinalAnswerTuple[0])

# Ejercicio 3: Presentar el tipo de dato de diccionario

# Definición de un diccionario. 
Un diccionario es una lista cuyas posiciones tienen nombres asignados (claves). Imagine que su lista muestra la fruta favorita de distintas personas.

Regrese al script en Python y escriba el siguiente código:

    myFavoriteFruitDictionary = {
      "Akua" : "apple",
      "Saanvi" : "banana",
      "Paulo" : "pineapple"
    }
    Utilice la función print() para escribir el diccionario en el shell: print(myFavoriteFruitDictionary)

    Utilice la función type() para escribir el tipo de dato en el shell: print(type(myFavoriteFruitDictionary))
  
# Acceso al diccionario por nombre

En esta actividad, en lugar de utilizar números, recurrirá al nombre de las personas para acceder a su fruta favorita.

    Para acceder a la fruta favorita de Akua, escriba el siguiente código:

    print(myFavoriteFruitDictionary["Akua"])

Ha trabajado con los tipos de datos de lista, tupla y diccionario en Python.

#Lab. #5: Clasificación de valores

Con Python, puede mezclar tipos en una lista. En este laboratorio, creará una lista con diferentes tipos e imprimirá los valores.

En este laboratorio, deberá realizar lo siguiente:

    utilizar tipos de datos numéricos
    utilizar tipos de datos de texto (cadena o string)
    utilizar el tipo de dato de lista
    utilizar un bucle for
    utilizar una función print()

# Ejercicio 1: Crear una lista de varios tipos

Puede mezclar tipos de datos en una lista de Python. En otros lenguajes, esta capacidad no es una característica de las listas. En este ejercicio, explorará esta capacidad.

Defina una lista con diferentes tipos, como el siguiente ejemplo: myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

    Utilice una instrucción de bucle for para recorrer la lista e imprimir el tipo de dato de cada elemento en ella:

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))

Este ejercicio reforzó los conceptos de programación de Python que se abordan en los laboratorios 1 a 6. Aunque el código solo tiene unas pocas líneas, es muy eficaz. Dedique un momento a revisarlo y asegúrese de comprender todo lo que sucede en él.

Ha trabajado con el tipo de dato de lista y ha aprendido sobre la compatibilidad de Python con la combinación de tipos de datos en una declaración de lista.

# Lab. #6: Trabajo con tipos de datos compuestos

Un tipo de datos compuesto es cualquier tipo de datos que comprende tipos de datos primitivos. Si le gusta la comida, puede imaginar un tipo de datos compuesto como si fuera turducken, un plato que consiste en pavo relleno con pato que, a su vez, está relleno con pollo. En este laboratorio, creará un tipo de datos que consiste en una cadena que está en un diccionario y que, a su vez, se encuentra en una lista.

En este laboratorio, deberá realizar lo siguiente:

    utilizar tipos de datos numéricos
    utilizar tipos de datos de texto (cadena o string)
    utilizar el tipo de dato de diccionario
    utilizar el tipo de dato de lista
    utilizar un bucle for
    utilizar la función print()
    utilizar la instrucción if
    utilizar la instrucción else
    utilizar la instrucción import

# Creación de datos de un inventario de vehículos

Valores separados por comas (CSV) es un formato de archivo que se utiliza para almacenar datos tabulares, como los datos de una hoja de cálculo. Trabajará con el archivo CSV del siguiente bloque.

Crea y guarde el archivo como car_fleet.csv.

Copie y pegue el siguiente bloque de texto en el archivo car_fleet.csv y guarde el archivo.

    vin,make,model,year,range,topSpeed,zeroSixty,mileage
    TMX20122,AnyCompany Motors, Coupe, 2012, 335, 155, 4.1, 50000
    TM320163,AnyCompany Motors, Sedan, 2016, 240, 140, 5.2, 20000
    TMX20121,AnyCompany Motors, SUV, 2012, 295, 155, 4.7, 100000
    TMX20204,AnyCompany Motors, Truck, 2020, 300, 155, 3.5, 0

Creación de un programa de inventario de vehículos
# Definición del diccionario

Leerá el archivo a través de un módulo denominado csv. Además, realizará una copia profunda de los datos para almacenarlos en la memoria mediante un módulo denominado copy.

Primero, importe los módulos que utilizará:

    import csv
    import copy

    A continuación, defina el diccionario que funcionará como tipo compuesto para leer los datos tabulares:

    myVehicle = {
        "vin" : "<empty>",
        "make" : "<empty>" ,
        "model" : "<empty>" ,
        "year" : 0,
        "range" : 0,
        "topSpeed" : 0,
        "zeroSixty" : 0.0,
        "mileage" : 0
    }

    Utilizará un bucle for para recorrer las claves y valores del diccionario.

for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

    Nota: La función items () pertenece al tipo de datos de diccionario. La función items() indica al bucle for que recorra la colección que pertenece al tipo de datos de diccionario.

    Defina una lista vacía para almacenar el inventario de vehículos que leerá:

myInventoryList = []

# Copia del archivo CSV en memoria

Leerá los datos del disco (disco duro) y realizará una copia en memoria (memoria de acceso aleatorio o RAM). En una computadora, se utiliza un disco duro para almacenar los datos a largo plazo, incluso cuando se apaga la alimentación. La sigla RAM hace referencia a la memoria temporal, que es más rápida, pero se borra cuando se apaga la alimentación de la computadora.

Se le presentará la instrucción de sintaxis with open, que mantiene un archivo abierto mientras lee datos. Cerrará automáticamente el archivo CSV cuando termine de ejecutarse el código dentro del bloque with.

También utilizará una nueva manera de formatear una cadena. En lugar de utilizar comillas dobles y .format para pasar las variables, puede utilizar comillas simples y escribir las variables entre los símbolos “{}”.

Por último, csv.reader() es una función existente en la biblioteca csv, que ya ha importado con la instrucción import csv.

Debería estar familiarizado con la mayor parte del resto del código.

Ahora, regrese al archivo en Python y escriba el siguiente código:

    with open('car_fleet.csv') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')  
        lineCount = 0  
        for row in csvReader:
            if lineCount == 0:
                print(f'Column names are: {", ".join(row)}')  
                lineCount += 1  
            else:  
                print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
                currentVehicle = copy.deepcopy(myVehicle)  
                currentVehicle["vin"] = row[0]  
                currentVehicle["make"] = row[1]  
                currentVehicle["model"] = row[2]  
                currentVehicle["year"] = row[3]  
                currentVehicle["range"] = row[4]  
                currentVehicle["topSpeed"] = row[5]  
                currentVehicle["zeroSixty"] = row[6]  
                currentVehicle["mileage"] = row[7]  
                myInventoryList.append(currentVehicle)  
                lineCount += 1  
        print(f'Processed {lineCount} lines.')

Aunque este código parece una gran cantidad de código para procesar, en su mayoría comprende instrucciones que vio en laboratorios anteriores. Contiene un bucle for con una instrucción if-else, seguido de una instrucción print() al final.

Sin embargo, la siguiente línea necesita una explicación adicional:

    currentVehicle = copy.deepcopy(myVehicle)

De forma predeterminada, Python realiza una copia superficial de tipos de datos complejos. Una copia superficial hace referencia o apunta a la ubicación del almacenamiento de la variable de diccionario myVehicle. Sin esta línea, contaría solo con una única caja de almacenamiento y solo el último elemento de la lista se copiaría en memoria. Esta línea garantiza que se creen nuevas cajas de almacenamiento en memoria para almacenar los nuevos datos tabulares que se están leyendo.
Impresión del inventario de vehículos

Finalizará el script de Python mostrando el inventario de automóviles de la variable myInventoryList.

    Regrese al script en Python y escriba el siguiente código:
    
    for myCarProperties in myInventoryList:
        for key, value in myCarProperties.items():
            print("{} : {}".format(key,value))
            print("-----")
        
Revise una vez más el código que lee los datos tabulares del archivo CSV. Comprender esta sección del código es fundamental para este ejercicio.
Ha trabajado con tipos de datos compuestos en Python.

# Lab. #7: Trabajo con condicionales

Se denomina instrucción condicional a una sección de código que compara dos fragmentos de información. Puede utilizar condicionales para crear diferentes rutas a través del programa. Utilizará los operadores de comparación para escribir un programa que tome decisiones.

En este laboratorio, deberá realizar lo siguiente:

    utilizar la instrucción if
    utilizar la instrucción else
    utilizar la instrucción elif

# Ejercicio 1: Trabajo con la instrucción if

En este ejercicio, deberá editar un script de Python para hacer envíos de paquetes.

    Utilice la función input() para obtener información del usuario: 
    userReply = input("Do you need to ship a package? (Enter yes or no) ")

    Utilice la instrucción if para mostrar una respuesta.

Las instrucciones de una declaración if deben mantener una sangría de un tabulador, debajo de la instrucción if. En otros lenguajes de programación, a menudo se utilizan corchetes ({}) para indicar el inicio y el final de un bloque lógico, pero Python utiliza espaciado:

    if userReply == "yes":
        print("We can help you ship that package!")

# Nota: El símbolo == es un operador de comparación. Significa es igual a.

# Ejercicio 2: Trabajo con la instrucción else

Para mejorar el servicio de atención al cliente, sería una buena idea proporcionar una respuesta, incluso cuando el usuario no desee enviar un paquete. En este ejercicio, mejorará el script de Python mediante la instrucción else:

    Ante la condición de que el usuario no desea enviar un paquete, se utiliza la instrucción else:

    else:
        print("Please come back when you need to ship a package. Thank you.")

# Ejercicio 3: Trabajo con la instrucción elif

En este ejercicio, mejorará el script de Python ofreciendo al usuario servicios adicionales. Cuando tenga varias condiciones, puede utilizar la instrucción elif, que es la abreviatura de else-if.

 # Nota: La instrucción elif siempre va después de la instrucción if y antes de la instrucción else.

    En el script de Python, escriba el siguiente código:

    userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
    if userReply == "stamps":
        print("We have many stamp designs to choose from.")
    elif userReply == "envelope":
        print("We have many envelope sizes to choose from.")
    elif userReply == "copy":
        copies = input("How many copies would you like? (Enter a number) ")
        print("Here are {} copies.".format(copies))
    else:
        print("Thank you, please come again.")

# Nota: Las instrucciones if, elif y else permiten que se ejecute solo una ruta a la vez. El programa no comprueba las demás instrucciones luego de encontrar una condición que es verdadera.

Como puede ver, cada vez que se ha utilizado el programa se han obtenido resultados ligeramente diferentes. Estas diferencias demuestran el poder de los condicionales.
Ha escrito un script de Python que utiliza las instrucciones if, elif y else.

# Trabajo con bucles

Un bucle es un segmento de código que se repite. Aprenderá dos tipos de bucles: el bucle while y el bucle for.

En este laboratorio, deberá realizar lo siguiente:

    utilizar un bucle while
    utilizar un bucle for

# Ejercicio 1: Trabajo con un bucle while

Un bucle while hace que una sección del código se repita hasta que se cumpla una determinada condición. En este ejercicio, creará un script en Python que pedirá al usuario adivinar un número.
Impresión de las reglas del juego

    Utilice la función print() para informar al usuario acerca del juego:

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# Importación aleatoria y escritura de un bucle while

Utilizará el comando import para incluir el código que escribió otra persona. Hasta ahora, ha utilizado funciones integradas. Recuerde que una función es un fragmento de código reutilizable.

    Al inicio del archivo, incluya el módulo de Python (que es un tipo de biblioteca) llamado random.

  #  Nota: Las instrucciones import se colocan al inicio del script por convención.

# import random

    Coloque el cursor en la línea siguiente a la segunda instrucción print(). Luego, escriba una instrucción que generará un número aleatorio entre 1 y 10 mediante el uso de la función randint() del módulo random.

number = random.randint(1,10)

    Monitoree si el usuario adivinó su número con la creación de una variable llamada isGuessRight:

isGuessRight = False

  #  Para gestionar la lógica del juego, cree un bucle while:

    while isGuessRight != True:
        guess = input("Guess a number between 1 and 10: ")
        if int(guess) == number:
            print("You guessed {}. That is correct! You win!".format(guess))
            isGuessRight = True
        else:
            print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

   # Nota: El bucle while repetirá el código dentro del bucle hasta que se adivine el número correcto, lo que está representado por la condición isGuessRight != True en el código. Además, Python utiliza la sangría con espacios para determinar los bloques lógicos, es decir, qué instrucciones se consideran parte del bucle while. Puede poner sangría en una línea si coloca el cursor junto a una instrucción y presiona TAB.

# Escritura de un pseudocódigo

Antes de ejecutar el script en Python, describa la lógica del bucle while en oraciones escritas (sin código). Esta técnica se denomina pseudocodificación.

Por ejemplo:

    Si el usuario no ha adivinado la respuesta correcta, ingrese el bucle.

    Pida al usuario que adivine el número.

    ¿Es el número correcto?

    Si la respuesta es correcta, dígaselo al usuario y salga del bucle.

    Si no ha adivinado el número, indique al usuario que fue una suposición incorrecta y continúe con el bucle.

# Ejecución del script

Ahora ejecute el script en Python y compruebe si funciona.

# Adición de comentarios

Es útil escribir comentarios en el código. Python ignora las líneas de comentarios y comienza con un signo numeral (#). En la mayoría de los teclados, puede crear este símbolo si presiona MAYÚS+3. Agregue sus propios comentarios para que lo ayuden a recordar qué hace el código.
Informe al usuario sobre el script

    Utilice la función print() para informar al usuario sobre lo que hace el script:

    print("Count to 10!")

# Escritura del bucle for

En Python, puede incluir una gran cantidad de funcionalidad en pocas palabras. Esta característica hace que Python sea relativamente fácil de escribir en comparación con otros lenguajes de programación, pero también puede hacer que el código Python sea más difícil de leer. En esta actividad, utilizará la instrucción for, pero también dedicará un poco de tiempo analizándola después de verla en acción.

    Regrese al script en Python. Para contar hasta 10, escriba el siguiente código.

  #  Nota: Python utiliza la sangría para determinar que la instrucción print está dentro de la instrucción del bucle for:

    for x in range (0, 11):
        print(x)

Guarde y ejecute el archivo.

Confirme que el script se ejecuta de forma correcta y que la salida se muestra según lo previsto.

Aquí hay una explicación de lo que sucedió en esas dos líneas. La instrucción for utiliza las palabras clave for … in para indicar a la computadora que recorra la lista. La función range() genera una lista. La función range() toma un número inicial y un número final, pero el número final no está incluido. Por lo tanto, pasa 11 para que la función deje de contar en 10. La letra x actúa como una variable. Cada vez que se ejecuta el bucle, la variable x se asigna a la siguiente variable en el bucle y se muestra en la pantalla.

¡Felicitaciones! Ha trabajado con los bucles while y for en Python.
