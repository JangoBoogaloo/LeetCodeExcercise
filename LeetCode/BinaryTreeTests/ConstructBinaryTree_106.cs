using BinaryTree;

namespace BinaryTreeTests;

[TestFixture]
public class ConstructBinaryTree_106
{
    private static IReadOnlyList<ConstructBinaryTreeTestCase> ConstructBinaryTree_106TestCase = new[]
    {
        new ConstructBinaryTreeTestCase()
        {
            InOrder = new[] { 9, 3, 15, 20, 7 },
            PostOrder = new []{9,15,7,20,3},
            Expected = new int?[] { 3, 9, 20, null, null, 15, 7 },
        }
    };
    
    [TestCaseSource(nameof(ConstructBinaryTree_106TestCase))]
    public void TestConstructBinaryTree_105(ConstructBinaryTreeTestCase testcase)
    {
        var solution = new Solution();
        var tree = solution.BuildTree(testcase.InOrder!, testcase.PostOrder!);
        var actual = TreeNode.ToList(tree).ToArray();
        CollectionAssert.AreEqual(testcase.Expected, actual);
    }

    private class Solution
    {
        public TreeNode BuildTree(int[] inorder, int[] postorder)
        {
            if (!inorder.Any() || !postorder.Any()) return null;

            var rootVal = postorder.Last();
            var root = new TreeNode(rootVal);
            var rootIndex = Array.IndexOf(inorder, rootVal);

            root.left = BuildTree(inorder[..rootIndex], postorder[..rootIndex]);
            root.right = BuildTree(inorder[(rootIndex + 1)..], postorder[rootIndex..^1]);
            return root;
        }
    }
}