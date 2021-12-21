class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.front=None
class CircleLinkedList:
    def __init__(self):
        self.head=Node("head")
        self.tail=Node("tail")
        self.cnt=0
        self.head.next=self.tail
        self.tail.front=self.head
    def append(self,data):
        newNode=Node(data)
        curr=self.head
        for i in range(self.cnt):
            curr=curr.next
        newNode.front=curr
        newNode.next=curr.next
        curr.next.front=newNode
        curr.next=newNode
        self.cnt+=1
    def insert(self,idx,data):
        newNode=Node(data)
        if idx>(self.cnt/2):
            curr=self.head
            for i in range(idx-1):
                curr=curr.next
        if idx<(self.cnt/2):
            curr=self.tail
            for i in range(self.cnt-idx+1):
                curr=curr.front
        newNode.front=curr
        newNode.next=curr.next
        curr.next.front=newNode
        curr.next=newNode
        self.cnt+=1
    def asc(self):
        curr=self.head
        for i in range(self.cnt):
            curr=curr.next
            print(curr.data,end=' ')
    def desc(self):
        curr=self.tail
        for i in range(self.cnt):
            curr=curr.front
            print(curr.data,end=' ')
    def show(self):
        curr=self.head
        for i in range(self.cnt):
            curr=curr.next
            print(curr.data,end=' ')
