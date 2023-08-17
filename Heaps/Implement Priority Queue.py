from os import *
from sys import *
from collections import *
from math import *


# Use this class to implement  the following operations.
''' 
    class priQueue:

		def __init__(self):
			self.size = -1
			self.arr = [None for i in range(1000)]
       
        pushMethod = push
		popMethod = pop
        getMaxElement = getMaxElement
        isEmptyMethod =  isempty
'''

# Function to perform push operation
def parent(idx):
	return ( idx-1 ) // 2
	
# Function to return the left child of 'idx'
def leftChild(idx):
	return ( 2 * idx + 1 )
	
#Function to return right child of 'idx'
def rightChild(idx):
	return ( 2 * idx + 2) 
	
	
# Moveup utility function used in push operation
def moveUp(idx, arr):
	
	# Get the parent of 'idx'
	prt = parent(idx)
	
	# Keep swapping the child with its parent until Heap property is satisfied
	while(idx > 0 and arr[idx] > arr[prt]):
		
		# Swaping parent with child

		arr[idx], arr[prt] = arr[prt], arr[idx]
		
		# Recursively call moveUp operation on parent
		moveUp(prt, arr)
		
# Function to perform push operation
def push(self, data):
	
	# Increment the size of heap by one
	 
	self.size += 1

	# Store the data to the end of the Heap
	self.arr[self.size] = data
	
	# To maintain the Heap property ( root element is greater than child element ) perform moveUp operation on size index
	moveUp(self.size, self.arr)
 

'''
Time Complexity of pop operation: O( log('N') )
Space Complexity: O(1)

where 'N' is the size of the Heap.
'''

# Utility function used in pop operation
def moveDown(idx, arr, size):
	
	# Let 'greateridx' be 'idx'
	greateridx = idx
	
	# Get the left child of 'idx'
	leftIdx = leftChild(idx)
	
	# Get the right child of 'idx'
	rightIdx = rightChild(idx)
	
	# Compare curret greteridx with left child 
	if(leftIdx <= size and arr[leftIdx] > arr[greateridx]):
		greateridx=leftIdx
		
	#Compare current greteridx with right child
	if(rightIdx <= size and arr[rightIdx] > arr[greateridx]):
		greateridx = rightIdx
		
	# Swap the parent index 'idx' with greteridx
	arr[idx], arr[greateridx] = arr[greateridx], arr[idx]
	
	# If parent index 'idx' was not greater than it's child ,perform moveDown operation on its greatest child
	if(idx!=greateridx):
		
		moveDown(greateridx, arr, size)
		
# Function to pop operation
def pop(self):
	
	# If size is negative i.e no data in heap, then do nothing
	
	if(self.size == -1):
		return 
		
	# Otherwise swap first element with last element
	self.arr[0], self.arr[self.size] = self.arr[self.size], self.arr[0]
	
	# Decrease the size of Heap by One
	self.size -= 1
	
	# To maintain the property of Heap  perform movedown opration on '0' index
	moveDown(0, self.arr, self.size)


'''
Time Complexity of getMaxElement operation: O(1)
Space Complexity: O(1)
'''

# Function that returns the maximum element from the Heap
def getMaxElement(self):
	
	# If Heap is empty 
	if(self.size == -1):
		return -1
	
	# Otherwise return first Heap element
	return self.arr[0]


'''
Time Complexity of isEmpty operation: O(1)
Space Complexity: O(1)
'''

# Function to check whether Heap is empty(1) or not(0)
def isempty(self):
	
	# If size of Heap is '-1', then Heap is empty
	if(self.size == -1):
		return 1
		
	# Otherwise not empty
	return 0
