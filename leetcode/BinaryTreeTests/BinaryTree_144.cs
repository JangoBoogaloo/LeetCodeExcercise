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
    
    class SolutionStackIterative {
        public IList<int> PreorderTraversal(TreeNode root) {
            var result = new List<int>();
            var stack = new Stack<TreeNode>();
            if (root is null) return result;

            stack.Push(root);
            while (stack.Count > 0)
            {
                var node = stack.Pop();
                result.Add(node.val);
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