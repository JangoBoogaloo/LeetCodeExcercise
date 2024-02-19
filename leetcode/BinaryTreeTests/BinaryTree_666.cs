namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_666
{
    class Solution
    {
        public int PathSum(int[] nums)
        {
            var result = 0;
            if (nums.Length == 0) return 0;
            var posValueMap = nums.ToDictionary(num => num / 10, num => num % 10);
            Dfs(1, 1, 0);
            return result;


            bool Dfs(int depth, int pos, int ancestorSum)
            {
                var key = depth * 10 + pos;
                if (!posValueMap.TryGetValue(key, out var nodeValue))
                {
                    return false;
                }
                ancestorSum += nodeValue;
                var hasLeft = Dfs(depth + 1, pos * 2 - 1, ancestorSum);
                var hasRight = Dfs(depth + 1, pos * 2, ancestorSum);
                if (!hasLeft && !hasRight)
                {
                    result += ancestorSum;
                }
                return true;
            }
        }
    }
}