namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_144
{
    private class SolutionRecursive {
        public IList<int> PreorderTraversal(TreeNode? root) {
            var result = new List<int>();
            PreorderTraversalRecursive(root);
            return result;

            void PreorderTraversalRecursive(TreeNode? node) {
                if(node is null) return;
                result.Add(node.val);
                PreorderTraversalRecursive(node.left);
                PreorderTraversalRecursive(node.right);
            }
        }
    }

    private class SolutionStackIterative {
        public IList<int> PreorderTraversal(TreeNode? root) {
            var result = new List<int>();
            var stack = new Stack<TreeNode?>();
            if (root is null) return result;

            stack.Push(root);
            while (stack.Count > 0)
            {
                var node = stack.Pop();
                result.Add(node!.val);
                if (node.right is not null)
                {
                    stack.Push(node.right);
                }

                if (node.left is not null)
                {
                    stack.Push(node.left);
                }
            }

            return result;
        }
    }
}