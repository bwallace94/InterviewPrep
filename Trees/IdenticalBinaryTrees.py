# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A == None and B == None:
            return 1
        if A == None or B == None:
            return 0
        if A.left == None and B.left == None and A.right == None and B.right == None:
            return A.val == B.val
        levelA = [A]
        levelB = [B]
        while levelA != [] and levelB != []:
            newlevelA = []
            newlevelB = []
            if len(levelA) != len(levelB):
                return 0
            for i in range(len(levelA)):
                nodeA = levelA[i]
                nodeB = levelB[i]
                if nodeA.val != nodeB.val:
                    return 0
                if nodeA.left != None:
                    newlevelA.append(nodeA.left)
                if nodeA.right != None:
                    newlevelA.append(nodeA.right)
                if nodeB.left != None:
                    newlevelB.append(nodeB.left)
                if nodeB.right != None:
                    newlevelB.append(nodeB.right)
            levelA = newlevelA
            levelB = newlevelB
        if not (levelA == [] and levelB == []):
            return 0
        return 1
