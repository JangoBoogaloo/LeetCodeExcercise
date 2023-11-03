namespace BackTrack;

[TestFixture]
class BackTrack_90
{
    class Solution {
        public IList<IList<int>> SubsetsWithDup(int[] nums) {
            var result = new List<IList<int>>();
            var set = new List<int>();
            Array.Sort(nums);
            Backtrack(0);
            return result;

            void Backtrack(int start)
            {
                result.Add(new List<int>(set));
                for(int i=start; i<nums.Length; i++) {
                    //pruning the duplicate number tracking, pattern is already set
                    if(i>start && nums[i] ==nums[i-1]) {
                        continue;
                    }
                    set.Add(nums[i]);
                    Backtrack(i+1);
                    set.RemoveAt(set.Count-1);
                }
            }
        }
    }
}