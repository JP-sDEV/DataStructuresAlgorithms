class ArrayQueue: 

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return (self._size) == 0
    
    def first(self):
        if self.is_empty():
            raise ("Queue is Empty")
        
        return self._data[self._front]
    
    def dequeue(self):
        if self.is_empty():
            raise ("Queue is Empty")

testQ = ArrayQueue()
print(testQ.first())