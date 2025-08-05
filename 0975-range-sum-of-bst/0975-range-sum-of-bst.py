# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        List=[]
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            List.append(root.val)
            inorder(root.right)
        inorder(root)
        index1=List.index(low)
        index2=List.index(high)
        ans=sum(List[index1:index2+1])
        return ans