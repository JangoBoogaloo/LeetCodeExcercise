namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_865_1123
{
    class Solution_865 {
        public TreeNode? SubtreeWithAllDeepest(TreeNode root) {
            return GetLcaWithDepth(root).node;
        }

        private (TreeNode? node, int depth) GetLcaWithDepth(TreeNode? root) {
            if(root is null) return (null, 0);

            var leftResult = GetLcaWithDepth(root.left);
            var rightResult = GetLcaWithDepth(root.right);

            if(leftResult.depth > rightResult.depth) {
                //Including root node, it is 1 extra depth
                return (leftResult.node, leftResult.depth + 1);
            }

            if(rightResult.depth > leftResult.depth) {
                //Including root node, it is 1 extra depth
                return (rightResult.node, rightResult.depth + 1);
            }

            return (root, leftResult.depth +1);
        }
    }

    class Solution_1123 {
        public TreeNode? LcaDeepestLeaves(TreeNode root) {
            return GetLcaWithDepth(root).node;
        }

        private (TreeNode? node, int depth) GetLcaWithDepth(TreeNode? root) {
            if(root is null) return (null, 0);

            var leftResult = GetLcaWithDepth(root.left);
            var rightResult = GetLcaWithDepth(root.right);

            if(leftResult.depth > rightResult.depth) {
                //Including root node, it is 1 extra depth
                return (leftResult.node, leftResult.depth + 1);
            }

            if(rightResult.depth > leftResult.depth) {
                //Including root node, it is 1 extra depth
                return (rightResult.node, rightResult.depth + 1);
            }

            return (root, leftResult.depth +1);
        }
    }
}