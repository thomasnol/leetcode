/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* cur = root;
        while (true) {
            if (cur->val == p->val) { return p; break; }
            if (cur->val == q->val) { return q; break; }
            if (cur->val < p->val && cur->val < q->val) {
                cur = cur->right;
            } else if (cur->val > p->val && cur->val > q->val) {
                cur = cur->left;
            } else {
                return cur;
            }
        }
    }
};