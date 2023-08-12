using System;
namespace BinaryTree
{
	public class TreeNode
	{
		public int val;
		public TreeNode? left;
		public TreeNode? right;
		public TreeNode(int val = 0, TreeNode? left=null, TreeNode? right=null)
		{
			this.val = val;
			this.left = left;
			this.right = right;
		}

		public static TreeNode? BuildTree(IReadOnlyList<int?> values) {
			if (values.Count == 0) return null;
            var root = new TreeNode((int)values[0]!);
			var nodes = new Queue<TreeNode>();
			nodes.Enqueue(root);
			var i = 1;
			while (i < values.Count) {
                var node = nodes.Dequeue();
				if (values[i] is not null) {
					node.left = new TreeNode((int)values[i]!);
					nodes.Enqueue(node.left);
                }
				i++;
                if (i < values.Count && values[i] is not null)
                {
                    node.right = new TreeNode((int)values[i]!);
                    nodes.Enqueue(node.right);
                }
				i++;
            }
			return root;
		}

		public static IReadOnlyList<int?> ToList(TreeNode? root) {
            var result = new List<int?>();
            if (root is null) return result;
			var nodes = new Queue<TreeNode?>();
			nodes.Enqueue(root);
			while (nodes.Count > 0) {
				var node = nodes.Dequeue();
				if (node is null)
				{
					result.Add(null);
				}
				else {
                    result.Add(node.val);
					nodes.Enqueue(node.left);
                    nodes.Enqueue(node.right);
                }
			}

			for (int i = result.Count - 1; i >= 0; i--) {
				if (result[i] is not null) break;
				result.RemoveAt(i);
			}

            return result;
        }
	}
}

