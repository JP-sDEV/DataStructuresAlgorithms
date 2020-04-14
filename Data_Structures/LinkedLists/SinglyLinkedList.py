"""
Node class looks like: 
    data|next ->
initially 'next' is none, target depends on where it is inserted
"""

class Node: 

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    """
    New node is placed at the beginning of Linked List, arrows pointing from left to right
    Runtime: O(1)
    """
    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    """
    New node is placed at the end of Linked List, arrows pointing from left to right
    Runtime: O(n)
    """
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

    
    def before_and_end(self):
        end = self.head
        before_end = None

        while end:
            before_end = end
            end = end.next
            print (str("{},{}\n".format(before_end.data, end.data)))
    
    def switch(self):
        end = self.head
        before_end = None
        e3 = None

        while end.next:
            e3 = before_end
            before_end = end
            end = end.next
            print (str("before: {},{}\n".format(before_end.data, end.data)))
            end.next = before_end
            before_end.next = e3
            print (str("after: {},{}\n".format(before_end.data, end.data)))



# llist = 12 -> 3 -> 1 -> 2 -> 90
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
# print(llist.printLList())