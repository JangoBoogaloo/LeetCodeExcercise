namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_314 {
    class Solution
    {
        public IList<IList<int>> VerticalOrder(TreeNode root)
        {
            var res = new List<IList<int>>();
            var minColumn = 0;
            var maxColumn = 0;
            if (root is null) return res;

            var columnTable = new Dictionary<int, List<int>>();
            var queue = new Queue<(TreeNode, int)>();
            queue.Enqueue((root, 0));
            while (queue.Any())
            {
                var (node, column) = queue.Dequeue();
                if (node is null) continue;
                if (!columnTable.ContainsKey(column))
                {
                    columnTable[column] = new List<int>();
                }
                columnTable[column].Add(node.val);

                if (node.left is not null)
                {
                    queue.Enqueue((node.left, column - 1));
                    minColumn = Math.Min(minColumn, column - 1);
                }
                if (node.right is not null)
                {
                    queue.Enqueue((node.right, column + 1));
                    maxColumn = Math.Max(maxColumn, column + 1);
                }
            }
            for (var i = minColumn; i < maxColumn + 1; i++)
            {
                res.Add(columnTable[i]);
            }

            return res;
        }
    }
}
