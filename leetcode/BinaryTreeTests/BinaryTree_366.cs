namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_366
{
    private class Solution {
        public IList<IList<int>> FindLeaves(TreeNode root) {
            var solution = new List<IList<int>>();
            GetHeight(root);
            return solution;

            int GetHeight(TreeNode root) {
                if (root is null) return -1;

                var leftHeight = GetHeight(root.left);
                var rightHeight = GetHeight(root.right);

                var currHeight = Math.Max(leftHeight, rightHeight) + 1;

                if(solution.Count == currHeight) {
                    solution.Add(new List<int>());
                }
                solution[currHeight].Add(root.val);
                return currHeight;
            }
        }
    }   
}

