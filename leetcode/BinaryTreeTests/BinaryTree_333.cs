namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_333
{
    class Solution {
        
        private class TreeInfo
        {
            public int MinValue;
            public int MaxValue;
            public int LargestBstNodes;
        }
        
        public int LargestBSTSubtree(TreeNode root)
        {
            var treeInfo = PostOrder(root);
            return treeInfo.LargestBstNodes;
        }

        private TreeInfo PostOrder(TreeNode? node)
        {
            var treeInfo = new TreeInfo() { MinValue = int.MaxValue, MaxValue = int.MinValue, LargestBstNodes = 0 };
            if (node is null)
            {
                return treeInfo;
            }

            var leftTreeInfo = PostOrder(node.left);
            var rightTreeInfo = PostOrder(node.right);

            //Up until now, we get a BST
            if (node.val > leftTreeInfo.MaxValue && node.val < rightTreeInfo.MinValue)
            {
                treeInfo.MinValue = Math.Min(node.val, leftTreeInfo.MinValue);
                treeInfo.MaxValue = Math.Max(node.val, rightTreeInfo.MaxValue);
                treeInfo.LargestBstNodes = 1 + leftTreeInfo.LargestBstNodes + rightTreeInfo.LargestBstNodes;
            }
            //Till this node, we dont form a BST, so we return extreme min max. Any parent form tree contains this branch will not be valid BST
            else
            {
                treeInfo.MinValue = int.MinValue;
                treeInfo.MaxValue = int.MaxValue;
                treeInfo.LargestBstNodes = Math.Max(leftTreeInfo.LargestBstNodes, rightTreeInfo.LargestBstNodes);
            }

            return treeInfo;
        }
    }
}