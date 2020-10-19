class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insertion(self,cur,val):
        #If cur doesn't exist
        if not cur:
            #Create a node with the passed value
            cur = Node(val)
        #If the value of cur is bigger than the passed value
        elif cur.info > val:
            #Left node of cur is recursive function
            #With left empty node of cur sent and the value
            cur.left = self.insertion(cur.left,val)
        else:
            #Right node of cur is recursive function
            #With right empty node of cur sent and the value
            cur.right = self.insertion(cur.right,val)

        return cur

    def insert(self, val):
        #If node root is None
        if self.root==None:
            #Create a node with the passed value
            #And establish it as the root node
            self.root = Node(val)
        else:
            #Send root node and value to insertion function
            self.insertion(self.root,val)




tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
