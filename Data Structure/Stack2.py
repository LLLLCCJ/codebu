
MAX_SIZE = 5
class Node:
    def __init__(self,data):
        self.data=data
class Stack:
    def __init__(self):
        self.sList=[]
        self.Top=0
        self.tempTop=0
    def push(self,data):
        if not self.is_full():
            newNode=Node(data)
            self.sList.insert(self.tempTop,newNode)
            self.Top+=1
            self.tempTop+=1
        else:
            print("stack overflow")
    def pop(self):
        if not self.is_empty():
            print(self.sList[self.tempTop-1].data)
            self.tempTop-=1
    def is_empty(self):
        return self.tempTop==0
    def is_full(self):
        return self.Top==MAX_SIZE

nemo=Stack()
nemo.push('a')
nemo.push('b')
nemo.push('c')
nemo.push('d')
nemo.pop()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedStack:
    def __init__(self):
        self.head=Node('head')
        self.top=None
    def push(self,data):
        newNode=Node(data)
        curr=self.head
        while curr.next is not None:
            curr=curr.next
        curr.next=newNode
        self.top=newNode
    def pop(self):
        if not self.is_empty():
            curr=self.head
            while curr.next.next is not None:
                curr=curr.next
            print(curr.next.data,end='')
            curr.next=None
            self.top=curr
        else:
            print("stack is empty")
    def is_empty(self):
        return self.head.next==None

    def selectAll(self):
        curr = self.head
        while (curr.next is not None):
            print(curr.data,end='⇨')
            curr=curr.next
        print(curr.data)








from 연결스택 import *

def getPriority(op):
    if op=='+' or op=='-':
        return 1
    elif op=='*' or op=='/':
        return 2

def doing(eq):
    for i in range(len(eq)):
        if eq[i].isdigit():
            print(eq[i],end='')
        else:
            if s.is_empty():
                s.push(eq[i])
            else:
                while (getPriority(s.top.data)>=getPriority(eq[i])):
                    s.pop()
                    if s.is_empty():
                        break
                s.push(eq[i])
    while not s.is_empty():
        s.pop()

s = LinkedStack()
while True:
    eq = input('수식 입력 : ')
    doing(eq)
    print()

