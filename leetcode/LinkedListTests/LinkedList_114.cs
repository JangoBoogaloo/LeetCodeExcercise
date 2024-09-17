using BinaryTree;

namespace LinkedListTests;

[TestFixture]
internal class LinkedList_114
{
    class Solution {
        public void Flatten(TreeNode root) {
            if (root is null) return;

            while (root is not null)
            {
                if (root.left is not null)
                {
                    var rightMost = root.left;
                    while (rightMost.right is not null)
                    {
                        rightMost = rightMost.right;
                    }

                    rightMost.right = root.right;
                    root.right = root.left;
                    root.left = null;
                }

                root = root.right;
            }
        }
    }
}