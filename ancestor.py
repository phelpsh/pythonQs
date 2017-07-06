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

T = [[0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
r = 3
n1 = 1
n2 = 4


def rootTest(r, holder):
    if holder == r:
        return True


def question4(T, r, n1, n2):

    n1folks = []  # list to hold n1 parents
    n2folks = []

    for t in T:
        if t[n1]:
            n1folks.append(T.index(t))
            # now find the parent of that node until it hits root (r)
            holder = T.index(t)  # test for root
            while not rootTest(r, holder):
                for tp in T:
                    # keep finding parents until root is identified
                    if tp[holder]:  # find parent
                        n1folks.append(T.index(tp))  # add parent to n1folks
                        holder = T.index(tp)
    for n in T:  # find second node parent
        if n[n2]:
            n2folks.append(T.index(n))
            # now find the parent of that node until it hits root (r)
            holder = T.index(n)
            while not rootTest(r, holder):  # test for root
                for np in T:
                    # keep finding parents until root is identified
                    if np[holder]:  # find parent
                        n2folks.append(T.index(np))  # add parent to n2folks
                        holder = T.index(np)
    # commonA = set(n1folks).intersection(n2folks)
    commonA = set(n1folks) & set(n2folks)
    return list(commonA)


print question4(T, r, n1, n2)


# and the answer would be 3
