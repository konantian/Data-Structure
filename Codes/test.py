from SinglyLinkedList import SLinked_List,SLinkedListNode

lst = SLinked_List()
nums = [1,2]
for num in nums:
    lst.append(num)
print(lst)
lst.removeKthToLast(1)
print(lst)