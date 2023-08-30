namespace BinaryTreeTests;

[TestFixture]
class MaximumPathSum_124
{
    class Solution
    {
        public int MaxPathSum(TreeNode root)
        {
            var maxSum = int.MinValue;
            MaxPathSumHelp(root);
            return maxSum;

            int MaxPathSumHelp(TreeNode? node)
            {
                if (node is null)
                {
                    return 0;
                }

                var leftDepthSum = MaxPathSumHelp(node.left);
                var rightDepthSum = MaxPathSumHelp(node.right);
                var maxDepthSum = Math.Max(0, Math.Max(leftDepthSum, rightDepthSum)) + node.val;
                var treePathSum = leftDepthSum + node.val + rightDepthSum;
                maxSum = Math.Max(treePathSum, maxSum);
                maxSum = Math.Max(node.val, maxSum);
                maxSum = Math.Max(maxDepthSum, maxSum);
                return maxDepthSum;
            }
        }
    }

    private static IReadOnlyList<MaximumPathSum_124TestCase> _maximumPathSum124TestCases = new[]
    {
        new MaximumPathSum_124TestCase()
        {
            Input = new int?[] { -10, 9, 20, null, null, 15, 7 },
            Expected = 42
        },
        new MaximumPathSum_124TestCase()
        {
            Input = new int?[] { 1,-2,-3,1,3,-2,null,-1 },
            Expected = 3
        },
        
        new MaximumPathSum_124TestCase()
        {
            Input = new int?[] {
                     9,
                    6,-3,
                null, null,-6,2, 
            null, null, null, null, null, null, 2, null, 
            null, null, null, null,null, null, null, null,null, null,null, null, -6,-6,-6},
            Expected = 16
        }
    };
    
    [TestCaseSource(nameof(_maximumPathSum124TestCases))]
    public void TestMaximumPathSum_124(MaximumPathSum_124TestCase testCase)
    {
        var solution = new Solution();
        var tree = TreeNode.BuildTree(testCase.Input);
        var actual = solution.MaxPathSum(tree);
        Assert.That(actual, Is.EqualTo(testCase.Expected));
    }

    public class MaximumPathSum_124TestCase
    {
        public int?[] Input;
        public int Expected;
    }
}

