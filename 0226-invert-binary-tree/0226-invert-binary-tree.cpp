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
    TreeNode* invertTree(TreeNode* root) {
        /*
        do a BF traversal
        for every node encountered, swap the left with the right via a temp TreeNode*
        */
        if (root == nullptr) return nullptr;
        queue<TreeNode*> nodesToProcess;
        nodesToProcess.push(root);
        while (!nodesToProcess.empty()) {
            TreeNode* cur = nodesToProcess.front();
            nodesToProcess.pop();

            TreeNode* temp = cur->left;
            cur->left = cur->right;
            cur->right = temp;

            if (cur->left) {
                nodesToProcess.push(cur->left);
            }
            if (cur->right) {
                nodesToProcess.push(cur->right);
            }
        }
        return root;
    }
};