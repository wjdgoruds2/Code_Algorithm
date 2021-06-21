class MyQueue:
    def __init(self):
        self.input=[]
        self.output=[]
    def push(self,x):
        self.input.append(x)
    def pop(self):
        self.peek() #처음에 있는 요소
        return self.output.pop()
    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
    def empty(self):
        return self.input == [] and self.output == []
