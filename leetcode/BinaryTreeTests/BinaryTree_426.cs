namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_426
{
    private class SolutionRecursive {
        public TreeNode TreeToDoublyList(TreeNode root) {
            if(root is null) return null;
            (var head, var tail) = ConstructRecursive(root);
            tail.right = head;
            head.left = tail;
            return head;

            (TreeNode, TreeNode) ConstructRecursive(TreeNode root)
            {
                if(root is null) return (null, null);

                (var leftHead, var leftTail) = ConstructRecursive(root.left);
                (var rightHead, var rightTail) = ConstructRecursive(root.right);
            
                var head = root;
                var tail = root;
                if(leftHead is not null) {
                    head = leftHead;
                    leftTail.right = root;
                    root.left = leftTail;
                }

                if(rightHead is not null) {
                    tail = rightTail;
                    rightHead.left = root;
                    root.right = rightHead;
                }

                return (head, tail);
            }
        }
    }
}