class Deque:
	def __init__(self):
		self.items=[]

	def isEmpty(self):
		return self.items==[]

	def insertFront(self,item):
		self.items.append(item)

	def insertRear(self,item):
		self.items.insert(0,item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def count(self,value):

		return self.items.count(value)

	def reverse(self):
		self.items=self.items[::-1]

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
		self.items[:]=self.items[length-n:]+self.items[:length-n]
		# if length <=1:
		# 	return
		# halflen=length >> 1
		# if n > halflen or n < -halflen:
		# 	n %= length
		# 	if n > halflen:
		# 		n-=length
		# 	elif n < - halflen:
		# 		n+=length
		# while n > 0:
		# 	self.insertRear(self.removeFront())
		# 	n-=1
		# while n < 0:
		# 	self.insertFront(self.removeRear())
		# 	n+=1

	def size(self):
		return len(self.items)

	def __str__(self):
		data=[str(i) for i in self.items]
		sep="]"
		return sep+",".join(data)+"]"


