namespace BackTrack;

[TestFixture]
class BackTrack_40
{
    class Solution {
        public IList<IList<int>> CombinationSum2(int[] candidates, int target) {
            Array.Sort(candidates);
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
                    if(i> start && candidates[i-1] == candidates[i]) {
                        continue;
                    }
                    trackSum += candidates[i];
                    aSet.Add(candidates[i]);
                    Backtrack(i+1);
                    trackSum -= candidates[i];
                    aSet.RemoveAt(aSet.Count-1);
                }
            }
        }
    }
}