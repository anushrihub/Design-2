# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        # defining empty list
        self.queue_list = []

    # method to append the element to the back of the queue
    def push(self, x: int) -> None:
        self.queue_list.append(x)
        
    def pop(self) -> int:
        if self.queue_list:
            pop_element = self.queue_list[0]
            self.queue_list = self.queue_list[1:]
            return pop_element
    
    def peek(self) -> int:
        return self.queue_list[0]

    def empty(self) -> bool:
        return not self.queue_list


# Your MyQueue object will be instantiated and called as such:

obj = MyQueue()
obj.push(2)
obj.push(3)
obj.push(4)
param_2 = obj.pop()
print(param_2)
param_5 = obj.pop()
print(param_5)
param_3 = obj.peek()
print(param_3)
param_4 = obj.empty()
print(param_4)