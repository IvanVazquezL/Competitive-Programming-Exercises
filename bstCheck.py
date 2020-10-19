""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def checkBST(root):
    return checkBSTo(root, None, None)

def checkBSTo(root,min,max):
    if root==None:
        return "Yes"
    if ((min is not None and root.data <=min)) or ((max is not None and root.data > max)):
        return "No"
    if not(checkBSTo(root.left,min,root.data)) or not(checkBSTo(root.right,root.data,max)):
        return "No"
    return "Yes"
###########
def checkBST(root):
    return check(root,float('inf'),float('-inf'))

def check(node,min,max):
    if(node==None):
        return "Yes"
    return min < node.data and node.data < max and check(node.left, min, node.data) and check(node.right,node.data,max)
    #############
    # if(node.data <= min or node.data >=max):
    #     return "No"
    #
    # return check(node.left,min,node.data) and check(node.right,node.data,max)
