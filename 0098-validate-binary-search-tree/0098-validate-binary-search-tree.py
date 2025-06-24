# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root,min_val=None,max_val=None):
            if not root:
                return True
            if min_val!=None and root.val<=min_val:
                return False
            if max_val!=None and root.val>=max_val:
                return False
            left=valid(root.left,min_val,root.val)
            right=valid(root.right,root.val,max_val)
            return left and right
        return valid(root)