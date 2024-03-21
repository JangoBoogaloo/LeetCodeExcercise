namespace TwoPointersTests;

[TestFixture]
internal class TwoPointers_18
{
    [Test]
    public void TestSolution()
    {
        var solution = new Solution();
        var result = solution.FourSum(new[] { -2, -1, -1, 1, 1, 2, 2 }, 0);
        Assert.IsNotEmpty(result);
    }

    class Solution {
        public IList<IList<int>> FourSum(int[] nums, int target)
        {
            Array.Sort(nums);
            return KSum(nums, target, 0, 4);
        }

        private List<IList<int>> KSum(int[] sortedNums, long target, int start, int k)
        {
            var result = new List<IList<int>>();
            if (start == sortedNums.Length) { return result; }

            var average = target / k;
            //smallest already bigger than average, or biggest smaller than average
            if (sortedNums[start] > average || average > sortedNums[^1])
            {
                return result;
            }

            if (k == 2)
            {
                return TwoSum(sortedNums, target, start);
            }

            for (var i = start; i < sortedNums.Length; i++)
            {
                //If this iteration have same value, we ignore, avoid duplicate answer
                if (i > start && sortedNums[i - 1] == sortedNums[i])
                {
                    continue;
                }

                var kSumSet = KSum(sortedNums, target - sortedNums[i], i + 1, k - 1);
                foreach (var set in kSumSet)
                {

                    var newList = new List<int>();
                    newList.Add(sortedNums[i]);
                    newList.AddRange(set);
                    result.Add(newList);
                }
            }

            return result;
        }

        private List<IList<int>> TwoSum(int[] sortedNums, long target, int start)
        {
            var result = new List<IList<int>>();
            var left = start;
            var right = sortedNums.Length - 1;

            while (left < right)
            {
                var sum = sortedNums[left] + sortedNums[right];
                if (sum > target || (right < sortedNums.Length - 1 && sortedNums[right] == sortedNums[right+1]))
                {
                    right--;
                }
                else if (sum < target || (left > start && sortedNums[left-1] == sortedNums[left]))
                {
                    left++;
                }
                else
                {
                    result.Add(new[] {sortedNums[left], sortedNums[right]} );
                    left++;
                    right--;
                }
            }
            return result;
        }
    }
}
