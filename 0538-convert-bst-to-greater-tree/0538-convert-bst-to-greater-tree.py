class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sumi = 0
        
        def reverse_inorder(node):
            nonlocal sumi
            if not node:
                return
            reverse_inorder(node.right)
            sumi += node.val
            node.val = sumi
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root
