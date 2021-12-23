class Node:
    
class Book:
    def __init__(self,ISBN,name,author):
        self.ISBN=ISBN
        self.name=name
        self.author=author

bookList=DoubleLinkedList()

while True:
    print("1. 도서 등록\n2. 도서 삭제\n3. 도서 검색\n4. 도서 목록\n5. 끝내기")
    choice = int(input())
    if choice==1:
        
    if choice==2:
 
    if choice==3:
        pass

    if choice==4:
        for i in range(bookList.cnt):
            print(bookList.get(i+1).data.name,bookList.get(i+1).data.author,bookList.get(i+1).data.ISBN)
    if choice==5:
        break
