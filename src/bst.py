import sys

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
	def addnode(self,data):
		if data < self.data:
			if self.left:
				self.left.addnode(data)
			else:
				self.left = Node(data)
		else:
			if self.right:
				self.right.addnode(data)
			else:
				self.right = Node(data)
	def height(self):
		hl = 0
		hr = 0
		if self.left:
			hl += self.left.height()
		if self.right:
			hr += self.right.height()
		return max(hl,hr)+1	
	def fmin(self):
		current = self
		while current.left:
			current = current.left
		return current.data
	def fmax(self):
		current = self
		while current.right:
			current = current.right
		return current.data
	def findnode(self,data):
		current = self
		flag = False
		while current and not flag:
			flag = data == current.data
			if data < current.data:
				if current.left:
					current = current.left
				else:
					return flag
			if data > current.data:
				if current.right:
					current = current.right
				else:
					return flag
		return flag
	
	def inorder(self):
		if self.left:
			yield from self.left.inorder()
		
		yield (self.data)
		if self.right:
			yield from self.right.inorder()
		
			
	def lorder(self):
		#self.item.data = []
		xp = []
		Q = [self]
		dist = {}
		dist[self] = 0
		level= {}
		level[0] = self.data
		while Q:
			v = Q.pop()
			if v.left:
				if v.left not in xp:
					xp.append(v.left)
					Q.append(v.left)
					d = dist[v] + 1
					dist[v.left] = d
					if d not in level.keys():
						level[d] = []
					level[d].append(v.left.data)
			if v.right:
				if v.right not in xp:
					xp.append(v.right)
					Q.append(v.right)
					d = dist[v] + 1
					dist[v.right] = d
					if d not in level.keys():
						level[d] = []
					level[d].append(v.right.data)
		return level
	def getdatanode(self):
		return self.data
	
	def isleaf(self):		
		flag = (self.left == None) and (self.right == None)
		return flag
			
	def pathnode(self,xp):
		if self.isleaf():
			print(xp)
			xp.pop()
		if self.left:
			xp.append(self.left.data)
			self.left.pathnode(xp)
			#xp.pop()
		if self.right:
			xp.append(self.right.data)
			self.right.pathnode(xp)
			xp.pop()
			
		#xp.pop()
		

		
		
class BST:
	def __init__(self):
		self.item = None
		self.size = 0
	def insert(self,data):
		self.size += 1
		if self.item:
			self.item.addnode(data)
		else:
			self.item = Node(data)
	def getheight(self):
		if self.item:
			return self.item.height()
		else:
			return 0
	def getsize(self):
		return (self.size)
	def findmin(self):
		if self.item:
			return self.item.fmin()
		else:
			return -1
	def findmax(self):
		if self.item:
			return self.item.fmax()
		else:
			return -1
	def find(self,data):
		if self.item:
			return self.item.findnode(data)
		else:
			return False
	def levelorder(self):
		if self.item:
			return self.item.lorder()
		else:
			return None
	def path(self):
		if self.item:
			xp = [self.item.getdatanode()]
			return self.item.pathnode(xp)
		else:
			return None
			
	def inorder(self):
		if self.item:
			yield from self.item.inorder()
		else:
			pass
			