namespace StringTests;

[TestFixture]
class String_76
{
    class Solution {
        public string MinWindow(string s, string t)
        {
            var need = new Dictionary<char, int>();
            var window = new Dictionary<char, int>();
    
            foreach (var c in t)
            {
                need[c] = need.GetValueOrDefault(c, 0) + 1;
            }
    
            var left = 0;
            var right = 0;
            var valid = 0;
            var start = 0;
            var len = int.MaxValue;
            while (right < s.Length)
            {
                var newChar = s[right];
                right++;
                if (need.TryGetValue(newChar, out var value))
                {
                    window[newChar] = window.GetValueOrDefault(newChar, 0) + 1;
                    if (window[newChar] == value) valid++;
                }
    
                while (valid == need.Count)
                {
                    if (right - left < len)
                    {
                        start = left;
                        len = right - left;
                    }
    
                    var d = s[left];
                    left++;
                    if (need.TryGetValue(d, out var value1))
                    {
                        if (window[d] == value1) valid--;
                        window[d] -= 1;
                    }
                }
            }
    
            return len == int.MaxValue ? "" : s.Substring(start, len);
        }
    }

    [TestCase("ADOBECODEBANC", "ABC", "BANC")]
    [TestCase("a", "a", "a")]
    [TestCase("a", "aa", "")]

    public void TestMinWindow(string s, string t, string expected)
    {
        var solution = new Solution();
        var actual = solution.MinWindow(s, t);
        Assert.That(string.Equals(expected, actual), Is.True);
    }
}

