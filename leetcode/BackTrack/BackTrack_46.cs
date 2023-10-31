namespace BackTrack;

[TestFixture]
class BackTrack_46
{
    class Solution {
        public IList<IList<int>> Permute(int[] nums) {
            var result = new List<IList<int>>();
            var track = new List<int>();
            var used = new bool[nums.Length];
            BackTrack();
            return result;

            void BackTrack() {
                if(track.Count == nums.Length) {
                    result.Add(new List<int>(track));
                    return;
                }

                for(var i=0; i<nums.Length; i++) {
                    if(used[i]) continue;
                    track.Add(nums[i]);
                    used[i] = true;
                    BackTrack();
                    //Back here
                    track.RemoveAt(track.Count -1);
                    used[i] = false;
                }
            }
        }
    }
}
