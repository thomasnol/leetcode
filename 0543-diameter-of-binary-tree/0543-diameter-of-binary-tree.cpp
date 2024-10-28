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
    int findDiameter(TreeNode* root, int& currMax) {
        if (root->left == NULL && root->right == NULL) return 0;
        if (root->left == NULL || root->right == NULL) {
            if (root->left == NULL) return findDiameter(root->right, currMax) + 1;
            else return findDiameter(root->left, currMax) + 1;
        } else {
            int left = findDiameter(root->left, currMax);
            int right = findDiameter(root->right, currMax);
            currMax = max(currMax, left + right + 2);
            return max(left, right) + 1;
        }
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int currMax = 0;
        int res = findDiameter(root, currMax);
        return max(res, currMax);
    }
};