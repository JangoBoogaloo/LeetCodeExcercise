namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_199
{
    class Solution {
        public IList<int> RightSideView(TreeNode root) {
            var result = new List<int>();
            var queue = new Queue<TreeNode>();
            if (root is null) return result;
            queue.Enqueue(root);
            while (queue.Any())
            {
                var levelCount = queue.Count;
                for (var i = 0; i < levelCount; i++)
                {
                    var node = queue.Dequeue();
                    if (i == 0)
                    {
                        result.Add(node.val);
                    }

                    if (node.right is not null)
                    {
                        queue.Enqueue(node.right);
                    }
                    if (node.left is not null)
                    {
                        queue.Enqueue(node.left);
                    }
                }
            }

            return result;
        }
    }
}