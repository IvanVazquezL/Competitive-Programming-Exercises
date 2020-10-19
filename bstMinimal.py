class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    #If array is empty return None
    if not nums:
        return None
    #Get the middle element of the array
    mid_val = len(nums)//2
    #Create a new node with the middle element
    node = TreeNode(nums[mid_val])
    #Left node of node is recursion of this function
    #sending the array from the start until the element
    #before the middle element
    node.left = sorted_array_to_bst(nums[:mid_val])
    #Right node of node is recursion of this function
    #sending the array from the element after the middle
    #element until the end
    node.right = sorted_array_to_bst(nums[mid_val+1:])
    return node

def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)

result = sorted_array_to_bst([1, 2, 3, 4, 5, 6, 7])
preOrder(result)
