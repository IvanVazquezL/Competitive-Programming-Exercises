class Node:
    #Node Constructor
    def __init__(self, data=None):
        #Left node is none
        self.left = None
        #Right node is none
        self.right = None
        #Passed data is the value of the node
        self.data = data

    def insert(self, data):
        #If parent node value is not None
        if self.data:
            #If the passed value is less than the parent node value
            if data < self.data:
                #If the left node value is None
                if self.left is None:
                    #Then create a left node for the parent node
                    #with this value
                    self.left = Node(data)
                else:
                    #Recursion, keep looking for a place for this value
                    #left node is now the parent node for this value
                    self.left.insert(data)
            #If the passed value is bigger than the parent node value
            elif data > self.data:
                #If the right node value is None
                if self.right is None:
                    #Then create a right node for the parent node
                    #with this value
                    self.right = Node(data)
                else:
                    #Recursion, keep looking for a place for this value
                    #right node is now the parent node for this value
                    self.right.insert(data)
        #If parent node value is none
        else:
            #Give the root node this value
            self.data = data

    # Print the tree
    #It will print from the left most to the right most
    def PrintTree(self):
        #if parent node has a left node
        if self.left:
            #Recursion, left node is now the parent node
            self.left.PrintTree()
        #Print the parent node value
        print( self.data)
        #if parent node has a right
        if self.right:
            #Recursion, right node is now the parent node
            self.right.PrintTree()

#Establish the root node
root = Node(12)
#Insert the rest of the nodes
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()
