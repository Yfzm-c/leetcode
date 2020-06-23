#用栈实现队列
"""
使用栈实现队列的下列操作：
push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。

示例:
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);  
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
"""

#难度：简单


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a=[]
        self.b=[]


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.a.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if(len(self.b)==0):
            while(len(self.a)!=0):
                self.b.append(self.a.pop())
        return self.b.pop()




    def peek(self) -> int:
        """
        Get the front element.
        """
        if(len(self.b)==0):
            while(len(self.a)!=0):
                self.b.append(self.a.pop())
        return self.b[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if(len(self.a)==0 and len(self.b)==0 ):
            return True
        return  False

obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.a)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)
