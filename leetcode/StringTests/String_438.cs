namespace StringTests;

[TestFixture]
class String_438
{
    class Solution {
        public IList<int> FindAnagrams(string s, string p) {
            var pCharFrequency = new Dictionary<char, int>();
            var sWindow = new Dictionary<char, int>();
            var result = new List<int>();
            foreach(var c in p) {
                pCharFrequency[c] = pCharFrequency.GetValueOrDefault(c, 0)+1;
            }
            var left = 0;
            var right = 0;
            var valid = 0;
            while(right <s.Length) {
                var rightChar = s[right];
                right++;

                if(pCharFrequency.TryGetValue(rightChar, out var value)) {
                    sWindow[rightChar] = sWindow.GetValueOrDefault(rightChar, 0)+1;
                    if(sWindow[rightChar] == value) valid++;
                }
                while(right-left >= p.Length) {
                    if(valid == pCharFrequency.Count) {
                        result.Add(left);
                    }
                    var leftChar = s[left];
                    left++;
                    if(pCharFrequency.TryGetValue(leftChar, out var value1)) {
                        if(sWindow[leftChar] == value1) valid--;
                        sWindow[leftChar] = sWindow.GetValueOrDefault(leftChar, 0) -1;
                    }
                }
            }

            return result;
        }
    }
}