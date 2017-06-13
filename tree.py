# minimum spanning tree algorithym

G = { 'C': [('B', 5)],'A': [('B', 2)], 'B': [('A', 2), ('C', 5)]}
G = { 'C': [('B', 5)],
	  'A': [('B', 2), ('D', 4)], 
	  'B': [('A', 2), ('C', 5), ('D', 6)],
	  'D': [('A', 4), ('B', 6)] }

# need weight, source, and destination for each node pair
# don't need to get each direction because this is an undirected graph

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
	# [('AB', 2), ('AD', 4), ('CB', 5)] # order of vertices doesn't matter - undirected graph

	return f

print Question3(G)
