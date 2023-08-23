namespace BinaryTree;

public static class PerfectTreeNodeExtensions
{
    public static void ConnectPerfect(this TreeNode? root)
    {
        if(root is null) return;
        Traverse(root.left, root.right);

        void Traverse(TreeNode? node1, TreeNode? node2) {
            if(node1 is null || node2 is null) return;
            node1.next = node2;
            Traverse(node1.left, node1.right);
            Traverse(node1.right, node2.left);
            Traverse(node2.left, node2.right);
        }
    }

    public static IEnumerable<int?> PerfectToList(this TreeNode? root)
    {
        var result = new List<int?>();
        if (root is null) return result;
        var nodes = new Queue<TreeNode?>();
        nodes.Enqueue(root);
        while (nodes.Count >0) {
            var nodeCount = nodes.Count;
            for (var i=0; i<nodeCount; i++)
            {
                var node = nodes.Dequeue();
                result.Add(node!.val);
                if(node.next is null) result.Add(null);
                if(node.left is not null) nodes.Enqueue(node.left);
                if(node.right is not null) nodes.Enqueue(node.right);
            }
        }

        return result;
    }
}