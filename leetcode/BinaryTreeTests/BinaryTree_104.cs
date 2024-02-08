namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_104
{
    private class SolutionRecursive {
        public int MaxDepth(TreeNode root) {
            var maxDepth = 0;
            var currentDepth = 0;
            TraverseRecursive(root);
            return maxDepth;

            void TraverseRecursive(TreeNode node) {
                if(node is null) return;
                currentDepth++;
                if(node.left is null && node.right is null) {
                    maxDepth = Math.Max(maxDepth, currentDepth);
                } else {
                    TraverseRecursive(node.left);
                    TraverseRecursive(node.right);
                }
                currentDepth--;
            }
        }
    }
}

