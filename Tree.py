from random import randint
from time import time
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.key = data

def insertion(root, data):
    if root == None:
        return Node(data)
    elif root.key == data:
        return root
    elif root.key>data:
        root.left = insertion(root.left, data)
    elif root.key<data:
        root.right = insertion(root.right, data)
    return root

def minimum(root):
    current = root
    while current.left != None:
        current = current.left
    return current

def deletion(root, value):
    if root == None:
        return root
    if root.key > value:
        root.left = deletion(root.left, value)
    elif root.key < value: 
        root.right = deletion(root.right, value)
    else:
        if root.left == None:
            dels = root.right
            root = None
            return dels
        elif root.right == None:
            dels = root.left
            root = None
            return dels

        dels = minimum(root.right)
        root.key = dels.key
        root.right = deletion(root.right, dels.key)

    return root

# def display(root):
#     if root:
#         display(root.left)
#         print(root.key)
#         display(root.right)

time_insertion = []
time_deletion = []

for i in range(2,11,2):
    root = Node(10)
    start = time()
    for x in range(i*2000):
        insertion(root, randint(1,2000))
    end = time()
    time_insertion.append((end - start)*1000000)

    deleted = 500
    print('number to be deleted is: {}'.format(deleted))
    nstart = time()
    deletion(root, deleted)
    nend = time()
    time_deletion.append((nend - nstart)*1000000)

print(time_insertion)
print(time_deletion)
