# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(root,height):
    if not root:
        return None
    if helper.height<height:
        helper.height = height
        helper.ans.append(root.val)

    helper(root.right,height+1)
    
    helper(root.left,height+1)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        helper.ans = []
        helper.height = 0
        helper(root,1)
        return helper.ans