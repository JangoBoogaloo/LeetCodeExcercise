namespace BinaryTreeTests;

[TestFixture]
class BinarySearchTree_1038
{
    private class Solution
    {
        public TreeNode BstToGst(TreeNode root)
        {
            var sum = 0;
            return InorderRight(root);

            TreeNode InorderRight(TreeNode node)
            {
                if (node is null) return null;
                var right = InorderRight(node.right);
                sum += node.val;
                var sumNode = new TreeNode(sum);
                var left = InorderRight(node.left);
                sumNode.right = right;
                sumNode.left = left;
                return sumNode;
            }
        }
    }

    private static IReadOnlyList<TestCase_1038> _testCases = new[]
    {
        new TestCase_1038()
        {
            Input = new int?[]{4,1,6,0,2,5,7,null,null,null,3,null,null,null,8},
            Expected = new int?[] {30,36,21,36,35,26,15,null,null,null,33,null,null,null,8}
        },
    };

    [TestCaseSource(nameof(_testCases))]
    public void TestBST_1038(TestCase_1038 testcase)
    {
        var solution = new Solution();
        var tree = TreeNode.BuildTree(testcase.Input);
        var greaterSumTree = solution.BstToGst(tree);
        var actual = TreeNode.ToList(greaterSumTree).ToArray();
        CollectionAssert.AreEqual(testcase.Expected, actual);
    }

    public class TestCase_1038
    {
        public int?[] Input;

        public int?[] Expected;
    }
}