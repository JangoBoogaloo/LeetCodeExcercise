namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_257
{
    private class Solution {
        public IList<string> BinaryTreePaths(TreeNode root) {
            List<string> result = new List<string>();
            DFS(root, "", result);
            return result;
        }

        private void DFS(TreeNode node, string path, List<string> result) {
            if (node == null) return;
            path += node.val.ToString();
            if (node.left == null && node.right == null) {
                result.Add(path);
            } else {
                DFS(node.left, path + "->", result);
                DFS(node.right, path + "->", result);
            }
        }
    }
}