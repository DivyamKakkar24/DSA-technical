// Pseudo-Palindromic Paths in a Binary Tree

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
    int solve(TreeNode* root, map<int, int>& net){
        if(root == NULL) return 0;
        
        if(root->left == NULL && root->right == NULL){
            int leaf = root->val;
            
            net[leaf]++;
            int odd = 0;
            
            for(auto x: net){
                if(x.second % 2 == 1) odd++;
            }
            
            net[leaf]--;
            if(odd <= 1) return 1;
            return 0;
            
        }
        
        int a = root->val;
        
        net[a]++;
        
        int left = solve(root->left, net);
        int right = solve(root->right, net);
        
        net[a]--;
        
        return (left + right);

    }
    
    int pseudoPalindromicPaths (TreeNode* root) {
        map<int, int> net;
        
        int ans = solve(root, net);
        
        return ans;
        
    }
};