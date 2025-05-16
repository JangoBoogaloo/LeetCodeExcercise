namespace Array;

[TestFixture]
class Array_5
{
    class Solution {
        public string LongestPalindrome(string s) {
            var begin=0;
            var maxLength = -1;
            for(var i=0; i< s.Length; i++) {
                Palindrome(s, i, i);
                Palindrome(s, i, i+1);
            }

            return s.Substring(begin, maxLength);

            void Palindrome(string s, int left, int right) {
                while(left >= 0 && right < s.Length && s[left] == s[right]) {
                    left--;
                    right++;
                }
                var startIndex = left + 1;
                var length = right - startIndex;
                if(maxLength < length) {
                    begin = startIndex;
                    maxLength = length;
                }
            }
        }
    }
}