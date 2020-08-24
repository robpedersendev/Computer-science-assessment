#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def tree_paths_sum(root):
    # Base case
    if (root == None): 
        return 0
    return (root.value + tree_paths_sum(root.left) + tree_paths_sum(root.right))  

