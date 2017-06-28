# Find the element in a singly linked list that's m elements from the end. 
# For example, if a linked list has 5 elements, the 3rd element from the end 
# is the 3rd element. 

# The function definition should look like question5(ll, m), 
# where ll is the first node of a linked list and m is the "mth number from the end". 
# You should copy/paste the Node class below to use as a representation of a node in 
# the linked list. Return the value of the node at that position.

class Node(object):

  def __init__(self, data, position, next_node=None):
    self.data = data
    self.next_node = next_node # first node in list has nothing to point at
    self.position = position

  def get_data(self): 
  	return self.data 

  def get_next(self): 
  	return self.next_node

  def set_next(self, new_next): 
  	self.next_node = new_next 

  def set_position(self, position):
  	self.position = position

# See more at: https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/#sthash.OSXodfIP.dpuf

# a linked list is a string of nodes, sort of like a string of pearls, 
# with each node containing both data and a reference to the next node 
# in the list

class LinkedList:

    def __init__(self, head = None):
        self.head = head

    def add_node(self, data, position = 0):
        new_node = Node(data, position) # create a new node
        if not self.head is None:
        	newpos = self.head.position + 1
        	new_node.set_position(newpos)
        new_node.set_next(self.head) # link the new node to the 'previous' node.
        self.head = new_node #  set the current node to the new one.

    def size(self): 
    	current = self.head 
    	count = 0
    	while current != None: 
    		count += 1
    		current = current.get_next() 
    	return count 

    def index(self, item):
	    current = self.head
	    while current != None:
	        if current.position == item:
	        	return current.get_data()
	        else:
	            current = current.get_next()
	    print ("An error has occurred.")


# Function to get the nth node from the last of a linked list

# build a sample list
ll = LinkedList()
ll.add_node(9)
ll.add_node(122)
ll.add_node(1333)
ll.add_node(85555)
ll.add_node(45555)

m = 3

def Question5(ll, m):
	print ll.index(m)

 
Question5(ll, m)