namespace BackTrack;

[TestFixture]
class BackTrack_980
{
    class Solution {
        public int UniquePathsIII(int[][] grid) {
            var rows = grid.Length;
            if(rows ==0) return 0;
            var cols = grid[0].Length;
            int startX = -1; 
            int startY = -1;
            int endX = -1;
            int endY = -1;
            bool startFound = false;
            bool endFound = false;
            var paths = 0;
            var emptyCount = 0;
            for(var r = 0; r<rows; r++) {
                for(var c = 0; c<cols; c++) {
                    if(grid[r][c] == 1) {
                        startX = c;
                        startY = r;
                    }
                    else if(grid[r][c] == 2) {
                        endX = c;
                        endY = r;
                    }
                    else if(grid[r][c] == 0) {
                        emptyCount++;
                    }
                }   
            }
            Backtrack(startX, startY, emptyCount);
            return paths;
    
            void Backtrack(int x, int y, int empty) {
                var distanceX = Math.Abs(endX-x);
                var distanceY = Math.Abs(endY-y);
                var distanceSteps = distanceX + distanceY;
                if(empty ==0 && distanceSteps ==1) {
                    paths++;
                    return;
                }
                if(empty < distanceSteps-1) {
                    return;
                }
                if(x-1>=0 && grid[y][x-1] == 0) {
                    grid[y][x-1] = -1;
                    Backtrack(x-1, y, empty-1);
                    grid[y][x-1] = 0;
                }
                if(x+1<cols && grid[y][x+1] == 0) {
                    grid[y][x+1] = -1;
                    Backtrack(x+1, y, empty-1);
                    grid[y][x+1] = 0;
                }
                if(y-1>=0 && grid[y-1][x] == 0) {
                    grid[y-1][x] = -1;
                    Backtrack(x, y-1, empty-1);
                    grid[y-1][x] = 0;
                }
                if(y+1<rows && grid[y+1][x] == 0) {
                    grid[y+1][x] = -1;
                    Backtrack(x, y+1, empty-1);
                    grid[y+1][x] = 0;
                }
            }
        }
    }
}