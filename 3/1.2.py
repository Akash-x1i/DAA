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
