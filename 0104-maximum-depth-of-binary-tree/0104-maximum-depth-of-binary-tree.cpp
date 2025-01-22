/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) {
        return 0; // Base case: If the node is null, depth is 0
    }
    int leftDepth = maxDepth(root->left);   // Recursively find depth of left subtree
    int rightDepth = maxDepth(root->right); // Recursively find depth of right subtree
    return max(leftDepth, rightDepth) + 1;  // Return the maximum depth plus one
    }
};