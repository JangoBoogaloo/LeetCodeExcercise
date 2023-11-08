namespace BackTrack;

[TestFixture]
class BackTrack_39
{
    class Solution {
        public IList<IList<int>> CombinationSum(int[] candidates, int target)
        {
            var combinations = new List<IList<int>>();
            var aSet = new List<int>();
            var trackSum = 0;
            Backtrack(0);
            return combinations;

            void Backtrack(int start)
            {
                if (trackSum == target)
                {
                    combinations.Add(new List<int>(aSet));
                    return;
                }

                if (trackSum > target) return;

                for (var i = start; i < candidates.Length; i++)
                {
                    trackSum += candidates[i];
                    aSet.Add(candidates[i]);
                    Backtrack(i);
                    trackSum -= candidates[i];
                    aSet.RemoveAt(aSet.Count-1);
                }
            }
        }
    }    
}