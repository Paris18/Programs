class linkedlist(object):
	def __init__(self):
		self.head = None


	class Node(object):
		def __init__(self,d):
			self.data = d
			self.next = None

# double linked list
	# class dnode(object):
	# 	def __init__(self,d):
	# 		self.data = d
	# 		self.next = None
	# 		self.prev = None


	# def insert(self,data):
	# 	new_node = self.dnode(data)
	# 	new_node.next = self.head
	# 	if self.head is not None:
	# 		self.head.prev = new_node
	# 	self.head = new_node







	def push(self,new_data):
		new_node = self.Node(new_data)
		new_node.next = self.head
		self.head = new_node


	def printdata(self):
		temp = self.head
		while(temp != None):
			print temp.data
			temp = temp.next


	def deleteitem(self,item):
		temp = self.head
		if temp.data == item:
			self.head = temp.next
			return 0

		while(temp.next != None):
			if(temp.next.data == item):
				temp.next = temp.next.next
				return 0
			temp = temp.next
		print "not found"
		return 0
				



ls = linkedlist()

ls.push(10)
ls.push(20)
ls.push(30)
ls.push(40)
ls.push(50)
ls.push(60)
ls.push(70)
ls.push(80)
ls.push(90)

# ls.insert(10)
# ls.insert(20)

ls.deleteitem(110)
ls.printdata()

