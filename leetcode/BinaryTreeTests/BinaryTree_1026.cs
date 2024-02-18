namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_1026
{
    private class Solution {
        public int MaxAncestorDiff(TreeNode root) {
            var result = 0;
            TraverseRecursive(root);
            return result;

            (int, int) TraverseRecursive(TreeNode node) {
                if(node is null) return (int.MaxValue, int.MinValue);

                var (leftMin, leftMax) = TraverseRecursive(node.left);
                var (rightMin, rightMax) = TraverseRecursive(node.right);
                var treeMin = Math.Min(node.val, Math.Min(leftMin, rightMin));
                var treeMax = Math.Max(node.val, Math.Max(leftMax, rightMax));

                var rootMinDiff = Math.Abs(node.val-treeMin);
                var rootMaxDiff = Math.Abs(node.val-treeMax);
                var rootMaxResult = Math.Max(rootMinDiff, rootMaxDiff);
                result = Math.Max(result, rootMaxResult);
                return (treeMin, treeMax);
            }
        }
    }
}