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
