class MinStack:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.min = list()
        self.index = 0

    def push(self, val: int) -> None:            
        if self.min:
            if val<=self.min[self.index]:
                if len(self.min)>self.index+1:
                    self.min[self.index+1] = val
                else:
                    self.min.append(val)
                self.index += 1
        else:
            self.min.append(val)
            
        
        if self.head.next == self.tail:
            self.head.next = Node(val, self.head, self.tail)
            self.tail.prev = self.head.next
        else:
            temp = self.tail.prev
            new = Node(val, temp, self.tail)
            self.tail.prev.next = new 
            self.tail.prev = new

    def pop(self) -> None:
        node = self.tail.prev
        self.tail.prev = node.prev
        self.tail.prev.next = self.tail
        if node.val == self.min[self.index]:
            self.index -= 1
        if self.index == -1:
            self.index = 0
            self.min = list()
            

    def top(self) -> int:
        return self.tail.prev.val
        

    def getMin(self) -> int:
        return self.min[self.index]
            
        
class Node:
    def __init__(self, value=None, prev_node=None, next_node=None):
        self.val = value
        self.next = next_node
        self.prev = prev_node