namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_270
{
    class Solution {
        public int ClosestValue(TreeNode root, double target) {
            var smallestDiff = double.MaxValue;
            var result = int.MaxValue;
            Dfs(root);
            return result;

            void Dfs(TreeNode root) {
                if(root is null) return;
                var diff = double.Abs(target - root.val);
                if(diff < smallestDiff ||
                   (diff == smallestDiff && result > root.val)) {
                    result = root.val;
                    smallestDiff = diff;
                }
                Dfs(root.left);
                Dfs(root.right);
            }
        }
    }
}