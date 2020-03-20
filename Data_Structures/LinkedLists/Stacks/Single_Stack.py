class LinkedStack():

    # Nested _Node class
    class _Node():

        # __slots__ optimize memory usage
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # Stack methods - LIFO

    def __init__(self):
        self._head = None
        self._size = 0
    
    # __len__ -> O(1)
    def __len__(self): 
        return self._size
    
    # is_empty -> O(1)
    def is_empty(self):
        return self._size == 0
    
    # push -> O(1)
    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1
    
    # top -> O(1)
    def top(self):
        if self.is_empty():
            raise ("Stack is Empty")
        else:
            return self._head
    
    # pop -> O(1)
    def pop(self):
        if self.is_empty():
            raise ("Stack is Empty")
        else:
            answer = self._head
            # head pointer assigned to the current head next element
            self._head = self._head._next
            self._size -= 1
            return answer
        