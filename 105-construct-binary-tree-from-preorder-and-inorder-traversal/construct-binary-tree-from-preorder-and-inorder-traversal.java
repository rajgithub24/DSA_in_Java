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
        return helper(0, 0, inorder.length-1, preorder, inorder);
    }
    public TreeNode helper(int prestart, int Start, int End, int[] preorder, int[] inorder){
        if(prestart > preorder.length-1 || Start > End) return null;
        TreeNode root = new TreeNode(preorder[prestart]);
        
        int inIndex = 0;
        for(int i = Start ; i <= End; i++ ){
            if(inorder[i] == root.val){
             inIndex = i;
            }
        }
        
        root.left = helper(prestart +1, Start, inIndex-1, preorder, inorder);
        root.right = helper(prestart + inIndex - Start +1, inIndex+1, End, preorder, inorder);
        return root;
    }
}