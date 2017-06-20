# Find the least common ancestor between two nodes on a binary search tree. 

# The least common ancestor is the farthest node from the root that is an 
# ancestor of both nodes. For example, the root is a common ancestor of all 
# nodes on the tree, but if both nodes are descendents of the root's left child, 
# then that left child might be the lowest common ancestor. 

# You can assume that both nodes are in the tree, and the tree itself adheres to 
# all BST properties. The function definition should look like 
# question4(T, r, n1, n2), where T is the tree represented as a matrix, 
# where the index of the list is equal to the integer stored in that node 
# and a 1 represents a child node, r is a non-negative integer representing the 
# root, and n1 and n2 are non-negative integers representing the two nodes in no 
# particular order. 

# For example, one test case might be

T = [[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
r = 3
n1 = 1
n2 = 4


def question4(T, r, n1, n2):

    n1folks = []  # list to hold n1 parents

    for t in T:
        if t[n1] or t[n1] == 0:
            n1folks.append(T.index(t))
            # now find the parent of that node
            holder = T.index(t)
            if t[holder] or t[holder] == 0:
                print "the parent has a parent"
            # this needs to be recursive and call a function do...while
    return n1folks


print question4(T, r, n1, n2)


# and the answer would be 3.

# Method 1 (By Storing root to n1 and root to n2 paths):
# Following is simple O(n) algorithm to find LCA of n1 and n2.
# 1) Find path from root to n1 and store it in a vector or array.
# 2) Find path from root to n2 and store it in another vector or array.
# 3) Traverse both paths till the values in arrays are same. Return the
# common element just before the mismatch.
