namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_979
{
    private class Solution {
        public int DistributeCoins(TreeNode root) {
            var result = 0;
            Traverse(root);
            return result;

            int Traverse(TreeNode root){
                if(root == null){
                    return 0;
                }
                int diff = root.val -1 + Traverse(root.left) + Traverse(root.right);
                result += Math.Abs(diff);
                return diff;       
            }
        }
    }
}