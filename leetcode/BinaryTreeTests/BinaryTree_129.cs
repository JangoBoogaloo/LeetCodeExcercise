namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_129
{
    private class Solution {
        public int SumNumbers(TreeNode root) {
            var sum = 0;
            Traverse(root, 0);
            return sum;

            void Traverse(TreeNode node, int numFromParent)
            {
                var digit = node.val;
                numFromParent += digit;
                if(node.left is not null) {
                    Traverse(node.left, numFromParent*10);
                }

                if(node.right is not null) {
                    Traverse(node.right, numFromParent*10);
                }

                if(node.left is null && node.right is null) {
                    sum += numFromParent;
                }
            }
        }
    }
}