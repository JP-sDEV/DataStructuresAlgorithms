"""
    _DoublyLinkedBase will serve as the base class when 
    implementing datas tructures as doubly linked lists
"""
class _DoublyLinkedBase:

    # differs from singly linked list (SLL) by adding prev pointer
    class _Node:

        __slots__ = ("_element", "_prev", "_next")

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    
    # differs from SLL by adding sentinel nodes
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = None
        return element 

# testDLL = HEADER <->TRAILER
testDLL = _DoublyLinkedBase()


"""
    testDLL = HEADER <-> 40 <-> TRAILER

    __len__ = 1
    is_empty() = False
"""
testDLL._insert_between(40, testDLL._trailer, testDLL._header)
print ("Elements in list: {}".format (testDLL.__len__()), "\nList empty: {}\n".format(testDLL.is_empty()))


"""
    testDLL = HEADER <-> TRAILER

    __len__ = 0
    is_empty() = True
"""
testDLL._delete_node(testDLL._header._next)
print ("Elements in list: {}".format (testDLL.__len__()), "\nList empty: {}".format(testDLL.is_empty()))

