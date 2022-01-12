# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def getSum(root,curr=''):
    if not root:
        return
    if not root.left and not root.right:
        getSum.ans+=int(curr+str(root.val),2)
        return
    getSum(root.left,curr+str(root.val))
    getSum(root.right,curr+str(root.val))
    

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        getSum.ans = 0
        getSum(root)
        return getSum.ans