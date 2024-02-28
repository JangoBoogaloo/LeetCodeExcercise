namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_510
{
    class Solution {
        public Node InorderSuccessor(Node x) {
            if(x is null) return null;
            if (x.right is not null) {
                x = x.right;
                while(x.left is not null) x = x.left;
                return x;
            }
            
            //           target 
            //           /
            //       node
            //          \
            //           x
            while(x.parent is not null && x == x.parent.right) {
                x = x.parent;
            }
            return x.parent;
        }
    }
}