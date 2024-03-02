namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_1161
{
    class Solution {
        private int maxLevelSum;
        private int resultLevel;

        public int MaxLevelSum(TreeNode root) {
            maxLevelSum = int.MinValue;
            resultLevel = 0;
            var currentLevel = 0;
            var queue = new Queue<TreeNode>();
            queue.Enqueue(root);
            while(queue.Any()) {
                var levelSize = queue.Count;
                var levelSum = 0;
                currentLevel++;
                for(var i=0; i<levelSize; i++) {
                    var curr = queue.Dequeue();
                    levelSum += curr.val;
                    if(curr.left is not null) {
                        queue.Enqueue(curr.left);
                    }
                    if(curr.right is not null) {
                        queue.Enqueue(curr.right);
                    }
                }
                if(levelSum > maxLevelSum) {
                    maxLevelSum = levelSum;
                    resultLevel = currentLevel;
                }
            }
            return resultLevel;
        }
    }
}