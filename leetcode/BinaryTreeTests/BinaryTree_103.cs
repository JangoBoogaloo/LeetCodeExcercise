namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_103
{
    private class Solution {
        public IList<IList<int>> ZigzagLevelOrder(TreeNode root) {
            var result = new List<IList<int>>();
            if(root is null) return result;
            var queue = new Queue<TreeNode>();
            queue.Enqueue(root);
            var fromRight = false;
            while(queue.Any()) {
                var levelList = new List<int>();
                var levelSize = queue.Count;
                for(var i=0; i<levelSize; i++) {
                    var node = queue.Dequeue();
                    levelList.Add(node.val);
                    if(node.left is not null) {
                        queue.Enqueue(node.left);
                    }
                    if(node.right is not null) {
                        queue.Enqueue(node.right);
                    }
                }
                if(fromRight) {
                    levelList.Reverse();
                }
                result.Add(levelList);
                //flip the level traversal order
                fromRight = !fromRight;
            }
            return result;
        }
    }
}

class Solution {
    public IList<IList<int>> ZigzagLevelOrder(TreeNode root) {
        var result = new List<IList<int>>();
        if(root is null) return result;
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        var fromRight = false;
        while(queue.Any()) {
            var levelList = new List<int>();
            var levelSize = queue.Count;
            for(var i=0; i<levelSize; i++) {
                var node = queue.Dequeue();
                levelList.Add(node.val);
                if(node.left is not null) {
                    queue.Enqueue(node.left);
                }
                if(node.right is not null) {
                    queue.Enqueue(node.right);
                }
            }
            if(fromRight) {
                levelList.Reverse();
            }
            result.Add(levelList);
            //flip the level traversal order
            fromRight = !fromRight;
        }
        return result;
    }
}