namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_987
{
    private class Solution {
        public IList<IList<int>> VerticalTraversal(TreeNode root) {
            // Track the vertical plane we're on, as well as the depth (for ordering final results)
            int verticalPlane = 0;
            int depth = 0;
            Dictionary<int, List<(int, int)>> res = new Dictionary<int, List<(int, int)>>();
    
            // Breadth first search
            Queue<(TreeNode, int)> queue = new Queue<(TreeNode, int)>();
            queue.Enqueue((root, verticalPlane));
            while (queue.Any())
            {
                int count = queue.Count();
                int i = 0;
                while (i < count)
                {
                    // Add current node to result dictionary with depth. The key is the vertical plane we're on
                    var curr = queue.Dequeue();
                    res.TryAdd(curr.Item2, new List<(int, int)>());
                    res[curr.Item2].Add((curr.Item1.val, depth));
    
                    // Enqueue left, with side variable decremented
                    if (curr.Item1.left != null)
                    {
                        queue.Enqueue((curr.Item1.left, curr.Item2 - 1));
                    }
    
                    // Enqueue right, with side variable incremented
                    if (curr.Item1.right != null)
                    {
                        queue.Enqueue((curr.Item1.right, curr.Item2 + 1));
                    }
                    i++;
                }
    
                depth++;
            }
    
            // Order results by vertical plane
            List<IList<int>> ans = new List<IList<int>>();
            res = res.OrderBy(x => x.Key).ToDictionary(k => k.Key, v => v.Value);
            foreach (var v in res.Values)
            {
                // In each vertical set, order by level, and then by node val
                ans.Add(v.OrderBy(x => x.Item2).ThenBy(x => x.Item1).Select(x => x.Item1).ToList());
            }
    
            return ans;
        }
    }
}
