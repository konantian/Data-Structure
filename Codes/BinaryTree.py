from BinarySearchTree import BST,TreeNode

class BinaryTree(BST):
		
	#Add a key to the tree in level order
	def insert(self,key):
		temp=TreeNode(key,None,None)

		if self.root is None:
			self.root=temp

		else:
			stack=[self.root]
			while True:
				node=stack.pop(0)
				if node.left is None:
					node.left=temp
					break

				elif node.right is None:
					node.right=temp
					break

				else:
					stack.append(node.left)
					stack.append(node.right)

		self.size+=1

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
				node=self.findDeepest()
				parent=self.getParent(node.value)
				temp=TreeNode(node.value,self.root.left,self.root.right)
				self.root=temp
				if parent.right:
					parent.right=None
				else:
					parent.left=None

			self.size-=1
			return self.root

	def findDeepest(self):

		current=self.root

		while 1:
			if current:
				if not current.left and not current.right:
					break
				else:
					current=current.right

		return current
		
	#Using DFS to search the key
	def find(self,key):

		stack=[self.root]

		while stack:
			node=stack.pop()
			if node.value == key:
				return node
			else:
				if node.right:
					stack.append(node.right)
				if node.left:
					stack.append(node.left)

		print("Error, key not in tree")
		return 

	def findPath(self,key,root=False):

		if root == False:
			root=self.root

		if not root:
			return ""

		if root.value == key:
			return str(root.value)

		res=self.findPath(key,root.left)
		if res:
			return str(root.value)+"->"+res
		res=self.findPath(key,root.right)
		if res:
			return str(root.value)+"->"+res

		return ""

	def findpath(self,key,root=False,path=""):
		if root==False:
			root=self.root

		path+=str(root.value)
		if root.value == key:

			return path

		if root.left:
			self.findpath(key,root.left,path+"->")

		if root.right:
			self.findpath(key,root.right,path+"->")

		return path

		
