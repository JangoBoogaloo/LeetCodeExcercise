namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_2385
{
    private class SolutionBFS
    {
        public int AmountOfTime(TreeNode root, int start)
        {
            if (root is null) return 0;
            var startNode = ConvertToStartGraph(root, start);
            var visited = new HashSet<Node>();
            var queue = new Queue<Node>();
            queue.Enqueue(startNode);
            visited.Add(startNode);
            var time = 0;
            while (queue.Any())
            {
                var levelSize = queue.Count;
                var newPath = false;
                for (var i = 0; i < levelSize; i++)
                {
                    var curr = queue.Dequeue();
                    if (curr.parent is not null && !visited.Contains(curr.parent))
                    {
                        queue.Enqueue(curr.parent);
                        visited.Add(curr.parent);
                        newPath = true;
                    }

                    if (curr.left is not null && !visited.Contains(curr.left))
                    {
                        queue.Enqueue(curr.left);
                        visited.Add(curr.left);
                        newPath = true;
                    }

                    if (curr.right is not null && !visited.Contains(curr.right))
                    {
                        queue.Enqueue(curr.right);
                        visited.Add(curr.right);
                        newPath = true;
                    }
                }

                if (newPath)
                {
                    time++;
                }
            }

            return time;
        }

        private Node ConvertToStartGraph(TreeNode root, int start)
        {
            var newRoot = new Node(root);
            newRoot.parent = null;
            var queue = new Queue<Node>();
            queue.Enqueue(newRoot);
            Node startNode = null;
            while (queue.Count > 0)
            {
                var currNode = queue.Dequeue();
                if (currNode.node.val == start)
                {
                    startNode = currNode;
                }

                if (currNode.node.left is not null)
                {
                    currNode.left = new Node(currNode.node.left, currNode);
                    queue.Enqueue(currNode.left);
                }

                if (currNode.node.right is not null)
                {
                    currNode.right = new Node(currNode.node.right, currNode);
                    queue.Enqueue(currNode.right);
                }
            }

            return startNode;
        }

        private class Node
        {
            public TreeNode node;
            public Node parent;
            public Node left;
            public Node right;

            public Node(TreeNode node, Node parent = null, Node left = null, Node right = null)
            {
                this.node = node;
                this.parent = parent;
                this.left = left;
                this.right = right;
            }
        }
    }

    private class SolutionDFS
    {
        public int AmountOfTime(TreeNode root, int start)
        {
            var maxDistance = 0;
            TraverseRecursive(root);
            return maxDistance;

            int TraverseRecursive(TreeNode node)
            {
                var depth = 0;
                if (node is null) return depth;

                // walk through sub tree first before checking
                var leftDepth = TraverseRecursive(node.left);
                var rightDepth = TraverseRecursive(node.right);

                var startInSubTrees = leftDepth < 0 || rightDepth < 0;

                if (node.val == start)
                {
                    maxDistance = Math.Max(leftDepth, rightDepth);
                    depth = -(depth+1);
                } else if (startInSubTrees)
                {
                    var distance = Math.Abs(leftDepth) + Math.Abs(rightDepth);
                    maxDistance = Math.Max(distance, maxDistance);
                    //we only take the start path, so here we are looking for a negative depth in subtree
                    depth = Math.Min(leftDepth, rightDepth) - 1;
                }
                else
                {
                    depth = Math.Max(leftDepth, rightDepth) + 1;
                }

                return depth;
            }
        }
    }
}