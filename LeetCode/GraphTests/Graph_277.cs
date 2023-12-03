namespace GraphTests;

[TestFixture]
class Graph_277
{
    class Solution : Relation {
        public int FindCelebrity(int n) {
            var cand = 0;
            for(var other = 1; other<n; other++) {
                if(Knows(cand, other) || !Knows(other, cand)) {
                    cand = other;
                }
            }
            for(var other = 0; other<n; other++) {
                if(cand == other) continue;
                if(Knows(cand, other) || !Knows(other, cand)) {
                    return -1;
                }
            }

            return cand;
        }
    }
}
