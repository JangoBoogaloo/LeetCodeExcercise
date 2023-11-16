namespace BackTrack;

[TestFixture]
class BackTrack_1601
{
    class Solution {
        public int MaximumRequests(int n, int[][] requests) {
            var buildings = new int[n];
            var answer = 0;
            Backtrack(0, 0);
            return answer;

            void Backtrack(int index, int requestCounts) {
                
                if(index == requests.Length) {
                    for(var i=0; i<n; i++) 
                    {
                        if(buildings[i] != 0) return;
                    }

                    answer = Math.Max(answer, requestCounts);
                    return;
                }

                buildings[requests[index][0]]--;
                buildings[requests[index][1]]++;
            
                //Accept request
                Backtrack(index+1, requestCounts+1);

                buildings[requests[index][0]]++;
                buildings[requests[index][1]]--;

                //Reject request
                Backtrack(index+1, requestCounts);
            }

        }
    }

    [Test]
    public void TestMaximumRequests()
    {
        var solution = new Solution();
        solution.MaximumRequests(5, new int[][]
        {
            new int[] { 0, 1 }, 
            new int[] { 1, 0 },
            new int[] {0,1},
            new int[] {1,2},
            new int[] {2,0},
            new int[] {3,4}
        });
    }
}

