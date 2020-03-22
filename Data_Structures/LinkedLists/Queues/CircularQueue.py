class CircularQueue:
    
    # Nested _Node class
    class _Node:

        __slots__ = ("_element", "_next")

        def __init__ (self, element):
            self._element = element
            self._next = None
    
    # Circular Queue methods - FIFO

    def __init__(self):
        self._tail: None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    # since circular, tail._next points to head of queue
    def first(self):
        if self.is_empty():
            raise ("Queue is Empty")
        return self._tail._next._element
    
    def dequeue(self):
        if self.is_empty():
            raise ("Queue is Empty")
        answer = self._tail._next
        self._tail._next = answer._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
        

    def enqueue(self, e):
        newest = self._Node(e)
        if self.is_empty():
            # point first node to itself, initialize circular structure
            newest._next = newest
        else:
            newest._next = self._tail._next 
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    

    """
    move tail node to the head of the list
    can be used in a round-robin scheduler
    """
    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next

test = CircularQueue()
# test = 1 -> 44 -> 9 -> 10 -> 7
test.enqueue(1)
test.enqueue(44)
test.enqueue(9)
test.enqueue(10)
test.enqueue(7)
# test.first() -> 1
print (test.first())
print (test.__len__())

before = test.__len__()
test.dequeue()
after = test.__len__()
print ("before: {}\nafter: {}".format(before, after))


