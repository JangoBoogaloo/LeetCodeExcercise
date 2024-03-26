namespace StringTests;

[TestFixture]
class String_3
{
    class Solution {
        public int LengthOfLongestSubstring(string s) {
            var result = 0;
            var charFrequency = new Dictionary<char, int>();
            var left = 0;
            var right = 0;
            while(right < s.Length) {
                var rightChar = s[right];
                right++;
                charFrequency[rightChar] = charFrequency.GetValueOrDefault(rightChar, 0) +1;
                while(charFrequency[rightChar] > 1) {
                    var leftChar = s[left];
                    left++;
                    charFrequency[leftChar] = charFrequency[leftChar] -1;
                }
                result = Math.Max(result, right-left);
            }

            return result;
        }
    }
}