class SLinkedListNode:
    
    def __init__(self, initData, initNext):
        # constructs a new node and initializes it to contain 
        # the given object (initData) and links to the given next 
        # and previous nodes. 
        self.data = initData
        self.next = initNext


    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newData):
        self.data = newData
    
    def setNext(self, newNext):
        self.next= newNext
    
class SLinked_List:
    
    # creates a new doubly linked list
    # head and tail are initialized to None
    def __init__(self):
        self.head=None
        self.__size=0

    
    # adds a new node with data = item to the beginning of the list    
    def add(self, item):
        temp = SLinkedListNode(item,self.head)
        self.head = temp
        self.__size += 1

    
    # adds a new node with data = item to the end of the list    
    def append(self, item):
        temp = SLinkedListNode(item, None)
        if (self.head == None):
            self.head=temp
        else:
            current = self.head;
            while (current.getNext() != None):
                current = current.getNext()
            current.setNext(temp)
        self.__size +=1

        
    # insert a new node with data = item at the given position
    # assume index is a valid position to insert at
    def insert(self, index, item):
        temp = SLinkedListNode(item,None)
        current = self.head
        previous = None
        pos = 0
        found = False

        while not found:
            if pos == index:
                found = True
            else:
                previous = current
                current=current.getNext()
                pos += 1
        if self.head == None:
            self.head = temp

        else :
            temp.setNext(current)
            if index == 0:
                self.head = temp
            else:
                previous.setNext(temp)


        self.__size +=1
    
   #search the indicated item  and return the number of occupancy
    def search(self, item):
        current = self.head
        found=False
        while current != None:
            if current.getData() == item:
                found=True
                current = current.getNext()
            else:
                current = current.getNext()
        return found
    
    # return a list of all the indices of where the item occurs in the list
    def index(self,item):
        current = self.head
        count=0
        index=[]
        pos=0
        while current != None:
            if current.getData() == item:
                count+=1
                index.append(pos)
                pos+=1
                current = current.getNext()
            else:
                pos+=1
                current = current.getNext()
        return index        
    # removes and returns the element at the specified index 
    # assume the index is a valid position to remove at
    # default value indicates to pop from the end of the list    
    def pop(self,pos):
        current = self.head
        previous = None
        found = False
        index = 0
        while not found:
            if pos ==index:
                found = True
            else:
                previous = current
                current = current.getNext()
                index+= 1

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.__size -= 1
        return current.getData()
    
    # removes the first node with data = item from the list
    # do nothing if item is not in the list
    def remove(self, item):
        current = self.head
        previous = None
        found=False
        while found == False:
            if current.getData() == item:
                found=True
                if previous==None:
                    self.head=current.getNext()
                else:
                    previous.setNext(current.getNext())
                self.__size-=1
                current=current.getNext()
            else:
                previous=current
                current=current.getNext()
        if found==False:
            raise Exception('This item does not exist! ')

    #remove all nodes that has same value with item
    def removeAll(self,item):
        current = self.head
        previous = None
        found=False
        while current !=None :
            if current.getData() == item:
                found=True
                if previous==None:
                    self.head=current.getNext()
                else:
                    previous.setNext(current.getNext())
                self.__size-=1
                current=current.getNext()
            else:
                previous=current
                current=current.getNext()
        if found==False:
            raise Exception('This item does not exist! ')
            
    #return a copy of the list starting at the start position and going up to but not including the stop position        
    def slice(self,start,stop):
        sll=SLinked_List()
        low=0;high=self.__size
        lst = []
        current=self.head
        for i in range(low,high):
            lst.append(current.getData())    
            current=current.getNext()
        for x in lst[start:stop]:
            sll.append(x)
        return sll

    #reverse the singly linked list
    def reverse(self):
        previous=None
        current=self.head
        while current is not None:
            next_node=current.next
            current.next=previous
            previous=current
            current=next_node
        self.head=previous

    #remove duplicate elements in list
    def removeDuplicates(self):
        unique = set()
        current = self.head
        previous = None
        while current != None:
            data = current.getData()
            if data not in unique:
                unique.add(data)
                previous = current
            else:
                previous.setNext(current.getNext())
                self.__size-=1
            current = current.getNext()

    #remove duplicate elements in list without temporary buffer
    #only applicable if all the elements in the list are non-negative integers
    def removeDuplicates2(self):
        current = self.head
        checker = 0
        previous = None
        while current != None:
            data = current.getData()
            value = checker & (1 << data)
            if value > 0:
                previous.setNext(current.getNext())
                self.__size-=1
            else:
                previous = current
                checker = checker | (1 << data)
            current = current.getNext()
            
    #return the kth to last element
    def returnKthToLast(self, k):
        if not self.head: return None
        
        fast = self.head
        for _ in range(k):
            fast = fast.getNext()

        slow = self.head
        while fast != None:
            fast = fast.getNext()
            slow = slow.getNext()
        return slow
    
    #remove the kth to last element
    def removeKthToLast(self, k):
        node = self.returnKthToLast(k)
        self.deleteNode(node)
        
    def deleteNode(self, node):
        current = self.head
        while current and current.getNext() != node:
            current = current.getNext()
        if node.getNext():
            node.setData(node.getNext().getData())
            node.setNext(node.getNext().getNext())
        else:
            current.setNext(None)
    
    #given a node, delete this node from the list
    def deleteMiddleNode(self, node):

        node.setData(node.getNext().getData())
        node.setNext(node.getNext().getNext())
        self.__size -= 1
    
    #return the middle node of the list
    #if there are two middle nodes, return the second one
    def returnMiddleNode(self):
        
        slow = fast = self.head
        while fast and fast.getNext():
            slow = slow.getNext()
            fast = fast.getNext().getNext()
        return slow
    
    #detect if there is cycle in the linked list
    def loopDetection(self):
        slow, fast = self.head, self.head
        while fast and fast.getNext():
            slow = slow.getNext()
            fast = fast.getNext().getNext()
            if slow == fast:
                return slow
        return False
    
    # returns the size of the linked list
    def size(self):
        
        return self.__size

    # returns True if the singly linked list is empty, False otherwise
    def isEmpty(self):
        return self.head==None

    # returns a string representation of the list, from head to tail
    # each piece of data is separated by "->"
    def __str__(self):
        output = []
        current = self.head
        while current:
            output.append(current.data)
            current = current.next
        output=[str(i) for i in output]
        return "->".join(output)
