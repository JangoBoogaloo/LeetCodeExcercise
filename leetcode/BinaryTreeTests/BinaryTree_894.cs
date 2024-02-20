namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_894
{
    private class Solution {
        public IList<TreeNode> AllPossibleFBT(int n)
        {
            var memo = new Dictionary<int, IList<TreeNode>>();
            return AllPossibleFBTRecursive(n);
        
            IList<TreeNode> AllPossibleFBTRecursive(int n)
            {
                var result = new List<TreeNode>();
                if (n % 2 == 0) // not a valid full binary tree, so it's combination is 0, empty list
                {
                    return result;
                }
                if (n == 1)
                {
                    result.Add(new TreeNode());
                    return result;
                }

                if (memo.TryGetValue(n, out var memoResult))
                {
                    return memoResult;
                }

                for (var i = 1; i < n; i += 2)
                {
                    var leftTrees = AllPossibleFBTRecursive(i);
                    var rightTrees = AllPossibleFBTRecursive(n - i - 1);
                    foreach (var leftTree in leftTrees)
                    {
                        foreach (var rightTree in rightTrees)
                        {
                            var root = new TreeNode(0, leftTree, rightTree);
                            result.Add(root);
                        }
                    }
                }

                memo[n] = result;
                return result;
            }
        }
    }
}