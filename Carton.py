import BinarySearchTree

class Carton:

    def __init__(self,id,color,numbers):
        self.id = id
        self.color = color
        self.numbers = numbers
        self.hits = 0

    def __str__(self):
        return "{" + str(self.id) + "," + str(self.color) + ","+ str(self.numbers) + "," + str(self.hits) + "}"