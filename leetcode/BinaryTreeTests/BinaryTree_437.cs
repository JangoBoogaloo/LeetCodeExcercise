namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_437
{
    private class Solution {
        private int target;
        private int count = 0;
        private Dictionary<long, int> sumOccurances = new Dictionary<long, int>();

        public int PathSum(TreeNode root, int targetSum) {
            target = targetSum;
            Preorder(root, 0);
            return count;
        }

        private void Preorder(TreeNode node, long currSum) {
            if(node is null) return;
            currSum += node.val;

            if(currSum == target) count++;

            var sumDiff = currSum - target;
            var sumDiffOccurence = sumOccurances.GetValueOrDefault(sumDiff, 0);
            count += sumDiffOccurence;
            var currSumOccurence = sumOccurances.GetValueOrDefault(currSum, 0) + 1;
            sumOccurances[currSum] = currSumOccurence;
            Preorder(node.left, currSum);
            Preorder(node.right, currSum);
            sumOccurances[currSum]--;
        }
    }
}