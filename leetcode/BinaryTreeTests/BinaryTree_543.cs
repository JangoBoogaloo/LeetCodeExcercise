namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_543
{
    private class Solution {
        public int DiameterOfBinaryTree(TreeNode root) {
            int diameterResult = 0;
            TreeMaxHeight(root);
            return diameterResult;
        
            int TreeMaxHeight(TreeNode root) {
                if(root is null) { return 0; }
                var leftH = TreeMaxHeight(root.left);
                var rightH = TreeMaxHeight(root.right);
                var diameter = leftH+rightH;
                diameterResult = Math.Max(diameterResult, diameter);
                return Math.Max(leftH, rightH) + 1;
            }
        }
    }
}