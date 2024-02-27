namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTee_1740
{
    class Solution {
        private int result;

        public int FindDistance(TreeNode root, int p, int q) {
            if(p == q) return 0;
            result = -1;
            DfsDistanceToOneOfThem(root, p, q);
            return result;
        }

        private int DfsDistanceToOneOfThem(TreeNode root, int p, int q) {
            if(root is null) return -1;
            var leftDistance = DfsDistanceToOneOfThem(root.left, p, q);
            var rightDistance = DfsDistanceToOneOfThem(root.right, p, q);

            if(root.val == p || root.val == q) {
                if (leftDistance < 0 && rightDistance < 0) {
                    return 0;
                }
                result = 1 + (leftDistance >= 0 ? leftDistance : rightDistance);

                //We already find result, set -1 for this branch to quick return
                return -1;
            }

            //ROOT is LCA
            if (leftDistance >= 0 && rightDistance >= 0) {
                result = leftDistance + rightDistance + 2;
                return -1;
            }

            if (leftDistance >= 0) {
                return leftDistance + 1;
            }
            if (rightDistance >= 0) {
                return rightDistance + 1;
            }

            //p and q are not found in this tree
            return -1;
        }
    }
}