using BinaryTree;

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
            var inorderIndexMap = new Dictionary<int, int>();
            for(var i=0; i<inorder.Length; i++) {
                inorderIndexMap[inorder[i]] = i;
            }
            return BuildTree(0, 0, inorder.Length-1);

            TreeNode BuildTree(int preStart, int inStart, int inEnd)
            {
                if(preStart > preorder.Length-1 || inStart > inEnd) return null;
                var rootValue = preorder[preStart];
                var root = new TreeNode(rootValue);
                var rootIndex = inorderIndexMap[rootValue];
                root.left = BuildTree(preStart+1, inStart, rootIndex-1);
                var leftTreeLength = rootIndex-inStart;
                root.right = BuildTree(preStart+1+leftTreeLength, rootIndex+1, inEnd);
                return root;
            }
        }
    }
}