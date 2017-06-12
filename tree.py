#minimum spanning tree algorithym

G = { 'C': [('B', 5)],'A': [('B', 2)], 'B': [('A', 2), ('C',5)]}

def Question3(G):

	# determine # of vertices ( minus 1 where to stop iteration )
	v = len(G) - 1
	#graph = sorted(G)
	result = []
	# make into list of all vertices and sort by weight
	for h, i in G.items():
		j = h
		for p in i:
			j = j + p[0] + str(p[1])


	return j

print Question3(G)
