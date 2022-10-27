# Python program to implement
# the above approach

# Structure of a Node of
# the doubly linked list
class Node:
	def __init__(self):
		self.data = 0;
		self.next = None;
		self.prev = None;

# Function to insert a Node at the
# beginning of the Doubly Linked List
def push(head_ref, new_data):

	# Allocate memory for new Node
	new_Node = Node();

	# Insert the data
	new_Node.data = new_data;

	# Since Node is added at the
	# beginning, prev is always None
	new_Node.prev = None;

	# Link the old list to the new Node
	new_Node.next = head_ref;

	# If pointer to head is not None
	if (head_ref != None):

		# Change the prev of head
		# Node to new Node
		head_ref.prev = new_Node;
	
	# Move the head to point to the new Node
	head_ref = new_Node;
	return head_ref;

# Function to find the position of
# an integer in doubly linked list
def search(head_ref, x):

	# Stores head Node
	temp = head_ref;

	# Stores position of the integer
	# in the doubly linked list
	pos = 0;

	# Traverse the doubly linked list
	while (temp.data != x and temp.next != None):
		# Update pos
		pos+=1;

		# Update temp
		temp = temp.next;
	
	# If the integer not present
	# in the doubly linked list
	if (temp.data != x):
		return -1;
	
	# If the integer present in
	# the doubly linked list
	return (pos + 1);

# Driver Code
if __name__ == '__main__':
	head = None;
	X = 8;
	
	# Create the doubly linked list
	# 18 <-> 15 <-> 8 <-> 9 <-> 14
	head = push(head, 14);
	head = push(head, 9);
	head = push(head, 8);
	head = push(head, 15);
	head = push(head, 18);
	print(search(head, X));

# This code is contributed by Rajput-Ji
