namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_236
{
    private class Solution {
        public TreeNode LowestCommonAncestor(TreeNode? root, TreeNode? p, TreeNode? q)
        {
            return FindLCAForNodes(root, p, q);
        }

        private TreeNode? FindLCAForNodes(TreeNode? node, TreeNode? p, TreeNode? q)
        {
            //We reach end of this path
            if (node is null) return null;

            // We find p node, it is ancestor of itself
            if (node == p) return node;
            
            // We find q node, it is ancestor of itself
            if (node == q) return node;

            var leftTreeLCA = FindLCAForNodes(node.left, p, q);
            var rightTreeLCA = FindLCAForNodes(node.right, p, q);
            
            //One of p, q in left tree and one of p, q in right tree
            if(leftTreeLCA != null && rightTreeLCA != null) return node;
            
            return leftTreeLCA ?? rightTreeLCA;
        }
    }
}
