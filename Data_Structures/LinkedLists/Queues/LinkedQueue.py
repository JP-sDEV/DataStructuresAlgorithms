class LinkedQueue:

    # Nested _Node class
    class _Node:

        __slots__ = ("_element", "_next")

        def __init__ (self, element):
            self._element = element
            self._next = None

    # Queue methods - FIFO

    # Queue as a linked list -> include tail pointer
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise ("Queue is Empty")
        return self._head._element
    
    def dequeue(self):
        if self.is_empty():
            raise ("Queue is Empty")
        answer = self._head
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

test = LinkedQueue()
# test = 1 -> 44 -> 9 -> 10 -> 7
test.enqueue(1)
test.enqueue(44)
test.enqueue(9)
test.enqueue(10)
test.enqueue(7)
# test.first() -> 1
print(test.first())

"""
remove first element of the queue, and reassign the header pointer

before -> 5
after -> 4
"""
before = test.__len__()
test.dequeue()
after = test.__len__()
print ("before: {}\nafter: {}".format(before, after))