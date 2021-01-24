import functions
from random import choice

bombo = [i for i in range(1,21)]
dict = functions.createDict("cartones.csv")

ganadores = None

color=input("¿De qué color es el carton? ").lower()

def Bingo():
    number = input("Dijite el número: ")
    return functions.checkNumber(dict, color, int(number))

if color=="amarillo" or color=="azul":
    for i in range(14):
        ganadores = Bingo()
if color=="rojo":
    for i in range(11):
        ganadores = Bingo()
print(ganadores)

