namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_993
{
    class Solution {
        public bool IsCousins(TreeNode root, int x, int y) {
            if(root is null) return false;
            var queue = new Queue<TreeNode>();
            queue.Enqueue(root);
            while(queue.Any()) {
                var levelNodes = queue.Count;
                var couldBeSibling = false;
                var couldbeCousins = false;

                for(var i=0; i<levelNodes; i++) {
                    var node = queue.Dequeue();

                    if(node is null) {
                        couldBeSibling = false;
                        continue;
                    }

                    if(node.val == x || node.val == y) {
                        if(!couldbeCousins) {
                            couldBeSibling = true;
                            couldbeCousins = true;
                        } 
                        else if(couldBeSibling) {
                            //They are siblings, not cousins
                            return false;
                        } else {
                            return true;
                        }
                    }
                    if(node.left is not null) queue.Enqueue(node.left);
                    if(node.right is not null) queue.Enqueue(node.right);
                    //Put in null node to distinguish sibling and cousin
                    queue.Enqueue(null);
                }
            
                if(couldbeCousins) {
                    return false;
                }
            }
            return false;
        }
    }
}