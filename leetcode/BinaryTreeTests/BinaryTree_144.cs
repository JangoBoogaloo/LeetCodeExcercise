namespace BinaryTreeTests;

[TestFixture]
class BinaryTree_144
{
    class SolutionRecursive {
        public IList<int> PreorderTraversal(TreeNode root) {
            var result = new List<int>();
            PreorderTraversalRecursive(root);
            return result;

            void PreorderTraversalRecursive(TreeNode root) {
                if(root is null) return;
                result.Add(root.val);
                PreorderTraversalRecursive(root.left);
                PreorderTraversalRecursive(root.right);
            }
        }
    }
}