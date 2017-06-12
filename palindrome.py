a = 'nur    ses run'

def updateLongestString(s, longest):

	if longest == "" or longest is None or longest == "error":
		return s
	if len(longest) > len(s):
		return longest
	return "error"

def Question2(a):
	
	# strip out spaces
	a = a.translate( None, " " )
	l = len(a)
	if l == 0: return None
	longest = "" # track the longest palidrome string

	r = a[::-1] #reverse the string

	# Find the thing in r that is the same as in a - this will be the palindrome
	if r in a: return r # easy out for perfect palindromes; works for 1 and 2 length as well

	lsR = list(enumerate(r)) # turns into list with indices
	rkpr = 0
	
	# loop through start of each string
	for i, letter in enumerate(r): 

		s = letter[0] + lsR[i+1][1] + lsR[i+2][1]
		rkpr = i+2

		while s in a: # palindrome is there
			rkpr = rkpr + 1
			longest = updateLongestString(s, longest) # set the output
			s = s + lsR[rkpr][1] # increment the s to get the next letter
			print s

		if i > l - 4:
			break # dump out of loop once within four of the end of the string

	return "The longest palindromic string is: " + longest

print Question2(a)