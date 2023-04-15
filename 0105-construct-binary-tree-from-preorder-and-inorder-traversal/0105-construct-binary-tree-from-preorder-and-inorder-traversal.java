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
    public TreeNode helper(List<Integer> preorder, List<Integer> inorder) {
        
        if(preorder.isEmpty())
            return null;
        
        else if(preorder.size() == 1) {
            return new TreeNode(preorder.get(0));
        }
        
        else {
            int index = inorder.indexOf(preorder.get(0));
            TreeNode root = new TreeNode(preorder.get(0));
            root.left = helper(preorder.subList(1,index+1), inorder.subList(0,index));
            root.right = helper(preorder.subList(index+1, preorder.size()), inorder.subList(index+1, inorder.size()));
            return root;
        }
    }
    
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        
        List<Integer> preOrder = new ArrayList<>();
        List<Integer> inOrder = new ArrayList<>();
        for(int p: preorder) preOrder.add(p);
        for(int i: inorder) inOrder.add(i);
        
        return helper(preOrder, inOrder);
        
    }
}