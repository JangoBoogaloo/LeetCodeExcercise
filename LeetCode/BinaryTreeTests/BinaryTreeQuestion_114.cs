using BinaryTree;

namespace BinaryTreeTests;

[TestFixture]
class BinaryTreeQuestion_114
{
    private static IReadOnlyList<TestCase_114> _testCase114 = new[]
    {
        new TestCase_114
        {
            Input = new int?[] { 1, 2, 5, 3, 4, null, 6 },
            Expected = new int?[]
            {
                1, null, 2,
                null, null, null, 3,
                null, null, null, null, null, null, null, 4,
                null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 5,
                null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
                null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 6
            }
        }
    };

    [TestCaseSource(nameof(_testCase114))]
    public void TestQuestion_114_Solution1(TestCase_114 testCase114)
    {
        var solution = new Solution1();
        var tree = TreeNode.BuildTree(testCase114.Input);
        solution.Flatten(tree);
        var actual = TreeNode.ToList(tree).ToArray();
        CollectionAssert.AreEqual(testCase114.Expected, actual);
    }

    public class TestCase_114
    {
        public int?[] Input;
        public int?[] Expected;
    }

    class Solution1
    {
        public void Flatten(TreeNode root)
        {
            FlattenHelp(root);

            TreeNode FlattenHelp(TreeNode node) {
                if(node is null) return null;
                if(node.left is null && node.right is null) return node;
                var leftEnd = FlattenHelp(node.left);
                var rightEnd = FlattenHelp(node.right);
                if(leftEnd is not null) {
                    leftEnd.right = node.right;
                    node.right = node.left;
                    node.left = null;
                }

                return rightEnd is null ? leftEnd : rightEnd;
            }
        }
    }
}