# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, pre: List[int]) -> Optional[TreeNode]:
        root=None
        def insertval(root,target):
            if not root:
                return TreeNode(target)
            if target<root.val:
                root.left=insertval(root.left,target)
            else:
                root.right=insertval(root.right,target)
            return root
        for i in range(len(pre)):
            root=insertval(root,pre[i])
        return root
        