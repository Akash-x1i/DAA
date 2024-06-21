# Set Manipulation Algorithm by Union-Find (Find Function, Union Function, Path Compression Modifications to Find():).)

## Find Function:

def find(i): 

	# If i is the parent of itself 
	if (parent[i] == i): 

		# Then i is the representative of 
		# this set 
		return i 
	else: 

		# Else if i is not the parent of 
		# itself, then i is not the 
		# representative of his set. So we 
		# recursively call Find on its parent 
		return find(parent[i])

## Union Function:

def union(parent, rank, i, j): 
	# Find the representatives 
	# (or the root nodes) for the set 
	# that includes i 
	irep = find(parent, i) 
	
	# And do the same for the set 
	# that includes j 
	jrep = find(parent, j) 
	
	# Make the parent of i’s representative 
	# be j’s representative effectively 
	# moving all of i’s set into j’s set) 
	
	parent[irep] = jrep 

## Path Compression (Modifications to Find()):

def find(i): 

	# If i is the parent of itself 
	if Parent[i] == i: 

		# Then i is the representative 
		return i 
	else: 

		# Recursively find the representative. 
		result = find(Parent[i]) 

		# We cache the result by moving i’s node 
		# directly under the representative of this 
		# set 
		Parent[i] = result 
		
		# And then we return the result 
		return result
