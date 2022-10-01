class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
def delhead(head):
    if head==None:
        return None
    else:
        return head.next
def insertend(a,head):
    if head==None:
        return Node(a)
    temp=Node(a)
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=temp
    return head
head=None
n=int(input())
for i in range(n):
    a=int(input()) # key to be inserted at head
    head=insertend(a,head)
head=delhead(head)
def printlist(head):
    curr=head
    while curr!=None:
        print(curr.key,end=' ')
        curr=curr.next
printlist(head)
     