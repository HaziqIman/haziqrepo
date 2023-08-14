# Assignment 1
# class Stack:
#     def __init__(self):
#         self.s=[]

#     def push(self,value):
#         self.s.append(value)

#     def pop(self):
#         if self.is_empty():
#             print("Stack empty, nothing to pop")
#             return
#         else:
#             return self.s.pop()

#     def is_empty(self):
#         return len(self.s)==0

#     def size(self):
#         return len(self.s)

#     def reverse_stack(self):
#         return self.s.reverse()

#     def peek(self):
#         if self.is_empty():
#             print("Stack empty, nothing to pop")
#             return
#         else:
#             return self.s[-1]

#     def printList(self):
#         if self.is_empty():
#             print("Nothing to print")
#             return
#         else:
#             for i in self.s:
#                 print(i)

# def reverse_list(List):
#     List = Stack()
#     List.reverse_stack()
#     List.printList()


# a = [ins(s) for s in input().split()]
# print(a)
# reverse_list(a)

class Queue:
    Default_Capacity = 10

    def __init__(self):
        self.data = [None] * Queue.Default_Capacity
        self.size = 0
        self.front = 0

    def Size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        if self.size == Queue.Default_Capacity:
            raise Exception("Queue is full")
        rear = (self.front + self.size) % Queue.Default_Capacity
        self.data[rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty:
            raise Exception("Queue is empty")

        front_element = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % Queue.Default_Capacity
        self.size -= 1
        return front_element

que = Queue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
que.enqueue(5)
print(que.dequeue)