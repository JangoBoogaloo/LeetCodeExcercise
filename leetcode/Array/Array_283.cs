namespace Array;

[TestFixture]
class Array_283
{
    class Solution {
        public void MoveZeroes(int[] nums) {
            var zeroStart = RemoveElement(nums, 0);
            for(var i = zeroStart; i<nums.Length; i++) {
                nums[i] = 0;
            }
        }

        private int RemoveElement(int[] nums, int val) {
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