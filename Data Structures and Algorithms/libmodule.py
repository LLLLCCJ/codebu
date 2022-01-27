class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoubleLinkedList:
    def __init__(self):
        self.head=Node('head')
        self.tail=Node('tail')
        self.head.next=self.tail
        self.tail.prev=self.head
        self.cnt=0
    def append(self,data):
        newNode=Node(data)
        newNode.prev=self.tail.prev
        newNode.next=self.tail
        self.tail.prev.next=newNode
        self.tail.prev=newNode
        self.cnt+=1
    def insert(self,idx,data):
        if idx>self.cnt:
            return
        newNode=Node(data)
        if idx > self.cnt/2:
            curr=self.tail
            for i in range(self.cnt-idx+1):
                curr=curr.prev
        else:
            curr=self.head
            for i in range(idx):
                curr=curr.next
        curr.prev.next=newNode
        newNode.prev=curr.prev
        newNode.next=curr
        curr.prev=newNode
        self.cnt+=1
    def delete(self,idx):
        if idx>self.cnt:
            return
        if idx > self.cnt/2:
            curr=self.tail
            for i in range(self.cnt-idx+1):
                curr=curr.prev
        else:
            curr=self.head
            for i in range(idx):
                curr=curr.next
        curr.prev.next=curr.next
        curr.next.prev=curr.prev
        self.cnt-=1
    def update(self,idx,data):
        if idx>self.cnt:
            return
        if idx > self.cnt/2:
            curr=self.tail
            for i in range(self.cnt-idx+1):
                curr=curr.prev
        else:
            curr=self.head
            for i in range(idx):
                curr=curr.next
        curr.data=data
    def get(self,idx):
        if idx>self.cnt:
            return
        if idx > self.cnt/2:
            curr=self.tail
            for i in range(self.cnt-idx+1):
                curr=curr.prev
        else:
            curr=self.head
            for i in range(idx):
                curr=curr.next
        return curr
    def descShow(self):
            curr=self.tail
            for i in range(self.cnt):
                print(curr.data,end=' ')
                curr=curr.prev
            print(curr.data,end=' ')
            print(curr.prev.data)
    def ascShow(self):
        curr=self.head
        for i in range(self.cnt):
            print(curr.data,end=' ')
            curr=curr.next
        print(curr.data,end=' ')
        print(curr.next.data)

    def show(self,flag=True):
        if flag:
            self.ascShow()
        else:
            self.descShow()
    def indexOf(self,data):
        curr=self.head
        for i in range(self.cnt):
            curr=curr.next
            if curr.data==data:
                return i+1
        
