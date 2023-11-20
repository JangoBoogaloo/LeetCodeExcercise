namespace Array;

[TestFixture]
class Array_27
{
    class Solution {
        public int RemoveElement(int[] nums, int val) {
            var slowIndex = 0;
            for(var fastIndex=0; fastIndex<nums.Length; fastIndex++)
            {
                if(nums[fastIndex] != val) {
                    nums[slowIndex] = nums[fastIndex];
                    slowIndex++;
                }
            }
            return slowIndex;
        }
    }
}