using BinaryTree;

namespace BinaryTreeTests;

[TestFixture]
class BinaryTreeQuestion_116
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
        var solution = new Solution1();
        tree = solution.Connect(tree);
        var actual = tree.PerfectToList().ToArray();
        CollectionAssert.AreEqual(testCase.Expected, actual);
    }

    class Solution1
    {
        public TreeNode? Connect(TreeNode? root)
        {
            if(root is null) return null;
            Traverse(root.left, root.right);
            return root;

            void Traverse(TreeNode? node1, TreeNode? node2) {
                if(node1 is null || node2 is null) return;
                node1.next = node2;
                Traverse(node1.left, node1.right);
                Traverse(node1.right, node2.left);
                Traverse(node2.left, node2.right);
            }
        }
    }
}