namespace BackTrack;

[TestFixture]
class BackTrack_2305
{
    class Solution {
        public int DistributeCookies(int[] cookies, int k) {
            var children = new int[k];
            var answer = int.MaxValue;
            Backtrack(0, k);
            return answer;

            int Backtrack(int bucketIndex, int zeroCount) {
                //If more children have 0 than remaining buckets
                if(cookies.Length - bucketIndex <zeroCount) {
                    return int.MaxValue;
                }

                //After we distributed every children
                if(bucketIndex==cookies.Length) {
                    var unfairness = int.MinValue;
                    foreach(var value in children) {
                        unfairness = Math.Max(unfairness, value);
                    }
                    return unfairness;
                }
                for(var i=0; i<k; i++) {
                    if (children[i] == 0) {
                        zeroCount--;
                    }
                    children[i] += cookies[bucketIndex];
                    var newAnswer = Backtrack(bucketIndex+1, zeroCount);
                    answer = Math.Min(answer, newAnswer);
                    children[i] -= cookies[bucketIndex];
                    if (children[i] == 0) {
                        zeroCount++;
                    }
                }
                return answer;
            }
        }
    }
}