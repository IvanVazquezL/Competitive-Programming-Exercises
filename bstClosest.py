class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def closest_value(root, target):
    #a has the value of root
    a = root.val
    #if the target number is lower than the value of root
    #then kid is root left node else kid is root right node
    kid = root.left if target < a else root.right
    #If the nodes are None
    if not kid:
        #return the value of root
        return a
    #if the nodes are not None, b is recursion of this function
    #with the kid as the new root and send the target
    b = closest_value(kid, target)
    #lambda function to check the absolute value of the subtraction
    #of the target number with a parent node and one of its child nodes
    #the function return the node value associated with the lowest of
    #the subtractions
    return min((a,b), key=lambda x: abs(target-x))

root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(14)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(8)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(24)
root.right.right.left = TreeNode(22)

result = closest_value(root, 19)
print(result)
