namespace BinaryTreeTests;

[TestFixture]
class ConstructBinaryTree_105
{
    private static IReadOnlyList<ConstructBinaryTreeTestCase> _constructBinaryTree105TestCase = new[]
    {
        new ConstructBinaryTreeTestCase()
        {
            Preorder = new[] { 3, 9, 20, 15, 7 },
            InOrder = new[] { 9, 3, 15, 20, 7 },
            Expected = new int?[] { 3, 9, 20, null, null, 15, 7 },
        }
    };
    
    [TestCaseSource(nameof(_constructBinaryTree105TestCase))]
    public void TestConstructBinaryTree_105(ConstructBinaryTreeTestCase testcase)
    {
        var solution = new Solution();
        var tree = solution.BuildTree(testcase.Preorder!, testcase.InOrder!);
        var actual = TreeNode.ToList(tree).ToArray();
        CollectionAssert.AreEqual(testcase.Expected, actual);
    }

    private class Solution
    {
        public TreeNode BuildTree(int[] preorder, int[] inorder)
        {
            if(!preorder.Any() || !inorder.Any()) return null;

            var root = new TreeNode(preorder[0]);
            var rootIndex = Array.IndexOf(inorder, preorder[0]);
            root.left = BuildTree(preorder[1..(rootIndex+1)], inorder[..rootIndex]);
            root.right = BuildTree(preorder[(rootIndex+1)..], inorder[(rootIndex+1)..]);
        
            return root;
        }
    }
}