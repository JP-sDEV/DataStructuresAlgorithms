class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def append(self, data):
        newNode = Node(data)
        pointer = self.head
        if self.head == None:
            self.head = newNode
        else:
            while pointer.next:
                pointer = pointer.next
            pointer.next = newNode

    def printLList(self):
        temp = self.head
        print("Printing List...")
        while(temp):
            print(str(temp.data))
            temp = temp.next

    def countNodes(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count


# if __name__ == '___main__':
llist = LinkedList()
llist.append(12)
llist.append(3)
llist.append(1)
llist.append(2)
llist.append(90)

print(llist.printLList())
