namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_285
{
    private class Solution {
        public TreeNode InorderSuccessor(TreeNode root, TreeNode p) {
            TreeNode successor = null;
        
            while (root is not null) {
            
                if (p.val >= root.val) {
                    root = root.right;
                } else {
                    successor = root;
                    root = root.left;
                }
            }
        
            return successor;
        }
    }
}