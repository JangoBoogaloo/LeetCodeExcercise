namespace GraphTests;

[TestFixture]
class Graph_997
{
    class Solution {
        public int FindJudge(int n, int[][] trust) {
            var trustRelation = new bool[n,n];
            foreach(var relation in trust) {
                trustRelation[relation[0]-1,relation[1]-1] = true;
            }
            var judge = 0;
            for(var other = 1; other < n; other++) {
                if(trustRelation[judge, other] || !trustRelation[other, judge]) {
                    judge = other;
                }
            }

            for(var other = 0; other < n; other++) {
                if(other == judge) continue;
                if(trustRelation[judge, other] || !trustRelation[other, judge]) {
                    return -1;
                }
            }
            return judge+1;
        }
    }
}
