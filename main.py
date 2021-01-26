import functions
from random import choice

fileName = ""
dict = None
rounds = [0,0,0]
anfora=list(range(1,21))

def esNumerico(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def DigitarNum(numStr,i):
    copia=numStr
    flag=esNumerico(copia)
    while(not flag):
        print('Lo digitado no es un número. Ingresa un valor válido')
        copia = input(str(i) + ". Ingrese el número de la bola: ")
        flag=esNumerico(copia)
    return int(copia)

def playBingo(color,i):
    number = DigitarNum(input(str(i) + ". Ingrese el número de la bola: "),i)
    if number not in anfora:
        print('Bola repetida, o no existe en el anfora. Ingrese número diferente')
        playBingo(color, i)
    else:
        anfora.remove(number)
        return functions.checkNumber(dict, color, int(number))

def showGanadores(list):
    if len(list) != 0:
        print("\nIdentificador(es) ganador(es):")
        listId = [item.id for item in list]
        print(listId)
        return True
    else:
        print("\nNo hay ganadores")
        return False

fileName = input("\nIngrese el nombre del archivo de cartones: ")
dict = functions.createDict(fileName)

if dict is None:
    print("El archivo", fileName, "no existe")
else:

    option = ""
    ganadores = []
    color = ""

    while option != "4":
        print("""

        ***BINGO 2.0***

        1) Jugar con cartones amarillos
        2) Jugar con cartones azules
        3) Jugar con cartones rojos
        4) Salir
                
        """)

        option = input("Elija una opción: ")

        if option == "1":
            color = "amarillo"
        elif option == "2":
            color = "azul"
        elif option == "3":
            color = "rojo"
        elif option == "4":
            print("¡Gracias por jugar!")
        else:
            print("Entrada no válida")

        if color != "": 
            rounds[int(option)-1]  += 1
            if rounds[int(option)-1] > 1:
                functions.restoreHits(dict,color)

            print("\nHa elegido el color",color)
            if color=="amarillo" or color=="azul":
                for i in range(14):
                    ganadores = playBingo(color,i+1)
            else:
                for i in range(11):
                    ganadores = playBingo(color,i+1)

            if showGanadores(ganadores) is False:
                if (input("\n¿Desea cantar un número más (s/n)? ").lower()) == "s":
                    ganadores = playBingo(color,"adicional")
                   # print(ganadores)
                    showGanadores(ganadores)

            anfora = list(range(1, 21))
            ganadores = []
            color = ""