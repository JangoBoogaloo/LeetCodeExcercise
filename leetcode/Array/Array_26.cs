namespace Array;

[TestFixture]
class Array_26
{
    class Solution {
        public int RemoveDuplicates(int[] nums) {
            if(nums.Length ==0) return 0;
            var slowIndex = 0;
            for(var fastIndex=1; fastIndex<nums.Length; fastIndex++)
            {
                if(nums[fastIndex] != nums[fastIndex-1]) {
                    slowIndex++;
                    nums[slowIndex] = nums[fastIndex];
                }
            }
            return slowIndex+1;
        }
    }
}