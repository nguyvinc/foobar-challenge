def solution(h, q):
    found = []
    max_node = 2 ** h
    # Insert nodes 1 to (2^height - 1) into array
    for num in range(1, max_node):
        found.append(num)
    found.reverse()

    # Construct post-order tree
    tree = Node(found, None)

    found = []  # Empty array to store found values
    # For each number to be found
    for num in q:
        # If the number is greater than the possible node number or less than 1, add -1
        if(num <= 0 or num >= max_node):
            found.append(-1)
        # Else, look for the number and insert its parent's value
        else:
            tree.searchParent(num, found)
    return found

        
class Node:
    def __init__(self, values, parent):
        self.left = None
        self.right = None
        self.value = None
        self.parent = parent    # Store parent to make it easier to search for parent value
        self.construct(values)  # Construct tree

    def construct(self, values):
        self.value = values[0]  # Assign 1st value of array to node
        values.pop(0)           # Remove that value
        if(len(values) >= 2):   # If there are at least 2 values left
            half = len(values) / 2
            # Split the remaining array in half for the 2 subtrees and construct the rest of the tree
            self.right = Node(values[0:(half)], self)
            self.left = Node(values[(half):len(values)], self)

    def searchParent(self, value, found):
        if(self.value == value):    # If the node's value matches what we're trying to find
            if(self.parent != None):    # If the node has a parent, push the parent's value
                found.append(self.parent.value)
            else:                       # If the node doesn't have a parent (is root), push -1
                found.append(-1)
        else:                       # Else keep searching
            if(self.left != None):
                self.left.searchParent(value, found)
            if(self.right != None):
                self.right.searchParent(value, found)

    def printTree(self):
        if(self.value != None):
            print(self.value)
        if(self.left != None):
            self.left.printTree()
        if(self.right != None):
            self.right.printTree()
    
    def printParent(self):
        if(self.parent != None):
            print(self.parent.value)
        if(self.left != None):
            self.left.printParent()
        if(self.right != None):
            self.right.printParent()