using BinaryTree;

namespace BinaryTreeTests;

[TestFixture]
public class ConstructBinaryTree_889
{
    private static IReadOnlyList<ConstructBinaryTreeTestCase> _constructBinaryTree889TestCase = new[]
    {
        new ConstructBinaryTreeTestCase()
        {
            Preorder = new[] { 1, 2, 4, 5, 3, 6, 7 },
            PostOrder = new [] { 4, 5, 2, 6, 7, 3, 1},
            Expected = new int?[] { 1, 2, 3, 4, 5, 6, 7 },
        }
    };

    [TestCaseSource(nameof(_constructBinaryTree889TestCase))]
    public void TestConstructBinaryTree_889(ConstructBinaryTreeTestCase testCase)
    {
        var solution = new Solution();
        var tree = solution.ConstructFromPrePost(testCase.Preorder!, testCase.PostOrder!);
        var actual = TreeNode.ToList(tree).ToArray();
        CollectionAssert.AreEqual(actual, testCase.Expected);
    }

    class Solution
    {
        public TreeNode ConstructFromPrePost(int[] preorder, int[] postorder) {
            if(!preorder.Any() || !postorder.Any()) return null;
            var root = new TreeNode(preorder[0]);
            if (preorder.Length == 1) return root;
            var leftRootIndex = Array.IndexOf(postorder, preorder[1]);
            root.left = ConstructFromPrePost(preorder[1..(leftRootIndex+2)], postorder[..(leftRootIndex+1)]);
            root.right = ConstructFromPrePost(preorder[(leftRootIndex+2)..], postorder[(leftRootIndex+1)..^1]);
            return root;
        }
    }
}