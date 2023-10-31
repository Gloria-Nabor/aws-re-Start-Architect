"""Lab #6"""
# Trabajando con tipos de datos compuestos

import csv
import copy

# Definición del Diccionario que funcionará como Tipo Compuesto para leer los datos tabulares
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

# Recorrer claves y valores del diccionario
# Función items() indica al bucle for que recorra la colección que pertenece al tipo de datos de diccionario

for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    
# Define una lista vacía para almacenar el inventario de vehículos que leerá
myInventoryList = []

print("--------")

# Copia del archivo CSV en memoria
# Instrucción with open, mantiene un archivo abierto mientras lee datos y cierra automáticamente el archivo CSV cuando termina de ejecutar el código dentro del Bloque with
# Otro formato de cadena, en vez de comillas dobles y .format para pasar las variables, utilizar comillas simples y escribir las variables entre “{}”
# csv.reader() es una función existente en la biblioteca csv

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
    print("--------")
    
    # Por default solo hay una caja de almacenamiento en memoria por tanto unicamente el último elemento de la lista se copiaría 
    # Esta línea garantiza se creen nuevas cajas para almacenar los nuevos datos tabulares que se están leyendo
    currentVehicle = copy.deepcopy(myVehicle)
    
    # Mostrar el inventario de vehículos de la variable myInventoryList
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")