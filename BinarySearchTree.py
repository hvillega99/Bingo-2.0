class BinaryNode:

    def __init__(self,value):
        self.__value = value
        self.__left = None
        self.__right = None

    def getValue(self):
        return self.__value
    
    def setLeft(self,value):
        self.__left = BinarySearchTree(value)

    def getLeft(self):
        return self.__left
    
    def setRight(self,value):
        self.__right = BinarySearchTree(value)

    def getRight(self):
        return self.__right

    def isLeaf(self):
        return (self.__right is None) and (self.__left is None)
    
    def __str__(self):
        return "{" + str(self.__value) + "}"

class BinarySearchTree:

    def __init__(self,value):
        self.__root = BinaryNode(value)

    def getRoot(self):
        return self.__root

    def setLeft(self,value):
        self.setLeft(value)

    def setRight(self,value):
        self.setRight(value)
    
    def getLeft(self):
        return self.__root.getLeft()
    
    def getRight(self):
        return self.__root.getRight()

    def insert(self,value):
        if self.__root.getValue!=value:
            if value < self.__root.getValue():
                if self.__root.getLeft() is None:
                    self.__root.setLeft(value)
                    return True
                else:
                   return self.__root.getLeft().insert(value)
            else:
                if self.__root.getRight() is None:
                    self.__root.setRight(value)
                    return True
                else:
                   return self.__root.getRight().insert(value)
        return False

    def search(self,value):
        if value == self.__root.getValue():
            return self.__root
        elif value < self.__root.getValue():
            if self.__root.getLeft() is not None:
               return self.__root.getLeft().search(value)
        else:
            if self.__root.getRight() is not None:
                return self.__root.getRight().search(value)
        return None

    def preOrder(self):
        print(self.__root)

        if self.getLeft() is not None:
            self.getLeft().preOrder()

        if self.getRight() is not None:
            self.getRight().preOrder()

    def inOrder(self):
        if self.getLeft() is not None:
            self.getLeft().inOrder()

        print(self.__root)

        if self.getRight() is not None:
            self.getRight().inOrder()

    def postOrder(self):
        if self.getLeft() is not None:
            self.getLeft().postOrder()

        if self.getRight() is not None:
            self.getRight().postOrder()

        print(self.__root)


    def remove(self,value):
        target = self.search(value)

        if target is None:
            return False
        else:

            if target.isLeaf():
                print(target)
                target=None
                print(target)
                return True

            elif (target.getLeft() is None and target.getRight() is not None) or (target.getLeft() is not None and target.getRight() is None):
                
                aux = None
                if target.getLeft() is not None:
                    aux = target.getLeft()
                else:
                    aux=target.getRight()
                target=aux.getRoot()
                aux = None
                return True
            
            else:

                aux = target.getRight()
                while aux.getLeft() is not None:
                    aux = aux.getLeft()

                target = aux.getRoot()
                return True

