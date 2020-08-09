from pythonds.basic import Stack
from pythonds.trees import BinaryTree

def preoder(tree):
    if tree:
        print(tree.getRootVal())
        preoder(tree.getLeftChild())
        preoder(tree.getRightChild())

def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

        