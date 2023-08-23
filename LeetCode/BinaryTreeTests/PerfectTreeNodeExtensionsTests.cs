using BinaryTree;

namespace BinaryTreeTests;

public class PerfectTreeNodeExtensionsTests
{
    private static IReadOnlyList<PerfectTreeNodeTestCase> _perfectTreeNodeTestCases = new[]
    {
        new PerfectTreeNodeTestCase
        {
            Input = new int?[] { 1, 2, 3, 4, 5, 6, 7 },
            Expected = new int?[] { 1, null, 2, 3, null, 4, 5, 6, 7, null }
        }
    };

    [TestCaseSource(nameof(_perfectTreeNodeTestCases))]
    public void TestPerfectTreeNodeExtensions(PerfectTreeNodeTestCase testCase)
    {
        var tree = TreeNode.BuildTree(testCase.Input);
        tree.ConnectPerfect();
        var actual = tree.PerfectToList().ToArray();
        CollectionAssert.AreEqual(testCase.Expected, actual);
    }
}


