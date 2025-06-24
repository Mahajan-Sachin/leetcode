# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(root==None or root==p or root==q):
            return root
        leftchild=self.lowestCommonAncestor(root.left,p,q)
        rightchild=self.lowestCommonAncestor(root.right,p,q)
        if leftchild and rightchild:
            return root
        return leftchild if leftchild else rightchild