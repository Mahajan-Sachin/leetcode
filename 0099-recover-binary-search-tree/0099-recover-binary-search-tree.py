# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        List=[]
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            List.append(root.val)
            inorder(root.right)
        inorder(root)
        List.sort()
        i=0
        def correct(root):
            nonlocal i
            if not root:
                return None
            correct(root.left)
            root.val=List[i]
            i+=1
            correct(root.right)
        correct(root)

    