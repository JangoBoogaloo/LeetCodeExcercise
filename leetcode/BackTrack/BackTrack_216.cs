namespace BackTrack;

[TestFixture]
class BackTrack_216
{
    class Solution {
        public IList<IList<int>> CombinationSum3(int k, int n) {
            var combinations = new List<IList<int>>();
            var trackSum = 0;
            var aSet = new List<int>();
            Backtrack(1);
            return combinations;

            void Backtrack(int start) {
                if(trackSum == n && aSet.Count == k) {
                    combinations.Add(new List<int>(aSet));
                    return;
                }

                if(trackSum > n) return;

                for(var i=start; i<=9; i++) {
                    trackSum += i;
                    aSet.Add(i);
                    Backtrack(i+1);
                    trackSum -= i;
                    aSet.RemoveAt(aSet.Count-1);
                }
            }
        }
    }
}