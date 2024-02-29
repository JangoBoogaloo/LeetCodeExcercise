namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_1530
{
    class Solution {
        private int _result;
    
        public int CountPairs(TreeNode? root, int distance) {
            _result = 0;
            PostOrder(root, distance);
            return _result;
        }

        private int[] PostOrder(TreeNode? node, int distance) {
            var distanceCache = new int[distance+1];
            if(node is null) return distanceCache;
            // node is leaf node, no child, just return
            if (node.left == null && node.right == null) {
                distanceCache[1] = 1; //parent node to this node have distance 1
                return distanceCache;
            }
            var leftDistanceCache = PostOrder(node.left, distance);
            var rightDistanceCache = PostOrder(node.right, distance);

            for(var l = 1; l<distance; l++) {
                for(var r=1; r<distance; r++) {
                    var goodDist = l+r;
                    if (goodDist <= distance) {
                        var goodDistCombination = leftDistanceCache[l] * rightDistanceCache[r];
                        _result += goodDistCombination;
                    }
                }
            }

            for(var i = distance; i > 0; i--) 
            {
                var leafCountDistToChild = leftDistanceCache[i-1] + rightDistanceCache[i-1];
                //Since this result return to parent, so the count become leaf count dist to parent
                distanceCache[i] = leafCountDistToChild;
            }
            return distanceCache;
        }
    }
}