using System.Text;

namespace BackTrack;

[TestFixture]
class BackTrack_17
{
    class Solution {
        public IList<string> LetterCombinations(string digits)
        {
            if (string.IsNullOrEmpty(digits))
            {
                return new List<string>();
            }

            var combinations = new List<string>();
            var aSet = new StringBuilder();
            var digitChars = digits.ToCharArray();
            var numberCharsMap = new Dictionary<char, List<char>>
            {
                ['2'] = new (){ 'a', 'b', 'c' },
                ['3'] = new (){ 'd', 'e', 'f' },
                ['4'] = new (){ 'g', 'h', 'i' },
                ['5'] = new (){ 'j', 'k', 'l' },
                ['6'] = new (){ 'm', 'n', 'o' },
                ['7'] = new (){ 'p', 'q', 'r', 's' },
                ['8'] = new (){ 't', 'u', 'v', },
                ['9'] = new (){ 'w', 'x', 'y', 'z' },
            };
            Backtrack(0);
            return combinations;


            void Backtrack(int start)
            {
                if (start == digitChars.Length)
                {
                    combinations.Add(aSet.ToString());
                    return;
                }

                var digitChar = digitChars[start];
                var charSet = numberCharsMap[digitChar];
                for (var i = 0; i < charSet.Count; i++)
                {
                    aSet.Append(charSet[i]);
                    Backtrack(start+1);
                    aSet.Length--;
                }
            }
        }
    }
}