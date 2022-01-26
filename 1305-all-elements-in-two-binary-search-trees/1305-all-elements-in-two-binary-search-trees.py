# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(root):
    
    if not root:
        return None
    helper(root.left)
    
    helper.in1.append(root.val)
    helper(root.right)

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        helper.in1 = []
        helper(root1)
        helper(root2)
        return sorted(helper.in1)