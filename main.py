import functions
from random import choice

bombo = [i for i in range(1,21)]
dict = functions.createDict("cartones.csv")

ganadores = None
for i in range(14):
    number = choice(bombo)
    bombo.remove(number)
    ganadores = functions.checkNumber(dict,"amarillo",number)

print(ganadores)

