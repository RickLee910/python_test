class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftchild = None
        self.rightchild = None

    def insertLeft(self, newNode):
        if self.leftchild == None:
            self.leftchild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftchild = self.leftchild
            self.leftchild = t


    def insertRight(self, newNode):
        if self.rightchild == None:
            self.rightchild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightchild = self.leftchild
            self.rightchild = t

    def getLeftChild(self):
        return self.leftchild

    def getRightChild(self):
        return self.leftchild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')
r.getLeftChild()
r.setRootVal('hello')
r.getLeftChild().insertRight('d')
