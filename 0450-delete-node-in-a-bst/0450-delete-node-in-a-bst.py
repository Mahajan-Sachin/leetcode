# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mini(self,node):
        while node.left:
            node=node.left
        return node
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
        elif key==root.val:
            if not root.left and root.right:
                return root.right
            elif not root.right and root.left:
                return root.left
            elif not root.left and not root.right:
                return None
            elif root.left and root.right:
                succesor=self.mini(root.right)
                root.val=succesor.val
                root.right=self.deleteNode(root.right,root.val)
        return root
        