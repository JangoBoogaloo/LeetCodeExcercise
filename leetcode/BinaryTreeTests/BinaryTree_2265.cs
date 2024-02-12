namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_2265
{
    class Solution
    {
        public int AverageOfSubtree(TreeNode root)
        {
            var count = 0;
            TraverseRecrusive(root);
            return count;


            (int, int) TraverseRecrusive(TreeNode node)
            {
                if (node is null) return (0, 0);

                (var lSum, var lCount) = TraverseRecrusive(node.left);
                (var rSum, var rCount) = TraverseRecrusive(node.right);

                var treeSum = lSum + rSum + node.val;
                var treeCount = lCount + rCount + 1;

                var treeAvg = treeSum / treeCount;
                if (node.val == treeAvg) count++;

                return (treeSum, treeCount);
            }
        }
    }
}