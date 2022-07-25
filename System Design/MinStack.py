class StackNode:
    def __init__(self, val, prev, min):
        self.val = val
        self.prev = prev
        self.min = min

class MinStack:
    def __init__(self):
        self.stack = StackNode(None, None, None)
        self.min = None
        

    def push(self, val: int) -> None:
        if(self.min == None):
            self.min = val
        min = self.min
        if(val < self.min):
            min = val
            self.min = val
        self.stack = StackNode(val, self.stack, min)
        

    def pop(self) -> None:
        self.stack = self.stack.prev
        self.min = self.stack.min
        

    def top(self) -> int:
        return self.stack.val
        

    def getMin(self) -> int:
        return self.stack.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

    
if __name__ == "__main__":
    # answer = []
    # expected = [-3, 0, -2]
    # minStack = MinStack()
    # minStack.push(-2)
    # minStack.push(0)
    # minStack.push(-3)
    # answer.append(minStack.getMin()) # return -3
    # minStack.pop()
    # answer.append(minStack.top())    # return 0 
    # answer.append(minStack.getMin()) # return -2
    answer = []
    expected = [None, None, -3]
    minStack = MinStack()
    minStack.push(2)
    minStack.push(0)
    minStack.push(3)
    minStack.push(0)
    minStack.getMin()
    minStack.pop()
    minStack.getMin()
    minStack.pop()
    minStack.getMin()
    minStack.pop()
    minStack.getMin()
    if(answer == expected):
        print('correct')
    else:
        print('wrong')
