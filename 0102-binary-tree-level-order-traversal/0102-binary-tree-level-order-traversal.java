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
    
    
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        LinkedList<TreeNode> queue = new LinkedList<>();
        
        if(root == null) {
            return ans;
        }
        
        queue.add(root);
        List<Integer> temp = new ArrayList<>();
        int track = 1;
        while (!queue.isEmpty()) {
            
            TreeNode curr = queue.remove();
            if(curr == null) {
                track -= 1;
                if(temp.size() == track && !temp.isEmpty()) {
                    ans.add(temp);
                    track *= 2;
                    temp = new ArrayList<>();
                }
                continue;
            }          
           
            temp.add(curr.val);
            
            if(temp.size() == track ) {
                ans.add(temp);
                track *= 2;
                temp = new ArrayList<>();
            }
            
            queue.add(curr.left);
            queue.add(curr.right);
            // System.out.println("curr =" +curr.val);
            // System.out.println("temp =" +temp);
            // System.out.println("track =" +track);
        }
        // if(!temp.isEmpty()) {
        //     ans.add(temp);
        // }
        
        return ans;
    }
} 