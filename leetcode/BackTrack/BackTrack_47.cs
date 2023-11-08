namespace BackTrack;

[TestFixture]
class BackTrack_47
{
    class Solution {
        public IList<IList<int>> PermuteUnique(int[] nums) {
            Array.Sort(nums);
            var permutations = new List<IList<int>>();
            var aPermutation = new List<int>();
            var used = new bool[nums.Length];
            Backtrack();
            return permutations;

            void Backtrack()
            {
                if(aPermutation.Count == nums.Length) {
                    permutations.Add(new List<int>(aPermutation));
                    return;
                }
                for(var i=0; i<nums.Length; i++) {
                    if(used[i]) continue;

                    if(i>0 && nums[i] == nums[i-1] && !used[i-1]) continue;
                    used[i] = true;
                    aPermutation.Add(nums[i]);
                    Backtrack();
                    used[i] = false;
                    aPermutation.RemoveAt(aPermutation.Count-1);
                }
            }
        }
    }    
}
