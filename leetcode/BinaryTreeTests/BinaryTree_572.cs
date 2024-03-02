namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_572
{
    class Solution {
        public bool IsSubtree(TreeNode root, TreeNode subRoot) {
            var rootTree = TreeToString(root);
            var subRootTree = TreeToString(subRoot);
            return rootTree.Contains(subRootTree);
        }

        private string TreeToString(TreeNode node) {
            if(node is null) return "n";
            var treeStr = $"\"{node.val}\"";
            treeStr += "(" + TreeToString(node.left) +")";
            treeStr += "(" + TreeToString(node.right) +")";
            return treeStr;
        }
    }
}