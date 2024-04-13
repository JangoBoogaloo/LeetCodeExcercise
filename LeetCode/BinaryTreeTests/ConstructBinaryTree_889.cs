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

    [TestCaseSource(nameof(_constructBinaryTree889TestCase))]
    public void TestConstructBinaryTreeIterative_889(ConstructBinaryTreeTestCase testCase)
    {
        var solution = new SolutionIterative();
        var tree = solution.ConstructFromPrePost(testCase.Preorder!, testCase.PostOrder!);
        var actual = TreeNode.ToList(tree).ToArray();
        CollectionAssert.AreEqual(actual, testCase.Expected);
    }
    
    class Solution
    {
        public TreeNode ConstructFromPrePost(int[] preorder, int[] postorder)
        {
            var postorderIndexMap = new Dictionary<int, int>();
            for (var i = 0; i < postorder.Length; i++)
            {
                postorderIndexMap[postorder[i]] = i;
            }

            return Build(0, preorder.Length - 1, 0, postorder.Length - 1);

            TreeNode Build(int preStart, int preEnd, int postStart, int postEnd)
            {
                if (preStart > preEnd || postStart > postEnd) return null;
                var root = new TreeNode(preorder[preStart]);
                if (preStart == preEnd) return root;
                var leftRootVal = preorder[preStart + 1];
                var postLeftRootIndex = postorderIndexMap[leftRootVal];
                var leftTreeSize = postLeftRootIndex - postStart + 1;
                root.left = Build(preStart + 1, preStart + leftTreeSize, postStart, postLeftRootIndex);
                root.right = Build(preStart + leftTreeSize + 1, preEnd, postLeftRootIndex + 1, postEnd - 1);
                return root;
            }
        }
    }

    class SolutionIterative
    {
        public TreeNode ConstructFromPrePost(int[] preorder, int[] postorder)
        {
            var nodeStack = new Stack<TreeNode>();
            nodeStack.Push(new TreeNode(preorder[0]));
            for (int i = 1, j = 0; i < preorder.Length; ++i)
            {
                var node = new TreeNode(preorder[i]);
                while (nodeStack.Peek().val == postorder[j])
                {
                    nodeStack.Pop();
                    j++;
                }

                if (nodeStack.Peek().left is null)
                {
                    nodeStack.Peek().left = node;
                }
                else
                {
                    nodeStack.Peek().right = node;
                }
                nodeStack.Push(node);
            }

            return nodeStack.Last();
        }
    }
}