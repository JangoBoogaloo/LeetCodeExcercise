namespace Array;

public class Array_344
{
    class Solution {
        public void ReverseString(char[] s) {
            var left = 0;
            var right = s.Length-1;
            while(left<right) {
                (s[left], s[right]) = (s[right], s[left]);
                left++;
                right--;
            }
        }
    }
}