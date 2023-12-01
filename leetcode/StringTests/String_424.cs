namespace StringTests;

[TestFixture]
class String_424
{
    class Solution {
        public int CharacterReplacement(string s, int k)
        {
            var charFrequency = new int[26];
            var start = 0;
            var maxFrequency = 0;
            var maxLength = 0;
            for (var end = 0; end < s.Length; end++)
            {
                var currentChar = s[end] - 'A';
                charFrequency[currentChar]++;
                maxFrequency = Math.Max(maxFrequency, charFrequency[currentChar]);

                var subStringLength = end + 1 - start;
                var operationCount = subStringLength - maxFrequency;
                if (operationCount > k)
                {
                    var outGoingChar = s[start] - 'A';
                    charFrequency[outGoingChar]--;
                    start++;
                }
                maxLength = subStringLength;
            }

            return maxLength;
        }
    }
}