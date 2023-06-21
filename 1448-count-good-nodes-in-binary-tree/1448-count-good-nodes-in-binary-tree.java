/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int ans = 0;
    
    public void helper(TreeNode root, int maxVal) {
        if(root.val >= maxVal) {
            maxVal = root.val;
            ans += 1;
        }
        if(root.left != null)
            helper(root.left, maxVal);
        if(root.right != null) 
            helper(root.right, maxVal);  
    }
    
    public int goodNodes(TreeNode root) {
        helper(root, Integer.MIN_VALUE); 
        return ans;
    }
}