namespace Array;

[TestFixture]
class Array_303
{
    class NumArray {
        private int[] sum;

        public NumArray(int[] nums) {
            sum = new int[nums.Length+1];
            for(var i=1; i<sum.Length; i++) {
                sum[i] = sum[i-1] + nums[i-1];
            }
        }
    
        public int SumRange(int left, int right) {
            return sum[right+1] - sum[left];
        }
    }
}

