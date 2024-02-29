namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_333
{
    class Solution {
        
        private class TreeInfo
        {
            public int MinValue;
            public int MaxValue;
            
            /// <summary>
            /// the number of nodes for the largest binary search treee
            /// </summary>
            public int LargestBst;
        }
        
        public int LargestBSTSubtree(TreeNode root)
        {
            var treeInfo = PostOrder(root);
            return treeInfo.LargestBst;
        }

        private TreeInfo PostOrder(TreeNode? node)
        {
            var treeInfo = new TreeInfo() { MinValue = int.MaxValue, MaxValue = int.MinValue, LargestBst = 0 };
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
                treeInfo.LargestBst = 1 + leftTreeInfo.LargestBst + rightTreeInfo.LargestBst;
            }
            //Till this node, we dont form a BST, so we return extreme min max. Any parent form tree contains this branch will not be valid BST
            else
            {
                treeInfo.MinValue = int.MinValue;
                treeInfo.MaxValue = int.MaxValue;
                treeInfo.LargestBst = Math.Max(leftTreeInfo.LargestBst, rightTreeInfo.LargestBst);
            }

            return treeInfo;
        }
    }
}