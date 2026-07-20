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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
     return helper(preorder, inorder, 0, inorder.length-1, 0);
    }
    public TreeNode helper(int[] preorder, int[] inorder, int start, int end, int idx){
        if(start > end) return null;
        TreeNode root = new TreeNode(preorder[idx]);
        int inIndex = 0;
        for(int i= start; i<= end; i++){
            if(inorder[i] == root.val) inIndex = i;
        }
        root.left = helper(preorder, inorder, start, inIndex-1, idx+1);
        root.right = helper(preorder, inorder, inIndex+1, end, idx + inIndex - start +1);
        return root;
    }
}