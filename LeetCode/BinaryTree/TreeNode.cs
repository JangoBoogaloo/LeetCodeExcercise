namespace BinaryTree;

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
		var nodes = new Queue<TreeNode?>();
		nodes.Enqueue(root);
		var i = 1;
		while (i<values.Count) {
            var node = nodes.Dequeue();
			if (node is null) {
				nodes.Enqueue(null);
				nodes.Enqueue(null);
				i += 2;
				continue; 
			}
            node.left = values[i] is null ? null : new TreeNode((int)values[i]!);
            nodes.Enqueue(node.left);
			i++;
            node.right = (i < values.Count && values[i] is not null) ? new TreeNode((int)values[i]!) : null;
            nodes.Enqueue(node.right);
            i++;
        }
		return root;
	}

	public static IEnumerable<int?> ToList(TreeNode? root) {
        var result = new List<int?>();
        if (root is null) return result;
		var nodes = new Queue<TreeNode?>();
		nodes.Enqueue(root);
		var nonNullExist = true;
		while (nonNullExist) {
			var nodeCount = nodes.Count;
			nonNullExist = false;
            for (var i=0; i<nodeCount; i++)
			{
                var node = nodes.Dequeue();
                if (node is null)
                {
                    result.Add(null);
                    nodes.Enqueue(null);
                    nodes.Enqueue(null);
                }
                else
                {
	                nonNullExist = true;
	                result.Add(node.val);
	                nodes.Enqueue(node.left);
	                nodes.Enqueue(node.right);
                }
            }
		}

		for (var i = result.Count - 1; i >= 0; i--) {
			if (result[i] is not null) break;
			result.RemoveAt(i);
		}

		return result;
    }
}