# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# def insert(root,val):
#     if not root:
#         return TreeNode(val)
#     if root.val < val:
#         root.right = insert(root.right,val)
#     else:
#         root.left = insert(root.left,val)
#     return root
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        temp = root
        while temp:
            if temp.val<val:
                if temp.right==None:
                    temp.right = TreeNode(val)
                    break
                temp = temp.right
            else:
                if temp.left == None:
                    temp.left = TreeNode(val)
                    break
                temp = temp.left
            
        return root
            
        
        