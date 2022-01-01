# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(root):
    if not root:
        return float('inf'),-float('inf')
    if not root.right and not root.left:
        return root.val,root.val
         
    mini1,maxi1 = helper(root.left)
    mini2,maxi2 = helper(root.right)
    
    mini = min(mini1,mini2)
    maxi = max(maxi1,maxi2)
    
    helper.ans = max(helper.ans,max(abs(root.val-mini),abs(root.val-maxi)))
    return min(mini,root.val),max(maxi,root.val)

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        helper.ans = 0
        helper(root)
        return helper.ans