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

    # get first element of the queue, does not remove it
    def first(self):
        if self.is_empty():
            raise ("Queue is Empty")
        return self._data[self._front]

    # get first element from the queue, remove it
    def dequeue(self):
        if self.is_empty():
            raise ("Queue is Empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        # save memory if currernt queue can fit in 1/4 of data length
        if 0 < self._size < len(self._data) // 4:
            self.resize(len(self._data) // 2)
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self.resize(2 * self._data)
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        # reset front pointer after copying queue to larger array
        self._front = 0


testQ = ArrayQueue()
# testQ = [12, 3, 14, ... None]
testQ.enqueue(12)
testQ.enqueue(3)
testQ.enqueue(14)
# testQ = [None, 3, 14, ... None]
testQ.dequeue()
# testQ.first = 3
print(testQ.first())
