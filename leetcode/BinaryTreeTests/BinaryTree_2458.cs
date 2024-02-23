namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_2458
{
    private class Solution {
        public int[] TreeQueries(TreeNode root, int[] queries) {
            var seen = new int[100001];
            var result = new int[queries.Length];
            var seenMaxHeight = 0;
            var fromLeft = true;
            Dfs(root, 0);
            seenMaxHeight = 0;
            fromLeft = false;
            Dfs(root, 0);
            for(var i=0; i<queries.Length; i++)
            {
                result[i] = seen[queries[i]];
            }
            return result;

            void Dfs(TreeNode node, int height) {
                if(node is null) return;
                //compare the previous traversal max height recrod, with this traversal max height
                seen[node.val] = Math.Max(seenMaxHeight, seen[node.val]);
                seenMaxHeight = Math.Max(seenMaxHeight, height);
                if (fromLeft) {
                    Dfs(node.left, height+1);
                    Dfs(node.right, height+1);
                } 
                else {
                    Dfs(node.right, height+1);
                    Dfs(node.left, height+1);
                }
            }
        }
    }
}