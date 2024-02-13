namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_606
{
    private class SolutionRecursive {
        public string Tree2str(TreeNode root) {
            if(root is null) return "";
            var str = $"{root.val}";
            if(root.left is not null) {
                str = str+"("+Tree2str(root.left)+")";
                if(root.right is not null) {
                    str = str+"("+Tree2str(root.right)+")";
                }
            } else if(root.right is not null) {
                str = str+"()("+Tree2str(root.right)+")";
            }
            return str;
        }
    }
}