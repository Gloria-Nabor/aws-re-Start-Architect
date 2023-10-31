"""Lab #7"""
# Trabajando con condicionales

# Función input() para obtener información del usuario
userReply = input("Do you need to ship a package? (Enter yes or no) ")

# Instrucción IF
# Las instrucciones debajo de una declaración if deben mantener una sangría de un tabulador 
# if else elif anidados. El programa no comprueba las demás instrucciones luego de encontrar una condición que es verdadera
if userReply == "yes":
    print("We can help you ship that package!")

# Instrucción else    
else:
    print("Please come back when you need to ship a package. Thank you.")
# Instrucción elif    
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