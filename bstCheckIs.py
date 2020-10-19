class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_BST(root):
    #Empty stack to store the nodes
    stack = []
    #previous node variable equal to None
    prev = None

    #While the node is not None or the stack is empty
    while root or stack:
        #While node is not None
        while root:
            #Append the node to the stack
            stack.append(root)
            #Root is now the left node of root
            root = root.left
        #Root is now the last element appended to the stack
        root = stack.pop()
        #If prev is not None and the root value is lower or equal
        #to the value of prev, return false
        if prev and root.val <= prev.val:
            return False
        #Prev is now root
        prev = root
        #Root is now the right node of root
        root = root.right
    #Return true when their is nothing in the stack or if the
    #variable root is None
    return True

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

result = is_BST(root)
print(result)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

result = is_BST(root)
print(result)
