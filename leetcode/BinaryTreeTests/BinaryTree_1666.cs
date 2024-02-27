namespace BinaryTreeTests;

[TestFixture]
internal class BinaryTree_1666
{
    class Solution {
        public Node FlipBinaryTree(Node root, Node leaf) {         
            var curr = leaf;
            Node prev = null;
            while( curr != null )
            {
                // curr's left make as curr right child .
                if( curr.left != null ) curr.right = curr.left;
                // curr's parent  make as  curr's left child 
                if( curr.parent != null)
                {   
                    curr.left = curr.parent; 
                    if( curr.parent.left == curr) // if curr is left child - make that null 
                        curr.parent.left = null; 
                    else if( curr.parent.right == curr) // if curr is right child - make that null 
                        curr.parent.right = null;   
                    curr.parent = prev;  
                }else {
                    curr.parent = prev;
                }
                       
                prev = curr; //  keep him as  new parent 
                curr = curr.left;  // move to it's left  [ actually original parent ]
                if( curr == root) // if we reach root , just  break .
                {
                    curr.parent = prev;
                    break;
                }
            }        
            return(leaf);  
        }
    }
}