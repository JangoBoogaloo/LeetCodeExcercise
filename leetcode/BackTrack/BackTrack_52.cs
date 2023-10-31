using System.Text;

namespace BackTrack;

[TestFixture]
class BackTrack_52
{
    class Solution {
        public int TotalNQueens(int n) 
        {
            var result = 0;
            var board = new List<string>();
            for(var r=0; r<n; r++)
            {
                var row = new string('.', n);
                board.Add(row);
            }
    
            BackTrack(0);
            return result;
    
            void BackTrack(int row)
            {
                if (row == board.Count)
                {
                    result++;
                    return;
                }
    
                var n = board[row].Length;
                for (int col = 0; col < n; col++)
                {
                    if(!IsValid(row, col)) continue;
                    var sb = new StringBuilder(board[row]);
                    sb[col] = 'Q';
                    board[row] = sb.ToString();
                    BackTrack(row+1);
                    sb[col] = '.';
                    board[row] = sb.ToString();
                }
            }
    
            bool IsValid(int row, int col)
            {
                var n = board.Count;
                for (var r = 0; r < board.Count; r++)
                {
                    if (board[r][col] == 'Q')
                    {
                        return false;
                    }
                }
    
                for (int r = row - 1, c = col + 1; r >= 0 && c < n; r--, c++)
                {
                    if (board[r][c] == 'Q') return false;
                }
    
                for (int r = row - 1, c = col - 1;
                     r >= 0 && c >= 0; r--, c--)
                {
                    if (board[r][c] == 'Q') return false;
                }
                return true;
            }
        }
    }
}