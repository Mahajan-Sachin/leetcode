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
    int count=0;
public:
    int countNodes(TreeNode* root) {
        if (root==NULL){
            return 0;
        }
        if (root->left!=NULL){
            count++;
            countNodes(root->left);
        }
        if (root->right!=NULL){
            count++;
            countNodes(root->right);
        }
        return count+1;
    }
};