namespace GraphTests;

[TestFixture]
class Graph_277
{
    class Relation
    {
        private bool[,] _knowRelation;
        public Relation(bool[,] knowRelation)
        {
            _knowRelation = knowRelation;
        }

        protected bool Knows(int a, int b)
        {
            return _knowRelation[a, b];
        }
    }

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

        public Solution(bool[,] knowRelation) : base(knowRelation)
        {
        }
    }
}
