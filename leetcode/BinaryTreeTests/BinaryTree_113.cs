namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_113
{
    private class Solution {
        public IList<IList<int>> PathSum(TreeNode root, int targetSum) {
            var result = new List<IList<int>>();
            if(root is null) return result;
            Dfs(root, targetSum, result, new List<int>());
            return result;
        }

        private void Dfs(TreeNode node, int targetSum, IList<IList<int>> result, IList<int> currentPath)
        {
            targetSum -= node.val;
            currentPath.Add(node.val);
            if (node.left is null && node.right is null)
            {
                if(targetSum == 0) result.Add(new List<int>(currentPath));
            }

            if (node.left is not null) Dfs(node.left, targetSum, result, currentPath);
            if (node.right is not null) Dfs(node.right, targetSum, result, currentPath);

            currentPath.RemoveAt(currentPath.Count-1);
        }
    }
}