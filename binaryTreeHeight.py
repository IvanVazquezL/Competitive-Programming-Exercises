class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    #Initialize counter of the height of the left side
    heightLeft = 0
    #Initialize counter of the height of the right side
    heightRight = 0
    #If the parent node has a left node
    if root.left:
        #Increment heightLeft with one and
        #Go into recursion with the left node as
        #the new parent node
        heightLeft = 1 + height(root.left)
    #If the parent node has a right node
    if root.right:
        #Increment heightRight with one and
        #Go into recursion with the right node as
        #the new parent node
        heightRight = 1 + height(root.right)

    #Return the highest of the heights
    if heightLeft > heightRight:
        return heightLeft
    else:
        return heightRight



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
