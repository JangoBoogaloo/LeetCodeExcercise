namespace Array;

class Array_304
{
    class NumMatrix {
        private int[,] matrixSum;

        public NumMatrix(int[][] matrix) {
            matrixSum = new int[matrix.Length+1,matrix[0].Length+1];
            for(var r=1; r<matrixSum.GetLength(0); r++) {
                for(var c=1; c<matrixSum.GetLength(1); c++)
                {
                    matrixSum[r, c] = matrix[r - 1][c - 1] 
                                      + matrixSum[r - 1, c] 
                                      + matrixSum[r, c - 1] 
                                      - matrixSum[r - 1, c - 1];
                }
            }
        }
    
        public int SumRegion(int row1, int col1, int row2, int col2) {
            return matrixSum[row2+1,col2+1] 
                   - matrixSum[row1,col2+1] 
                   - matrixSum[row2+1,col1] 
                   +matrixSum[row1,col1];
        }
    }

    [TestCase(2,1,4,3,8)]
    [TestCase(1,1,2,2,11)]
    [TestCase(1,2,2,4,12)]
    public void TestNumMatrixAndSumRegion(int row1, int col1, int row2, int col2, int expected)
    {
        var data = new int[][]
        {
            new[] { 3, 0, 1, 4, 2 },
            new[] { 5, 6, 3, 2, 1 },
            new[] { 1, 2, 0, 1, 5 },
            new[] { 4, 1, 0, 1, 7 },
            new[] { 1, 0, 3, 0, 5 }
        };
        var numMatrix = new NumMatrix(data);
        Assert.That(numMatrix.SumRegion(row1, col1, row2, col2), Is.EqualTo(expected));
    }
}
