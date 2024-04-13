using BinaryTree;

namespace BinaryTreeTests;

[TestFixture]
class ConstructBinaryTree_106
{
    private static IReadOnlyList<ConstructBinaryTreeTestCase> _constructBinaryTree106TestCase = new[]
    {
        new ConstructBinaryTreeTestCase()
        {
            InOrder = new[] { 9, 3, 15, 20, 7 },
            PostOrder = new []{9,15,7,20,3},
            Expected = new int?[] { 3, 9, 20, null, null, 15, 7 },
        }
    };
    
    [TestCaseSource(nameof(_constructBinaryTree106TestCase))]
    public void TestConstructBinaryTree_106(ConstructBinaryTreeTestCase testcase)
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
            var inorderIndexMap = new Dictionary<int,int>();
            for(int i=0; i<inorder.Length; i++) {
                inorderIndexMap[inorder[i]] = i;
            }
            return BuildTreeHelper(postorder.Length-1, 0, inorder.Length-1);

            TreeNode BuildTreeHelper(int postEnd, int inStart, int inEnd)
            {
                if(postEnd <0 || inStart > inEnd) return null;
                var rootVal = postorder[postEnd];
                var rootIndex = inorderIndexMap[rootVal];
                var rightTreeLength = inEnd-rootIndex;
                var root = new TreeNode(rootVal);
                root.left = BuildTreeHelper(postEnd-1-rightTreeLength, inStart, rootIndex-1);
                root.right = BuildTreeHelper(postEnd-1, rootIndex+1, inEnd);
                return root;
            }
        }
    }
}