namespace Array;

[TestFixture]
class Array_1658
{
    class Solution {
        public int MinOperations(int[] nums, int x) {
            var total = 0;
            var maxLength = -1;
            foreach(var num in nums){
                total += num;
            }
            var remainSum = total - x;
            var left = 0;
            var right = 0;
            var currentSum = 0;
            while(right < nums.Length) {
                currentSum += nums[right];
                while(currentSum > remainSum && left <=right) {
                    currentSum -= nums[left];
                    left++;
                }
                if(currentSum == remainSum) {
                    maxLength = Math.Max(maxLength, right-left+1);
                }
                right++;
            }
            if(maxLength == -1) return -1;
            return nums.Length-maxLength;
        }
    }
}