# Find the element in a singly linked list that's m elements from the end. 
# For example, if a linked list has 5 elements, the 3rd element from the end 
# is the 3rd element. 

# The function definition should look like question5(ll, m), 
# where ll is the first node of a linked list and m is the "mth number from the end". 
# You should copy/paste the Node class below to use as a representation of a node in 
# the linked list. Return the value of the node at that position.

class Node(object):

  def __init__(self, data):
    self.data = data
    self.next = None # first node in list has nothing to point at

  def get_data(self): 
  	return self.data 

  def get_next(self): 
  	return self.next_node 

  def set_next(self, new_next): 
  	self.next_node = new_next 

  	#See more at: https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/#sthash.OSXodfIP.dpuf

# a linked list is a string of nodes, sort of like a string of pearls, 
# with each node containing both data and a reference to the next node 
# in the list

class LinkedList:

    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = Node(data) # create a new node
        new_node.data = data
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.

    def list_print(self):
        node = self.cur_node 
        while node:
            print node.data
            node = node.next

    def size(self): 
    	current = self.head 
    	count = 0 
    	while current: 
    		count += 1 
    		current = current.get_next() 
    		return count # - 


# Function to get the nth node from the last of a linked list

# build a sample list
ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)
ll.add_node(5)

m = 3

def Question5(ll, m):
	# ll.list_print() # works
	# find the total length of the sample list


 
Question5(ll, m)