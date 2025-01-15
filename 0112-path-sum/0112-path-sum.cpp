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
    bool hasPathSum(TreeNode* root, int targetSum) {
        // Base case: if the tree is empty
        if (root == nullptr) {
            return false;
        }

        // Check if the current node is a leaf and its value matches the remaining targetSum
        if (root->left == nullptr && root->right == nullptr) {
            return root->val == targetSum;
        }

        // Recursive call for left and right subtrees with the updated targetSum
        int remainingSum = targetSum - root->val;
        return hasPathSum(root->left, remainingSum) || hasPathSum(root->right, remainingSum);
    }
};
