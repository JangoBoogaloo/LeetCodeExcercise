namespace BackTrack;

[TestFixture]
class BackTrack_78
{
    public class Solution {
        public IList<IList<int>> Subsets(int[] nums) {
            var result = new List<IList<int>>();
            var aSet = new List<int>();
            Backtrack(0);
            return result;

            void Backtrack(int start)
            {
                result.Add(new List<int>(aSet));
                for(int i=start; i<nums.Length; i++) {
                    aSet.Add(nums[i]);
                    Backtrack(i+1);
                    aSet.RemoveAt(aSet.Count-1);
                }
            }
        }
    }
}