namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_404
{
    private class Solution {
        public int SumOfLeftLeaves(TreeNode? root) {
            var sum = 0;
            if (root is null) return 0;

            if (root.left != null &&
                root.left.left == null &&
                root.left.right == null)
                sum += root.left.val;

            sum+=SumOfLeftLeaves(root.left);
            sum+=SumOfLeftLeaves(root.right);
            return sum;
        }
    }
}