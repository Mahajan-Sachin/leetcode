class MyCircularQueue:

    def __init__(self, k: int):
        self.front=0
        self.rear=-1
        self.currentSize=0
        self.cap=k
        self.arr=[0]*k
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear=(self.rear+1)%self.cap
        self.arr[self.rear]=value
        self.currentSize += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front=(self.front+1)%self.cap
        self.currentSize -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front] 
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return self.currentSize==0

    def isFull(self) -> bool:
        return self.currentSize==self.cap



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()