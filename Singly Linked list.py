class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)

        if index == 0:
            self.prepend(value)
        else:
            count = 0
            current = self.head
            while count<=index - 1:
                current = current.next
                count += 1
            
            news = current.next
            new_node.next = news
            current.next = new_node

    def deleteByNode(self, index):
        count = 0
        current = self.head
        while count<index-1 and current!=None:
            current = current.next
            count += 1
        
        delete = current.next
        aftdel = delete.next
        current.next = aftdel
        del delete

    def display(self):
        if(self.head == None):
            print("Empty")
        else:
            current = self.head
            while current != None:
                print(current.data)
                current = current.next


linkedlist1 = LinkedList()
linkedlist1.prepend(16)
linkedlist1.prepend(17)
linkedlist1.prepend(15)
linkedlist1.prepend(19)
linkedlist1.insert(2,14)
linkedlist1.display()
linkedlist1.deleteByNode(2)
print()
linkedlist1.display()
