# minimum spanning tree algorithym

G = { 'C': [('B', 3), ('G', 9), ('E', 8)],
	  'A': [('B', 10), ('F', 2)], 
	  'B': [('A', 10), ('C', 3), ('E', 4)],
	  'D': [('E', 6)],
	  'E': [('D', 6), ('C', 8), ('B', 4), ('F', 5)],
	  'G': [('C', 9)],
	  'F': [('A', 2), ('E', 5)] }

G = { 'C': [('B', 5)],'A': [('B', 2)], 'B': [('A', 2), ('C', 5)]}

G = { 'C': [('B', 5)],
	  'A': [('B', 2), ('D', 4)], 
	  'B': [('A', 2), ('C', 5), ('D', 6)],
	  'D': [('A', 4), ('B', 6)] }
# need weight, source, and destination for each node pair
# don't need to get each direction because this is an undirected graph

edges = [] # global list to track edges because graph is not circular 
           # to start when moving through weights
           # this will be dictionary of list of tuples: 
           # { 'C': [('B', 5)],'A': [('B', 2)], 'B': [('A', 2), ('C', 5)]}

def checkCircular(edge):
	# break out the edge
	v1 = edge[0] # one side of edge
	v2 = edge[1] # the other side of edge
	
	# check each vertex to see if it's in any other pairs
	# if it is,0 run through those and collect the other letters

	# need to account for 0 edges
	if len(edges) == 0 or len(edges) == 1 or len(edges) == 2: 
		return False

	templist1 = []
	templist2 = []

	for y in edges: # global edges
		
		if not (v1 == y[0][0] and v2 == y[0][1]): # skip if it finds itself
			if v1 in y[0]: # the vertex is in another vertex, add it to a temp list AB BC etc
				templist1.append(y[0])
				# find others that connect to it - "parents" (this helps to understand loop completion)

				# continue checking recursively
				# if len(templist1) == 0: continue # vertex not yet used, move onto next y
				# should go to true or false
			if v2 in y[0]: # the vertex is in another vertex, add to list
				templist2.append(y[0])
				
	for w in templist1:
		for a in w:
			for q in templist2:
				for x in q:
					if x == a:
						return True
	
	return False


def Question3(G):

	result = {} # empty dictionary to hold data
	# make into list of all vertices and sort by weight
	for h, i in G.items():
		for p in i:
			o = h + p[0] # vertices # key
			# check to see if reversed edge already in result
			r = o[::-1] #reverse the string
			if r in result: continue # check if it's already there			
			result[o] = p[1] # weight # value # add to dictionary

	# sort result by weight
	f = sorted(result.items(), key=lambda x:x[1]) # makes a list of tuples sorted by weight
	
	k = []
	for dd in f:
		k.append(dd[0][0])
		k.append(dd[0][1])

	# get total count of vertices ii 
	gg = {pp for pp in k} # get unique values
	gg = list(gg)
	vlength = len(gg)
	
	for y in f: # gets the edges and tests in order ('AB', 2) ('AD', 4) ('CB', 5) ('BD', 6)
		isCirc = checkCircular(y[0]) # AB, AD, CB, etc Check each edge to see if it's circular
		if isCirc is False:
			if len(edges) < vlength - 1: # number of potential edges one less than vertices
			# add the edge
				edges.append(y)
			
	return edges

print Question3(G)



