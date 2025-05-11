namespace Array;

[TestFixture]
class Array_370
{
    class Solution {
        public int[] GetModifiedArray(int length, int[][] updates) {
            var diff = new int[length];
            for(var i=0; i<updates.Length; i++) {
                var startIndex = updates[i][0];
                var endIndex = updates[i][1];
                var increaseRange = updates[i][2];
                diff[startIndex] += increaseRange;
                if(endIndex+1 < length) {
                    diff[endIndex+1] -= increaseRange;
                }
            }
            for(var i=1; i<diff.Length; i++) {
                diff[i] += diff[i-1];
            }
            return diff;
        }
    }
}