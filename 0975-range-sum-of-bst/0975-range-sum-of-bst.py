# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        node=root
        if not node:
            return 0
        elif node.val<low:
            return self.rangeSumBST(node.right,low,high)
        elif node.val>high:
            return self.rangeSumBST(node.left,low,high)
        elif low<=node.val<=high:
            return (node.val+self.rangeSumBST(node.right,low,high)+self.rangeSumBST(node.left,low,high))
                