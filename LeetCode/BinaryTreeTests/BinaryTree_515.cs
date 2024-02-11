namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_515 {
    private class Solution
    {
        public IList<int> LargestValues(TreeNode root)
        {
            var result = new List<int>();
            if (root is null) return result;
            var queue = new Queue<TreeNode>();
            queue.Enqueue(root);
            while (queue.Any())
            {
                var levelSize = queue.Count;
                var largest = int.MinValue;
                for (var i = 0; i < levelSize; i++)
                {
                    var node = queue.Dequeue();
                    largest = Math.Max(largest, node.val);
                    if (node.left is not null) queue.Enqueue(node.left);
                    if (node.right is not null) queue.Enqueue(node.right);
                }
                result.Add(largest);
            }

            return result;
        }
    }
}