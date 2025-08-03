class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        inorder_vals = []

        # Step 1: Get inorder traversal into a list
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            inorder_vals.append(node.val)
            inorder(node.right)
        
        inorder(root)

        # Step 2: Sort the values (correct inorder)
        inorder_vals.sort()

        # Step 3: Traverse again and overwrite wrong values
        self.i = 0  # use self to persist i across recursion

        def correct_tree(node):
            if not node:
                return
            correct_tree(node.left)
            node.val = inorder_vals[self.i]
            self.i += 1
            correct_tree(node.right)
        
        correct_tree(root)
