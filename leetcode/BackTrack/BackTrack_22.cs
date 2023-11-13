using System.Text;

namespace BackTrack;

[TestFixture]
class BackTrack_22
{
    class Solution {
        public IList<string> GenerateParenthesis(int n) {
            var combinations = new List<string>();
            var leftCount = 0;
            var rightCount = 0;
            var setLenght = n*2;
            var aSet = new StringBuilder();
            Backtrack();
            return combinations;

            void Backtrack() {
                if(aSet.Length == setLenght) {
                    combinations.Add(aSet.ToString());
                    return;
                }
                if(leftCount < n) {
                    aSet.Append('(');
                    leftCount++;
                    Backtrack();
                    aSet.Length--;
                    leftCount--;
                }
                if(leftCount > rightCount) {
                    aSet.Append(')');
                    rightCount++;
                    Backtrack();
                    aSet.Length--;
                    rightCount--;
                }
            }
        }
    }
}