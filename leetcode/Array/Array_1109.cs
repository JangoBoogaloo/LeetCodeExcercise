namespace Array;

[TestFixture]
class Array_1109
{
    class Solution {
        public int[] CorpFlightBookings(int[][] bookings, int n) {
            var result = new int[n];
            var diff = new int[n+1];
            foreach(var booking in bookings) {
                diff[booking[0]-1] +=booking[2];
                var next = booking[1];
                if(next < n) {
                    diff[next] -= booking[2];
                }
            }
            result[0] = diff[0];
            for(var i=1; i<result.Length; i++) {
                result[i] = result[i-1] + diff[i];
            }
            return result;
        }
    }
}