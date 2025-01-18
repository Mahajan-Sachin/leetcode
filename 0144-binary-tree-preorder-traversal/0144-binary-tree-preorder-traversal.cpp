class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> result;
        if (!root) return result; // If the tree is empty, return an empty vector

        stack<TreeNode*> stk;
        stk.push(root);

        while (!stk.empty()) {
            TreeNode* node = stk.top();
            stk.pop();
            result.push_back(node->val); // Visit the root

            // Push right child first so that the left child is processed first
            if (node->right) stk.push(node->right);
            if (node->left) stk.push(node->left);
        }

        return result;
    }
};
