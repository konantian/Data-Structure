class Double_Node:
    
    def __init__(self, initData, initNext, initPrevious):
        # constructs a new node and initializes it to contain 
        # the given object (initData) and links to the given next 
        # and previous nodes. 
        self.data = initData
        self.next = initNext
        self.previous = initPrevious
        if (initPrevious != None):
            initPrevious.next = self
        if (initNext != None):
            initNext.previous = self

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous
    
    def setData(self, newData):
        self.data = newData
    
    def setNext(self, newNext):
        self.next= newNext
    
    def setPrevious(self, newPrevious):
        self.previous= newPrevious 
        
class Doubly_Linked_List:
    
    # creates a new doubly linked list
    # head and tail are initialized to None
    def __init__(self):
        self.head=None
        self.tail=None
        self.__size=0

    
    # adds a new node with data = item to the beginning of the list    
    def add(self, item):
        temp = Double_Node(item, self.head, None)
        if (self.head != None):
            self.head.setPrevious(temp)
        elif (self.head == None):
            self.tail=temp
        self.head = temp
        self.__size =self.__size+ 1

    
    # adds a new node with data = item to the end of the list    
    def append(self, item):
        temp = Double_Node(item, None, None)
        if (self.head == None):
            self.head=temp
        elif (self.head!= None):
            self.tail.setNext(temp)
            temp.setPrevious(self.tail)
            
        self.tail=temp
        self.__size =self.__size+1

        
    # insert a new node with data = item at the given position
    # assume index is a valid position to insert at
    def insert(self, index, item):
        temp = Double_Node(item,None,None)
        current = self.head
        previous = None;found = False
        count = 0

        while not found:
            if (count == index):
                found = True
            elif (count != index):
                previous = current
                current=current.getNext()
                count = count+ 1
                
        if (self.head == None):
            self.tail = temp
            self.head = temp
            
        elif (self.head != None):
            current.setPrevious(temp)
            temp.setNext(current)
            temp.setPrevious(previous)
            
            if index == 0:
                self.head = temp
            elif index!= 0:
                previous.setNext(temp)
                
        self.__size =self.__size+1
    
    # removes and returns the element at the specified index 
    # assume the index is a valid position to remove at
    # default value indicates to pop from the end of the list
    def pop(self, index=-1):
        number = 0
        current = self.head
        found = False;previous = None
        
        
        while not found and (current.getNext() != None):
            if index ==number:
                found = True
            elif index != number:
                previous = current
                current = current.getNext()
                number= number+1
                
        if current.getNext() != None:
            current.getNext().setPrevious(previous)
        elif current.getNext() == None:
            self.tail = previous
            
        if previous == None:
            self.head = current.getNext()
        elif previous != None:
            previous.setNext(current.getNext())

        self.__size =self.__size - 1; return current.getData()
    
    # removes the first node with data = item from the list
    # do nothing if item is not in the list
    def remove(self, item):
        current = self.head
        previous = None;found = False
        while not found:
            if (current.getData()) == item:
                found = True
            elif (current.getData()) != item:
                previous = current
                current = current.getNext()
        if (previous == None):
            self.head = current.getNext()
        elif (previous != None):
            previous.setNext(current.getNext())
        if (current.getNext() != None):
            current.getNext().setPrevious(previous)
        elif (current.getNext() == None):
            self.tail = previous
            
        self.__size =self.__size - 1

    #remove all nodes that has same value with given item
    def removeAll(self,item):
        current=self.head
        previous=None
        found=False
        while current != None:
            if current.getData() == item:
                found=True
                if previous == None:
                    self.head=current.getNext()
                elif previous != None:
                    previous.setNext(current.getNext())

                if current.getNext() != None:
                    current.getNext().setPrevious(previous)
                elif current.getNext() == None:
                    self.tail=previous

                self.__size-=1   
                current=current.getNext()
            else:
                previous=current
                current=current.getNext()
        if found==False:
            raise Exception('This item does not exsit! ')

        
    #reverse the order of the doubly linked list
    def reverse(self):
        temp=None
        current=self.head

        while current is not None:
            temp=current.previous
            current.previous=current.next
            current.next=temp
            current=current.previous

        if temp is not None:
            self.head=temp.previous
    # returns the size of the doubly linked list
    def size(self):
        return self.__size

    # returns True if the doubly linked list is empty, False otherwise
    def is_empty(self):
        return self.__size == 0

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
        
    # returns a string representation of the list, from tail to head
    # each piece of data is separated by "<-"
    def reverse_string(self):
        output = []
        current = self.tail
        while current:
            output.append(current.data)
            current = current.previous
        return "<-".join(output)
                 
                 
                 
