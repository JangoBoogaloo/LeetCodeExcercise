namespace BackTrack;

[TestFixture]
class BackTrack_77
{
    class Solution {
        public IList<IList<int>> Combine(int n, int k) {
            var result  = new List<IList<int>>();
            var aSet = new List<int>();
            Backtrack(1);
            return result;

            void Backtrack(int start) {
                if(aSet.Count == k) {
                    result.Add(new List<int>(aSet));
                    return;
                }
                for(var i=start; i<=n; i++) {
                    aSet.Add(i);
                    Backtrack(i+1);
                    aSet.RemoveAt(aSet.Count-1);
                }
            }
        }
    }
}