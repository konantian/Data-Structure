from DoublyLinkedList import Doubly_Linked_List
class Deque:
    def __init__(self):
        self.items =Doubly_Linked_List()  #create a new dequeue with doubly linked list

    def isEmpty(self):
    	return self.items.size()==0

    def size(self):
    	return self.items.size()

    def insertFront(self,item):
    	self.items.append(item)

    def insertRear(self,item):
    	self.items.insert(0,item)

    def removeFront(self):
    	return self.items.pop()

    def removeRear(self):
    	return self.items.pop(0)

    def count(self,value):
        count=0
        current=self.items.head
        while current != None:
            if current.data == value:
                count+=1
            current=current.next
        return count

    def extend(self,lst):
        if lst is self:
            lst=list(lst)
        for elem in lst:
            self.insertFront(elem)

    def extendleft(self,lst):
        if lst is self:
            lst=list(lst)
        for elem in lst:
            self.insertRear(elem)

    def rotate(self,n):
        length=self.size()
        if length <=1:
            return
        halflen=length >> 1
        if n > halflen or n < -halflen:
            n %= length
            if n > halflen:
                n-=length
            elif n < - halflen:
                n+=length
        while n > 0:
            self.insertRear(self.removeFront())
            n-=1
        while n < 0:
            self.insertFront(self.removeRear())
            n+=1

    def reverse(self):
        self.items.reverse()

    def remove(self,value):
        self.items.remove(value)

    def removeAll(self,value):
        self.items.removeAll(value)

    def __str__(self):                   #Returns a string representation of the object
        data=self.items.__str__().split('->')
        sep="]"
        return sep+",".join(data)+"]"