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
    int getHeight(TreeNode* root) {
        if (root == NULL) return 0;
        int lHeight = getHeight(root->left);
        int rHeight = getHeight(root->right);
        if (abs(lHeight - rHeight) > 1 || lHeight == -1 || rHeight == -1) return -1;
        return (1 + max(lHeight, rHeight));
    }
    bool isBalanced(TreeNode* root) {
        if (root == NULL) return true;
        if (getHeight(root) == -1) return false;
        return true;
    }
};