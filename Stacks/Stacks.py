class AraryStack:

    # follow FIFO principle

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise ("Stack is Empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise ("Stack is Empty")
        return self._data.pop()


test_stack = AraryStack()
# test_stack = [23, 1, 98, 45, "hello"]
test_stack.push(23)
test_stack.push(1)
test_stack.push(98)
test_stack.push(45)
test_stack.push("hello")

# stack_top = "hello"
stack_top = test_stack.top()

# test_stack = [23, 1, 98]
test_stack.pop()
test_stack.pop()
test_stack.top()

# stack_top2 = [98]
stack_top2 = test_stack.top()
print(stack_top2)
