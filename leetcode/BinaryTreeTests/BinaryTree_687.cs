namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_687
{
    private class Solution
    {
        private int longestPath = 0;

        public int LongestUnivaluePath(TreeNode root)
        {
            longestPath = 0;
            GetLongestArrowPath(root);
            return longestPath;
        }

        private int GetLongestArrowPath(TreeNode node)
        {
            if (node is null) return 0;

            var leftSubtreeArrowPath = GetLongestArrowPath(node.left);
            var rightSubtreeArrowPath = GetLongestArrowPath(node.right);

            var treeTakeLeftArrowPath = 0;
            if (node.left is not null && node.left.val == node.val)
            {
                //         node
                //        /
                //leftTree
                treeTakeLeftArrowPath = leftSubtreeArrowPath + 1;
            }

            var treeTakeRightArrowPath = 0;
            if (node.right is not null && node.right.val == node.val)
            {
                //   node
                //       \
                //       rightTree
                treeTakeRightArrowPath = rightSubtreeArrowPath + 1;
            }

            longestPath = Math.Max(longestPath, treeTakeLeftArrowPath + treeTakeRightArrowPath);

            return Math.Max(treeTakeLeftArrowPath, treeTakeRightArrowPath);
        }
    }
}