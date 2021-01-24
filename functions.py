from BinarySearchTree import BinarySearchTree
from Carton import Carton

def createDict(fileName):
    file = open(fileName,"r")
    dict = {"amarillo": [], "azul": [], "rojo": []}

    for line in file.readlines():
        cleanLine = line.replace("\n","")
        elements = cleanLine.split(",")
        numbers = elements[2::]

        bst = createBST(numbers)    
        carton = Carton(elements[0],elements[1],bst)

        dict[carton.color].append(carton)

    file.close()
    return dict

def createBST(arr):
    bst = BinarySearchTree(int(arr[0]))
    for item in arr[1::]:
        bst.insert(int(item))
    
    return bst

def checkNumber(dict,color,number):
    ganadores = []
    max = 0
    if color == "rojo":
        max = 11
    else:
        max = 14

    arr = dict[color]
    for carton in arr:
        result = carton.numbers.search(number)
        if result is not None:
            carton.hits+=1
            if carton.hits == max:
                ganadores.append(carton)
    return ganadores
