namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_1382
{
    private class Solution {
        public TreeNode BalanceBST(TreeNode root) {
            var sortedList = new List<int>();
            if(root is null) return null;
            Inorder(root);
            return BuildTree(sortedList, 0, sortedList.Count-1);

            void Inorder(TreeNode node)
            {
                if(node is null) return;
                Inorder(node.left);
                sortedList.Add(node.val);
                Inorder(node.right);
            }

            TreeNode BuildTree(IList<int> sortedList, int left, int right) {
                if(left > right) return null;
                var mid = left + (right-left) /2;
                var node = new TreeNode(sortedList[mid]);
                node.left = BuildTree(sortedList, left, mid-1);
                node.right = BuildTree(sortedList, mid+1, right);
                return node;
            }
        }
    }
}