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
    private TreeNode helper(int[] preorder, int[] inorder, int Start, int End, int idx){
        if(idx > preorder.length-1 || Start > End) return null;
        TreeNode root = new TreeNode(preorder[idx]);
        
        int inIndex = 0;
        for(int i = Start ; i <= End; i++ ){
            if(inorder[i] == root.val){
             inIndex = i;
            }
        }
        
        root.left = helper(preorder, inorder, Start, inIndex-1, idx +1);
        root.right = helper(preorder, inorder, inIndex+1, End, idx + inIndex - Start +1);
        return root;
    }
}