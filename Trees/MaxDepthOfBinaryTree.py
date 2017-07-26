# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        max_found = 0
        next_level = [A]
        while next_level != []:
            new_level = []
            max_found += 1
            for node in next_level:
                if node.left != None:
                    new_level.append(node.left)
                if node.right != None:
                    new_level.append(node.right)
            next_level = new_level
        return max_found
                
                
