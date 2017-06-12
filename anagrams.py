###################
# test cases      #
# all return True #
###################

s = "udacity"
t = "add"

s = "gooogdnksdfjeb"
t = "sgoog"

s = "  d6 dd 8s  h"
t = "  d8dh"


def Question1(s, t):
	for l in t:
		if not l in s:
			return False #not there, easy out of def
		#count how many times l is in t
		c = t.count(l)
		if c > 1: #if l is more than one, move on
			# count l in s
			c2 = s.count(l)
			if c > c2:
				return False #counts not the same, bail out
		
	return True # all letters accounted for

print Question2(s, t)

