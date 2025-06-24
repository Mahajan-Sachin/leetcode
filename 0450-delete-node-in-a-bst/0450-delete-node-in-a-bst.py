# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minvalue(self,node):
        current=node
        while(current and current.left):
            current=current.left
        return current
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        #left exist
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            #1 child exist, let say left
            if root.left and not root.right:
                return root.left
            #if right exists not left
            if root.right and not root.left:
                return root.right
            # if both dont exist means root is leaf
            if not root.left and not root.right:
                return None
            #both exist
            else:
                success=self.minvalue(root.right)
                root.val=success.val
                root.right=self.deleteNode(root.right,root.val)
        return root

            
