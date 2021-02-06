'''Function to display hashtable'''


def display_hash(hashTable): 
	
	for i in range(len(hashTable)): 
		print(i, end = " ") 
		
		for j in hashTable[i]: 
			print("-->", end = " ") 
			print(j, end = " ") 
			
		print() 

# Creating Hashtable as 
# a nested list. 
HashTable = [[] for _ in range(10)] 

# Hashing Function to return 
# key for every dataue. 
def Hashing(keydataue): 
	return keydataue % len(HashTable) 


# Insert Function to add 
# dataues to the hash table 
def insert(Hashtable, keydataue, dataue): 
	
	hash_key = Hashing(keydataue) 
	Hashtable[hash_key].append(dataue) 

# Driver Code 
insert(HashTable, 10, 'Allahabad') 
insert(HashTable, 25, 'Mumbai') 
insert(HashTable, 20, 'Mathura') 
insert(HashTable, 9, 'Delhi') 
insert(HashTable, 21, 'Punjab') 
insert(HashTable, 2, 'Anshu')
insert(HashTable, 29, 'Atulya')
insert(HashTable, 17, 'Adarsh') 

display_hash (HashTable) 


###################################################################################

''' Binary Tree '''


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)

root.PrintTree()
