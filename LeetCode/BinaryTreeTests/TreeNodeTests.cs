namespace BinaryTreeTests;

using BinaryTree;

public class TreeNodeTests
{
    public static IReadOnlyList<int?[]> BinaryTreeTestCases = new[]
    {
        Array.Empty<int?>(),
        new int?[] { 1, },
        new int?[] { 1, 2 },
        new int?[] { 1, null, 3 },
        new int?[] { 1, 2, 3, 4},
        new int?[] { 1, 2, null, 4},
        new int?[] { 1, 2, null, null, 5},
        new int?[] { 1, null, 3, null, null, 6, 7},
        new int?[] { 1, 2, 3, null, 5, 6, 7},
        new int?[] { 1, 2, 3, null, null, 6, 7},
        new int?[] { 1, 2, 3, null, 5, null, 7},
    };

    [TestCaseSource(nameof(BinaryTreeTestCases))]
    public void BinaryTreeTests(int?[] expected)
    {
        var root = TreeNode.BuildTree(expected);
        var actual = TreeNode.ToList(root).ToArray();
        CollectionAssert.AreEqual(expected, actual);
    }
}
