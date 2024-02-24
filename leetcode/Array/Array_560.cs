namespace Array;

[TestFixture]
internal class Array_560
{
    private class Solution {
        public int SubarraySum(int[] nums, int target) {
            var count = 0;
            var currSum = 0;
            var sumOccurance = new Dictionary<int, int>();
            foreach(var num in nums)
            {
                currSum += num;
                if(currSum == target) {
                    count++;
                }
                var targetDiff = currSum - target;
                count += sumOccurance.GetValueOrDefault(targetDiff, 0);
                sumOccurance[currSum] = sumOccurance.GetValueOrDefault(currSum, 0) + 1;
            }

            return count;
        }
    }
}