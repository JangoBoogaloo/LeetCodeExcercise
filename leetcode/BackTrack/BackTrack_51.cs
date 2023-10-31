using System.Text;

namespace BackTrack;

[TestFixture]
class BackTrack_51
{
    public class Solution {
        public IList<IList<string>> SolveNQueens(int n)
        {
            var result = new List<IList<string>>();
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
                    result.Add(new List<string>(board));
                    return;
                }

                for (var col = 0; col < board[row].Length; col++)
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
                if (board.Any(rowStr => rowStr[col] == 'Q'))
                {
                    return false;
                }

                for (int r = row - 1, c = col + 1; r >= 0 && c < board.Count; r--, c++)
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