from Carton import Carton
from random import choice

def createDict(fileName):
    try:
        file = open(fileName, "r")
        dict = {"amarillo": [], "azul": [], "rojo": []}

        for line in file.readlines():
            cleanLine = line.replace("\n", "")
            elements = cleanLine.split(",")

            numbers = makeArr(elements[2::])
            mergeSort(numbers)

            carton = Carton(elements[0], elements[1], numbers)

            dict[carton.color].append(carton)

        file.close()
        return dict
    except:
        return None


def makeArr(list):
    arr = []
    for item in list:
        arr.append(int(item))
    return arr


def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def binarySearch(arr, low, high, x):
    if high >= low:

        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, high, x)

    else:
        return -1


def checkNumber(dict, color, number):
    ganadores = []

    max = 0
    if color == "rojo":
        max = 11
    else:
        max = 14

    arr = dict[color]
    for carton in arr:
        result = binarySearch(carton.numbers, 0, len(carton.numbers) - 1, number)
        if result != -1:
            carton.hits += 1
            if carton.hits == max:
                ganadores.append(carton)
    return ganadores

def generateCartones(c,fileName):
    file = open(fileName,"w")
    colors = ["amarillo","azul","rojo"]
    numbers = [i for i in range(1,21)]
    count = 1
    max = 0
    for i in range(c):
        color = choice(colors)
        if color == "rojo":
            max = 11
        else:
            max = 14

        line = str(count)+","+color
        count += 1

        for item in range(max):
            number = choice(numbers)
            numbers.remove(number)
            line += "," + str(number)
        
        line += "\n"

        file.write(line)

        numbers.clear()
        numbers = [i for i in range(1,21)]
    
    file.close()

