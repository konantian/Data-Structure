from DoublyLinkedList import Doubly_Linked_List
class Queue:
    def __init__(self):
        self.items =Doubly_Linked_List()  #create a new queue with doubly linked list
           
    def enqueue(self,item):               #add a new item to the end of the queue
        self.items.append(item)
    
    def dequeue(self):                   #remove the first item of the queue and return it
        if self.items.is_empty():
            raise Exception('The list is empty ')
        else:
            return self.items.pop(0)   
    def peek(self):
        if self.items.is_empty():
            raise Exception('The list is empty ')
        else:
            return self.items.head.data
    def isEmpty(self):                   #determine if the queue is empty
        return self.items.size()==0
    
    def size(self):                      #return the number of items in the queue
        return self.items.size()
                      
    def __str__(self):                   #Returns a string representation of the object
        data=self.items.__str__().split('->')
        sep="]"
        return sep+",".join(data)+"]"
