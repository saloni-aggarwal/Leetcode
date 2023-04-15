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
    public boolean check(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) {
            return true;
        }
        else if (root == null || subRoot == null) {
            return false;
        }
        else if (root.val != subRoot.val) {
            return false;
        }
        return check(root.right, subRoot.right) && check(root.left, subRoot.left);
    }
    
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        // if (root == null && subRoot == null) {
        //     return true;
        // }
        if(root == null) {
            return false;
        }
        if(root.val == subRoot.val && check(root, subRoot))
            return true;
       
        return (isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot));
        
        
    }
}