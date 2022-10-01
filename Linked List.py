class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
def inserthead(a,head):
    temp=Node(a)
    temp.next=head
    return temp
head=None
n=int(input())
for i in range(n):
    a=int(input()) # key to be inserted at head
    head=inserthead(a,head)
def printlist(head):
    curr=head
    while curr!=None:
        print(curr.key,end=' ')
        curr=curr.next
printlist(head)
    

    
