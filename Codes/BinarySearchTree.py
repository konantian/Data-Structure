class TreeNode:
	def __init__(self,initdata,initleft,initright):
		self.value=initdata
		self.left=initleft
		self.right=initright

class BST:
	#Initialize the root node
	def __init__(self):
		self.root=None
		self.size=0

	#Get the left child value of given key
	def getLeft(self,key):

		return self.find(key).left.value

	#Get the right child value of given key
	def getRight(self,key):

		return self.find(key).right.value

	def getRoot(self):

		return self.root.value

	#Given a key, insert a node to the tree,Time complexity:O(h)
	def insert(self,val,node=False):
		node=self.root if node == False else node

		temp=TreeNode(val,None,None)

		if self.root == None:
			self.root=temp
			self.size+=1
		else:
			if val < node.value:
				if node.left == None:
					node.left=temp
					self.size+=1
				else:
					self.insert(val,node.left)
			else:
				if node.right == None:
					node.right=temp
					self.size+=1
				else:
					self.insert(val,node.right)

	#Given a value and find it in the tree, return node if found else False,Time complexity:O(h)
	def find(self,val,node=False):
		node = node if node is not False else self.root
		if node:
			if val == node.value:
				return node
			elif val < node.value and node.left:
					return self.find(val,node.left)
			else:
				if node.right:
					return self.find(val,node.right)

		return False

	#Given a key and find the path from the root to it, if found return the path else return empty path
	def findPath(self,key,node=False,path=""):

		if node == False:
			node=self.root

		if node.value == key:
			
			path+=str(node.value)

			return path

		elif key < node.value:
			if node.left:
				path+=str(node.value)+"->"
				return self.findPath(key,node.left,path)
			else:
				return []
		else:
			if node.right:
				path+=str(node.value)+"->"
				return self.findPath(key,node.right,path)
			else:
				return []

	#Find all the paths from root node to the leaf nodes
	def findAllpath(self):
		if not self.root:
			return []

		return self.findAllpathHelp(self.root,[],"")

	#Helper function
	def findAllpathHelp(self,root,result,temp):

		temp+=str(root.value)
		if root.left:
			self.findAllpathHelp(root.left,result,temp+"->")
		if root.right:
			self.findAllpathHelp(root.right,result,temp+"->")
		if not root.left and not root.right:
			result.append(temp)
	
		return result

	#Determine if the tree is balanced
	def isBalanced(self):
		if not self.root:
			return True

		left=self.getHeight(self.root.left)
		right=self.getHeight(self.root.right)
		if abs(left-right) > 1:
			return False
		return True

	#Determine if the tree is perfect
	def isPerfect(self):
		height=self.getHeight(self.root)

		return self.size == pow(2,height)-1

	#Determine if the tree is full
	def isFull(self):
		leaf_node=self.countLeaf()
		internal_node=self.size-leaf_node

		return internal_node+1 == leaf_node

	#Count the number of leaf nodes in the tree
	def countLeaf(self,node=False):

		if node == False:
			node=self.root

		if node is None:
			return 0
		if node.left is None and node.right is None:
			return 1
		else:
			return self.countLeaf(node.left)+self.countLeaf(node.right)

	#Delete all nodes of the tree
	def clear(self):

		self.root=None
		self.size=0

	#Return the number of elements of the tree
	def getSize(self):

		return self.size

	#Detect if the tree has no nodes
	def isEmpty(self):
		
		return self.size == 0

	#Given a key, if this key exist, if the key has same value with the root
	#remove the root,Time complexity:O(h)
	def delete(self,key):

		if self.find(key) == False:
			print("Error, key not in tree")
			return

		if self.root.value == key:
			if self.root.left == None and self.root.right == None:
				self.root=None

			elif self.root.left and self.root.right == None:
				self.root=self.root.left

			elif self.root.right and self.root.left == None:
				self.root=self.root.right

			elif self.root.left and self.root.right:

				node=self.findSmallest(self.root.right)
				if node == self.root.right:
					temp=TreeNode(node.value,self.root.left,node.right)
					self.root=temp
				else:
					parent=self.getParent(node.value)
					temp=TreeNode(node.value,self.root.left,self.root.right)
					self.root=temp
					parent.left=node.right
					
			self.size-=1
			return self.root
		else:
			return self.deleteNode(self.root,key)

	#Helper function to delete a node insted of the root
	def deleteNode(self,node,val):

		if not node:
			return None

		if node.value == val:
			if node.left:
				left_right_most=node.left
				while left_right_most.right:
					left_right_most=left_right_most.right
				left_right_most.right=node.right
				self.size-=1
				return node.left
			else:
				self.size-=1
				return node.right
		elif node.value > val and node.left:
			node.left=self.deleteNode(node.left,val)

		else:
			node.right=self.deleteNode(node.right,val)

		return node

	#Return the smallest key greater than the given key,Time complexity:O(h)
	#Largest element in the tree does not have successor
	def successor(self,key):
		node=self.find(key)


		#The key given does not exist
		if node == False:
			print("Key does not exist")
			return 

		#If the given node has right subtree
		if node.right:
			return self.findSmallest(node.right).value

		#If the given node does not have right subtree, traverse the parent
		#until find the one greater than it
		else:
			temp=self.getParent(node.value)
			while temp != None and temp.value < node.value:
				
					temp=self.getParent(temp.value)

			if temp:
				return temp.value 
			else:
				print("This key does not have successor")
				return

	#Return the largest key smaller than the given key, Time complexity:O(h)
	#Smallest element in the tree dose not have predecessor
	def predecessor(self,key):

		node=self.find(key)

		if node == False:
			print("Key does not exist")
			return 

		if node.left:
			return self.findLargest(node.left).value
		else:
			temp=self.getParent(node.value)
			while temp != None and temp.value > node.value:

				temp=self.getParent(temp.value)

			if temp:
				return temp.value 
			else:
				print("This key does not have predecessor")
				return
		
	#Given a node, find the smallest node in current subtree,Time complexity:O(h)
	def findSmallest(self,currentNode):
		
		current=currentNode
		while current.left != None:
			current=current.left

		return current

	#Given a node, find the largest node in current subtree
	def findLargest(self,currentNode):

		current=currentNode
		while current.right != None:
			current=current.right

		return current

	#Given a key,return the parent node of it,Time complexity:O(h)
	def getParent(self,key,node=False,parent=None):
		
		node = self.root if node == False else node

		if node:
			if node.value == key:
				return parent

			elif key < node.value and node.left:
				return self.getParent(key,node.left,node)
			else:
				if node.right:
					return self.getParent(key,node.right,node)

	#Get the height of this tree,,Time complexity:O(n)
	def getHeight(self,node=False):

		node = self.root if node == False else node

		if node is None:
			return 0
		else:
			lheight=self.getHeight(node.left)
			rheight=self.getHeight(node.right)

			return lheight+1 if lheight > rheight else rheight+1

	#Print the tree in order, recursively,Time complexity:O(n)
	def printInorder(self,node=False):
		node = self.root if node == False else node

		if node:
			self.printInorder(node.left)
			print(node.value,end=' ')
			self.printInorder(node.right)

	#Print the tree in order, iteratively,Time complexity:O(n)
	def printinorder(self):
		
		root=self.root
		stack=[]

		while True:
			while root:
				stack.append(root)
				root=root.left
			if not stack:
				return
			node=stack.pop()
			print(node.value,end=' ')
			root=node.right

	#Print the tree postorder, recursively,Time complexity:O(n)
	def printPostorder(self,node=False):
		node = self.root if node == False else node

		if node:
			self.printPostorder(node.left)
			self.printPostorder(node.right)
			print(node.value,end=' ')

	#Print the tree postorder, iteratively,Time complexity:O(n)
	def printpostorder(self):
		stack=[]
		current=self.root
		while True:
			if current:
				if current.right:
					stack.append(current.right)
				stack.append(current)
				current=current.left
				continue
			if not stack:
				break
			node=stack.pop()
			if node.right and stack and node.right == stack[-1]:
				current=stack.pop()
				stack.append(node)
			else:
				print(node.value,end=' ')

	#Print the tree preorder, recursively,Time complexity:O(n)
	def printPreorder(self,node=False):
		node = self.root if node == False else node

		if node:
			print(node.value,end=' ')
			self.printPreorder(node.left)
			self.printPreorder(node.right)

	#Print the tree preorder, iteratively,Time complexity:O(n)
	def printpreorder(self):
		
		root=self.root
		stack=[root]

		while stack:
			node=stack.pop()
			print(node.value,end=' ')
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)

	#Print the tree levelorder, recursively,Time complexity:O(n)
	def printLevelorder(self):
		h=self.getHeight(self.root)
		for i in range(1,h+1):
			self.printGivenLevel(self.root,i)

	#Helper function to print node at each level,Time complexity:O(n)
	def printGivenLevel(self,root,level):
		if root is None:
			return

		if level == 1:
			print(root.value,end=' ')

		elif level > 1:
			self.printGivenLevel(root.left,level-1)
			self.printGivenLevel(root.right,level-1)

