namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_545
{
    class Solution {
        private enum NodeType
        {
            Root,
            LeftBound,
            RightBound,
            Other
        }

        public IList<int> BoundaryOfBinaryTree(TreeNode root) {
            var result = new List<int>();
            var leftBound = new List<int>();
            var rightBound = new Stack<int>();
            var leaves = new List<int>();
            if(root is null) return result;
            Preorder(root, leftBound, rightBound, leaves, NodeType.Root);
            result = leftBound.Concat(leaves).Concat(rightBound).ToList();
            return result;
        }

        private NodeType GetLeftChildType(TreeNode node, NodeType nodeType)
        {
            switch (nodeType)
            {
                case NodeType.LeftBound:
                case NodeType.Root:
                    return NodeType.LeftBound;
                case NodeType.RightBound when node.right is null:
                    return NodeType.RightBound;
                default:
                    return NodeType.Other;
            }
        }

        private NodeType GetRightChildType(TreeNode node, NodeType nodeType)
        {
            switch (nodeType)
            {
                case NodeType.RightBound:
                case NodeType.Root:
                    return NodeType.RightBound;
                case NodeType.LeftBound when node.left is null:
                    return NodeType.LeftBound;
                default:
                    return NodeType.Other;
            }
        }

        private void Preorder(TreeNode node, IList<int> leftBound, Stack<int> rightBound, IList<int> leaves,
            NodeType nodeType)
        {
            if (node is null) return;

            switch (nodeType)
            {
                case NodeType.Root:
                case NodeType.LeftBound:
                    leftBound.Add(node.val);
                    break;
                case NodeType.RightBound:
                    rightBound.Push(node.val);
                    break;
                case NodeType.Other when node.left is null && node.right is null:
                    leaves.Add(node.val);
                    break;
            }
            Preorder(node.left, leftBound, rightBound, leaves, GetLeftChildType(node, nodeType));
            Preorder(node.right, leftBound, rightBound, leaves, GetRightChildType(node, nodeType));
        }
    }
}