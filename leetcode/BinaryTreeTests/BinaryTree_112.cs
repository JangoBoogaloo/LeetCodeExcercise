namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_112
{
    private class Solution {
        public bool HasPathSum(TreeNode root, int targetSum) {
            if(root is null) return false;
            targetSum -= root.val;
            if(root.left is null && root.right is null) {
                return (targetSum == 0);
            }
            return HasPathSum(root.left, targetSum) || HasPathSum(root.right, targetSum);
        }
    }
}