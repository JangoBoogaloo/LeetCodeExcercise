namespace Array;

[TestFixture]
class Array_209
{
    class Solution {
        public int MinSubArrayLen(int target, int[] nums) {
            var currentSum = 0;
            var minLength = int.MaxValue;
            var left = 0;
            var right = 0;
            while(right <nums.Length) {
                currentSum += nums[right];
                right++;
                while(currentSum >= target) {
                    minLength = Math.Min(minLength, right-left);
                    currentSum -= nums[left];
                    left++;
                }

            }
            if(minLength == int.MaxValue) return 0;
            return minLength;
        }
    }   
}