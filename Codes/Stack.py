# A Stack implementation

class Stack(object):
    
    def __init__(self,items=[]):
        self.__items = items
        
    def push(self, item):
        self.__items.append(item)
        
    def pop(self):
        if self.isEmpty():
             raise Exception("Stack empty!")

        return self.__items.pop()
    
    def peek(self):
        if self.isEmpty():
             raise Exception("Stack empty!")
             
        return self.__items[len(self.__items)-1]
    
    def isEmpty(self):
        return len(self.__items) == 0
    
    def size(self):
        return len(self.__items)

    def show(self):
        return self.__items