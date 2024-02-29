namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_919
{
    class CBTInserter {
        private Queue<TreeNode> _levelQueue;
        private TreeNode _root;
        public CBTInserter(TreeNode root) {
            var queue = new Queue<TreeNode>();
            _levelQueue = new Queue<TreeNode>();
            _root = root;
            queue.Enqueue(_root);
            while(queue.Count > 0) {
                var current = queue.Dequeue();
                if(NeedsChild(current)) {
                    _levelQueue.Enqueue(current);
                }
                if(current.left is not null) {
                    queue.Enqueue(current.left);
                }
                if(current.right is not null) {
                    queue.Enqueue(current.right);
                }
            }
        }
    
        public int Insert(int val) {
            var node = _levelQueue.Peek();
            var newNode = new TreeNode(val);
            if(node.left is null) {
                node.left = newNode;
            } else {
                node.right = newNode;
                _levelQueue.Dequeue();
            }
            _levelQueue.Enqueue(newNode);
            return node.val;
        }
    
        public TreeNode Get_root() {
            return _root;
        }

        private bool NeedsChild(TreeNode node) {
            return (node.left is null || node.right is null);
        }
    }
}