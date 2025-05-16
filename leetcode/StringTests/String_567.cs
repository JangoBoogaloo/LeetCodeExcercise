namespace StringTests;

[TestFixture]
class String_567
{
    class Solution {
        public bool CheckInclusion(string s1, string s2)
        {
            var need = new Dictionary<char, int>();
            var window = new Dictionary<char, int>();
            foreach (var c in s1)
            {
                need[c] = need.GetValueOrDefault(c, 0) + 1;
            }

            var left = 0;
            var right = 0;
            var valid = 0;
            while (right < s2.Length)
            {
                var c = s2[right];
                right++;
                if (need.TryGetValue(c, out var cVal))
                {
                    window[c] = window.GetValueOrDefault(c, 0) + 1;
                    if (window[c] == cVal) valid++;
                }

                while (right - left >= s1.Length)
                {
                    if (valid == need.Count) return true;
                    var d = s2[left];
                    left++;
                    if (need.TryGetValue(d, out var dVal))
                    {
                        if (window[d] == dVal) valid--;
                        window[d] = window.GetValueOrDefault(d, 0) - 1;
                    }
                }
            }

            return false;
        }
    }

    [TestCase("ab", "eidbaooo", true)]
    [TestCase("ab", "eidboaoo", false)]
    public void TestCheckInclusion(string s1, string s2, bool expectedIsInclude)
    {
        var solution = new Solution();
        var actualIsInclude = solution.CheckInclusion(s1, s2);
        Assert.That(actualIsInclude, Is.EqualTo(expectedIsInclude));
    }
}