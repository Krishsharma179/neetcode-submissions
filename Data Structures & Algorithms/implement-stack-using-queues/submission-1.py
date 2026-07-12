class MyStack:

    def __init__(self):
        self.stack1=deque()
        # self.stack2=deque()

    def push(self, x: int) -> None:
        self.stack1.append(x)
        for _ in range(len(self.stack1)-1):
            self.stack1.append(self.stack1.popleft())
  

    def pop(self) -> int:
        
        return self.stack1.popleft()

        

    def top(self) -> int:
        return self.stack1[0]
        

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True 
        else:
            return False     
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()